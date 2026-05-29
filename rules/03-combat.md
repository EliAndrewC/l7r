# Combat

## Initiative

Combat is divided into **rounds**, each of which has 10 **phases**.  You begin each round by rolling dice equal to your Void Ring plus 1 without spending void points or rerolling 10s, and keeping all but the highest die.  These are called **action dice** because each represents one action, and the number showing on each die is the phase in which that action takes place.

Taking an action **spends** one action die in the current phase.  An action die not spent in its phase becomes a **held action**, and may be spent in any future phase.  Held actions not spent by the end of Phase 10 are lost.

If two characters act in the same phase, the one with the lowest action die goes first.  If this is tied, compare their second-lowest action dice, and so on.  If they have the same action dice, the character with higher Void wins, and if their Void is tied then flip a coin.


## Attacking and Parrying

All characters begin with two advanced skills at 1: attack (which uses Fire) and parry (which uses Air).  Attacking has a TN of 5 plus 5 times the defender's parry skill.  If the TN is not met, the attack fails.  Otherwise, the defender may attempt to parry, with the TN being the result of the attack roll.  Characters may parry for each other, but the TN is raised by 5 times the attacker's attack skill.  If a parry succeeds, the attack fails.

If your character wishes to parry but has no actions in the current phase, you may take an **interrupt action**.  Spending any 2 action dice creates an interrupt action in the current phase, which may be used to parry.  If you decide to parry before the attack is rolled, you get a free raise to your parry.


## Damage

Your base damage depends on your weapon and Fire.  This damage starts at 4k2 for katana, 3k2 for spears and wakizashi, 2k2 for knives and other small weapons, and 0k2 for unarmed fighting.  You also add your Fire to the number of rolled dice of your base damage.  You can't spend void points on damage, but you roll an extra die for every 5 by which your attack roll exceeded its TN.  If the defender attempted and failed to parry, you don't roll these extra damage dice.

When your characters gets hit, the damage is added to your character's **light wound total**.  You then roll (Water+1)k(Water) as a **wound check**.  The TN for this roll is your character's light wound total.

If you fail this roll, your character takes 1 **serious wound** plus 1 serious wound for every 10 by which you failed the wound check, and the light wound total is set back to 0.  If you succeed, you may either keep all light wounds or take 1 serious wound to reduce the light wound total to 0.

When the **serious wound total** meets or exceeds your character's Earth Ring, your character is **impaired**.  While impaired, you no longer reroll 10s for any skill, but you still reroll 10s on non-skill rolls such as wound checks and damage rolls.  When the serious wound total reaches twice your character's Earth Ring, your character is mortally wounded and unable act.

Characters heal 1 serious wound every other night, starting the first night after damage is taken.  The GM may decide to speed this up or slow it down depending on the physical exertion your character undergoes while wounded.  Light wounds can be automatically healed after combat with rudimentary first aid.


## Iaijutsu Duels

Before a duel begins, you stand motionless a few feet from your opponent and **show your stance**.  Each duelist makes an open roll to discern the opponent's Fire Ring, using iaijutsu with Air.  This tells you that your opponent has at least X Fire, where X is your roll divided by 5 (rounded down).  If X exceeds their Fire, you know for certain what it is.  This roll also allows you to discern your opponent's starting TN (see below) in the same fashion.

After this, the participants make a contested iaijutsu roll.  Each duelist's TN to be hit begins at their experience point total divided by 10, rounded down.  The duelists take turns choosing whether to **focus** or **strike**.  The winner of this contested roll chooses first.

When you declare a focus, your character's TN to be hit is raised by 5.  When a strike is declared, both duelists attack simultaneously using iaijutsu.  You roll 1 extra damage die for every 1 by which your iaijutsu roll exceeded its TN instead of for every 5, and each rolled die above 10k10 adds +5 instead of +2.  Void points can't be spent and 10s aren't rerolled on either these rolls or the wound checks they cause, but they are rolled on the resulting damage rolls.

If neither participant hits, both duelists resheathe their katana and restart the duel.  Whoever rolled higher receives a free raise to all future iaijutsu rolls for the remainder of the duel.  Both characters get this free raise if they roll the same amount.  When at least one duelist hits, the duel switches from iaijutsu to kenjutsu, and normal combat rules apply.


## Movement and Positioning

As with most rules in L7R, our goal with movement and positioning rules is to keep things as simple as possible, while still allowing players to say things like "I'd like to make an effort to move more quickly" or "I'd like to reposition myself within the fight to go over to where that other guy is" and have a mechanical framework by which we can say how this will work and what consequences may result.

Quite often, characters remain in one place for the entire round, engaging with the enemy without withdrawing from the fight or needing to pursue a fleeing opponent.  When fighting in formation, there is often little need to move, and the combat rules largely presume that most combats will be relatively stationary.  However, as a fight progresses, characters may wish to reposition themselves to e.g. cut off a retreat or gain a tactical advantage.

Movement speed is tricky to define at the level of a phase, because while a combat round is 10 seconds long, phases are more abstract.  A single phase can be several seconds long, in cases where many characters take several sequential actions in a row.  Alternatively, several phases in a row might represent no time passing at all, in situations where no character has any actions available.  That said, in some instances where actions are held and characters are assessing one another while waiting and deciding how to act next, a pause of multiple phases without any actions being spent may represent the combatants catching their breath while staring down their enemies as they prepare to strike.  Thus, while we can say "what is a character's approximate speed per combat round", per-phase movement speed is not a coherent concept, as phases do not represent a fixed amount of time.

Characters automatically get ~50 feet of movement per round, though this may be affected by the terrain.  Characters may be able to move a fraction of this amount when on unstable footing, or when forced to navigate around obstacles.  Alternatively, the amount may be higher on a large flat area, or when running downhill.

Regardless, for the reasons explained above, 50 feet of movement per round does not necessarily translate into 5 feet of movement per phase, though in some cases it might.  In a fight where some characters are giving chase to their opponents, and everyone is constantly moving in the same direction, the GM would likely divide each character's movement into a per-phase velocity.  In other cases where the actions for the round mostly occur in 2-3 bursts throughout the phase, the GM might pause in the middle of a phase to ask "do you want to move between those two actions?"  When players decide not to move when the option is available, they are **spending down** some of this 50 feet of movement for the round.  Changes to a character's movement such as halting their motion or changing direction may decrease the movement per round.

Characters who wish to move at a greater rate may spend 1 **action** per round on movement.  They may decide to do this at any time in the round, spending any action die from any phase to do so, i.e. you do not need to wait until an action is available to begin moving, and a character who does not act until phase 5 may spend a phase 10 action die as early as phase 1.  Spending this action gives you an extra number of feet of movement per round equal to 50 times your Earth Ring.  For example, a character with 3 Earth would get a total of 200 feet of movement for the round (50 + 3 * 50).  If not activated until later in the round, then a portion of this extra movement may already be considered "spent down" in the same way that choosing not to move when given the option uses up some of your available movement.

Our general combat rules presume that defenders can see their attackers.  When a target cannot see the attack coming at them, their normal TN of (5 + 5 * parry) becomes 0, and the defender cannot parry or use discretionary bonuses on their wound checks, e.g. they cannot spend discretionary bonuses such as void points or school abilities on the wound check.  (Constant bonuses such as +1k0 from a 1st Dan technique or a free raise to wound checks from a 2nd Dan technique are still added, but discretionary bonuses such as free raises from a 3rd Dan technique may not be added.)

When a character is **surrounded** by two or more others, all attackers get a bonus of (5 + 5 * surrounders) to all types of attack rolls.  For example, if three people are surrounding 1 opponent, they each receive +20 to their attack rolls against that opponent (5 + 3 * 5).

Someone who is surrounded might decide to try to move between their attackers to escape.  In general, moving between 2 opponents grants each of them a **free provoked attack** roll against the opponent moving between them.  This roll may be made with either the attack skill or the counterattack knack.  Characters may take no more than X / 2 (round up) free provoked actions per round, where X is equal to their attack skill, and may not attack more than once per provocation.


## Archery Rules

Here are the high-level things we are trying to accomplish with these rules:

- You miss more often than with normal attacks.
- You deal more damage than normal hits when you do hit.
- There is more variance (e.g. the amount of damage is more randomized).
- Bushi school knacks can help (specifically double attack, iaijutsu, and counterattack).
- Hitting close targets is easier than hitting targets far away.
- Taking cover helps you avoid being hit.

Shooting a bow and arrow works much like any other attack.  You make a normal initiative roll, and each action can be an attack, made with the regular **attack** skill.  However, *all* types of bonuses to attack rolls and damage rolls for *all* types of attacks stack (e.g. a 4th Dan Kakita bushi gets +2k0 + 5 to archery attack rolls because they get to add both the +1k0 iaijutsu and +1k0 double attack to the attack roll from their 1st Dan, +5 to iaijutsu attack rolls from their 2nd Dan, and +5 to damage from their 4th Dan technique which is normally to iaijutsu).

When firing an arrow, you receive a bonus to your attack roll equal to the number of phases the action was held.  This number resets to zero after another arrow is fired, e.g. if someone has a phase 1 action and a phase 2 action, and they fire an arrow in phase 5, then they get +4 to their attack roll (because they were holding the action for 4 phases).  If they fire another arrow in the same phase, they receive a +0 bonus since firing the first arrow reset the accumulated bonus to 0.  You may also spend any number of extra actions available in the current phase to get +5 to the attack roll per extra action spent, and any bonuses from holding those actions also apply.  Finally, characters with the iaijutsu skill receive an additional bonus to their attack roll equal to their iaijutsu.

Here's how arrow damage works:

- Arrows deal an automatic **serious wound** when they hit.
- Characters with the **double attack** knack automatically add 1 additional serious wound to the damage (i.e. 2 automatic serious wounds), without any effect on the TN.
- In addition to automatic serious wounds, each arrow deals a variable amount of damage, with the base chances occurring according to this probability chart:
    - 30% chance: 10k2
    - 30% chance: 10k4
    - 30% chance: 10k6
    - 10% chance: 10k8
- Exceeding the TN to hit does not result in extra rolled damage dice.  Instead, every increment of 5 shifts 10% from the lowest remaining damage roll to the 10k8 result.  For example, if someone exceeds the TN to hit by 12, the adjusted probabilities look like this:
    - 10% chance: 10k2
    - 30% chance: 10k4
    - 30% chance: 10k6
    - 30% chance: 10k8
- And if someone exceeds the TN to hit by 22 then the probability looks like this:
    - 20% chance: 10k4
    - 30% chance: 10k6
    - 50% chance: 10k8
- After we have reached a 100% chance of a 10k8 damage roll, every extra increment of 5 above the TN (i.e. after we have exceeded the TN to hit by more than 45), every additional increment of 5 adds a free raise to the damage roll.

### TN to be hit

When facing the archer and able to see the arrows coming, targets begin at their normal TN (5 + 5 * parry), modified by this table:

| Distance      | Modifier  |
| ------------- | --------- |
| 0 - 49 ft     | +5        |
| 50 - 99 ft    | +10       |
| 100 - 199 ft  | +15       |
| 200 - 399 ft  | +20       |
| 400+ ft       | n/a       |

Anything above ~400 ft is beyond the range of a standard bow to hit a moving target.  Targets have the option to spend 1 action per round on **evasion**, i.e. bobbing and weaving to increase their TN to be hit by arrows by 5 for the entire round.  This is in addition to being able to spend 1 action to increase their movement for the round, and like spending an action for movement, you may spend an action from any phase regardless of what the current phase is.

Targets unable to see the arrow coming have a base TN of 5 (increased by the above modifiers as applicable), and the usual rules apply: you may not attempt to parry or spend void points or other discretionary bonuses on the wound check.  Taking **cover** can make a character completely impossible to hit, or add an arbitrary amount to the TN, typically between +10 and +30 for partial cover.

### Parrying

Parry rolls are as normal, i.e. the TN of the parry is the result of the attack roll.  A successful parry roll negates the attack entirely, as it does with other attacks.  A failed parry roll negates the automatic serious wound but does not affect the damage in any other way (i.e. it does not negate the extra automatic serious wound from double attack or the probability adjustments from the attacker exceeding the TN to hit).  A parry attempt costs 10 feet of movement per round (see below).

### Movement

As always, characters can move ~50 feet per round without spending any actions, and they can spend 1 action from any phase to move an additional number of feet per round equal to 50 times their Earth Ring.  A character who changes directions or suddenly leaves cover or dodges a different archer's attack may be counterattacked by characters with the **counterattack** knack.
