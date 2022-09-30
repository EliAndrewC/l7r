
from abc import ABC, abstractmethod

from simulation.events import DeathEvent, LightWoundsDamageEvent, SeriousWoundsDamageEvent, TakeSeriousWoundEvent, UnconsciousEvent, WoundCheckDeclaredEvent, WoundCheckFailedEvent, WoundCheckRolledEvent, WoundCheckSucceededEvent

class Listener(ABC):
  '''
  Class that responds to an Event for a Character.
  A Listener should be the only way that a Character's state is modified during a simulation.
  Listeners should not make decisions, they should only implement rules.
  If a Character has a choice about how to respond to an Event,
  then the Listener for that Event should consult a Strategy.
  '''
  @abstractmethod
  def handle(self, character, event, context):
    '''
    handle(character, event, context) -> Event or None
      character (Character): the Character that is responding to the Event
      event (Event): the Event that is being handled
      context (EngineContext): context about other Characters and groups of Characters

    Handles an Event for a Character. Returns another Event if appropriate, or returns nothing.
    This function must determine if the Character needs to respond to the Event.
    If the Character needs to make a decision about how to respond -
    for example, what kind of action to take, or whether to parry or counterattack,
    or whether to spend resources like void points - then this
    function gets a Strategy from the Character and delegates the decision to the Strategy.
    '''
    pass


class NewRoundListener(Listener):
  def handle(self, character, event, context):
    character.roll_initiative()


class NewPhaseListener(Listener):
  def handle(self, character, event, context):
    return character.action_strategy().recommend(character, event, context)


class AttackDeclaredListener(Listener):
  def handle(self, character, event, context):
    if character != event.subject():
      # respond to another character's attack
      return character.attack_declared_strategy().recommend(character, event, context)
 

class AttackRolledListener(Listener):
  def handle(self, character, event, context):
    if event.action.subject() != character:
      character.knowledge().observe_attack_roll(event.action.subject(), event.roll)
    return character.parry_strategy().recommend(character, event, context)


class FeintSucceededListener(Listener):
  def handle(self, character, event, context):
    if event.action.subject() == character:
      if event.action.skill() == 'feint':
        character.gain_tvp(1)
        if len(character.actions()) > 0:
          max_action = max(character.actions())
          character.actions().remove(max_action)
          character.actions().insert(context.phase())
          return InitiativeChangedEvent()


class LungeDeclaredListener(Listener):
  def handle(self, character, event, context):
    if event.action.subject() != character:
      if event.action.skill() == 'lunge':
        # TODO: how to deal with the lunge bonus?
        pass


class LightWoundsDamageListener(Listener):
  def handle(self, character, event, context):
    if isinstance(event, LightWoundsDamageEvent):
      if event.target == character:
        character.take_lw(event.damage)
        character.knowledge().observe_damage_roll(event.target, event.damage)
        return character.wound_check_strategy().recommend(character, event, context)

# TODO: write an AkodoLightWoundsDamageListener and strategy that considers the post-roll bonuses


class SeriousWoundsDamageListener(Listener):
  def handle(self, character, event, context):
    if isinstance(event, SeriousWoundsDamageEvent):
      if event.target == character:
        character.take_sw(event.damage)
        if not character.is_alive():
          return DeathEvent(character)
        elif not character.is_conscious():
          return UnconsciousEvent(character)
        elif not character.is_fighting():
          return SurrenderEvent(character)
      else:
        character.knowledge().observe_wounds(event.target, event.damage)

class TakeActionListener(Listener):
  def handle(self, character, event, context):
    if isinstance(event, TakeActionEvent):
      if character == event.subject:
        # spend resources if necessary
        if event.action.ap() > 0:
          character.spend_ap(event.action.skill(), event.action.ap())
        if event.action.vp() > 0:
          character.spend_vp(event.action.vp())
      else:
        character.knowledge().observe_action(event.subject)

class TakeSeriousWoundListener(Listener):
  def handle(self, character, event, context):
    if isinstance(event, TakeSeriousWoundEvent):
      if event.target == character:
        character.reset_lw()
        return SeriousWoundsDamageEvent(character, event.damage)
      else:
        character.knowledge().observe_wounds(event.target, event.damage)

class WoundCheckDeclaredListener(Listener):
  def handle(self, character, event, context):
    if isinstance(event, WoundCheckDeclaredEvent):
      if event.subject == character:
        roll = character.roll_wound_check(event.damage, event.vp)
        return WoundCheckRolledEvent(character, event.damage, roll)


class WoundCheckFailedListener(Listener):
  def handle(self, character, event, context):
    if isinstance(event, WoundCheckFailedEvent):
      if event.subject == character:
        sw = character.wound_check(event.roll)
        character.reset_lw()
        return SeriousWoundsDamageEvent(character, sw)


class WoundCheckRolledListener(Listener):
  def handle(self, character, event, context):
    if isinstance(event, WoundCheckRolledEvent):
      if event.subject == character:
        if event.roll <= event.damage:
          # wound check failed
          return WoundCheckFailedEvent(character, event.damage, event.roll)
        else:
          return WoundCheckSucceededEvent(character, event.damage, event.roll)


class WoundCheckSucceededListener(Listener):
  def handle(self, character, event, context):
    if isinstance(event, WoundCheckSucceededEvent):
      if event.subject == character:
        # if the character may keep LW, consult the character's light wounds strategy
        return character.light_wounds_strategy().recommend(character, event, context)

