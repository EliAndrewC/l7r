# Domain Budgets

Per-tier budget breakdowns for the median domain hierarchy, plus supporting tables.

## Contents

- [What These Populations Count](#what-these-populations-count)
- [What the Samurai Counts Mean](#what-the-samurai-counts-mean)
- [Samurai Stipend Convention](#samurai-stipend-convention)
- [Domain](#domain)
  - [Samurai](#samurai)
  - [Budget](#budget)
  - [Combined Budgets](#combined-budgets)
- [Province](#province)
  - [Samurai](#samurai-1)
  - [Budget](#budget-1)
  - [Tax Farming Cost by Tier](#tax-farming-cost-by-tier)
- [County](#county)
  - [Samurai](#samurai-2)
  - [Skilled Ashigaru](#skilled-ashigaru)
  - [Ashigaru](#ashigaru)
  - [Budget](#budget-2)
- [Ministry Budgets](#ministry-budgets)
  - [Domain Ministry Budgets](#domain-ministry-budgets)
  - [Provincial Ministry Budgets](#provincial-ministry-budgets)
  - [Cross-cutting project negotiation](#cross-cutting-project-negotiation)
- [Example Office-Holder Budgets](#example-office-holder-budgets)
  - [Magistrate Kakita Hikai of Seitoyama County](#magistrate-kakita-hikai-of-seitoyama-county)
    - [Income](#income)
    - [Mandatory expenses](#mandatory-expenses)
    - [Gift income (in addition to tax revenue)](#gift-income-in-addition-to-tax-revenue)
    - [Discretionary residual](#discretionary-residual)
    - [Hikai's discretionary breakdown](#hikais-discretionary-breakdown)
    - [Summary](#summary)
  - [Governor Kakita Asuka of Tsurugamine Province](#governor-kakita-asuka-of-tsurugamine-province)
    - [Income](#income-1)
    - [Mandatory expenses](#mandatory-expenses-1)
    - [Gift income](#gift-income)
    - [Discretionary residual](#discretionary-residual-1)
    - [Asuka's discretionary breakdown](#asukas-discretionary-breakdown)
    - [Summary](#summary-1)
- [Capital City](#capital-city)
- [Provincial City](#provincial-city)
- [Town](#town)
- [Village](#village)
- [Hamlet](#hamlet)
- [Tax Pie](#tax-pie)
- [Land Productivity](#land-productivity)
  - [Unit Conversions: land area to rice koku](#unit-conversions-land-area-to-rice-koku)
  - [Per-Family Reference](#per-family-reference)
  - [Farm Families by Tier (per Domain)](#farm-families-by-tier-per-domain)
  - [Arable Land Allocation (per Domain)](#arable-land-allocation-per-domain)
  - [Rice Productivity by Land Quality](#rice-productivity-by-land-quality)
  - [Wheat Productivity by Land Quality](#wheat-productivity-by-land-quality)

## What These Populations Count

The "population" figures in this document mean different things at different tiers, and the differences matter for the math downstream (see [`l7r.md` - The Median Domain](l7r.md#the-median-domain) for the canonical per-tier population ranges):

- **Hamlet (~50-100, average ~75) and Village (~200-500, average ~350)**: counts every person living in that settlement.  These are pure farming communities - a hamlet is just a cluster of farmhouses; a village is several clusters around multiple large fields plus a slightly larger headman's household.  No burakumin in most rural settlements, as burakumin live in towns and cities where their specialty trades have customers.
- **Town (~900-1,500, average ~1,200)**: counts the in-and-around population.  Most town residents are farmers (~65%) because the working farmland immediately surrounding a county town is included in the town's population.  Border towns tend to be walled, whereas towns which do not need to maintain this level of military preparedness have a much more porous boundary and lack a clear inside-vs-outside boundary.  A "county" is the town plus its surrounding village districts.
- **Provincial city (~2,000-4,000, average ~3,000) and Capital city (~12,000)**: counts ONLY the population living within the city walls / on the city's footprint proper.  Cities are nearly always built on top of (or beside) very fertile land, and that land is farmed - but the farmers who work it live in villages and hamlets in the *surrounding county*, not in the city itself, which will almost always be walled and thus have rigorous demarcation between their urban interior and agricultural exterior.  That is why both city tiers show zero farmers in their caste tables.

The practical result: a capital city of ~12,000 is a city of ~12,000 administrators / artisans / soldiers / merchants / servants, ringed by farming villages whose inhabitants are counted under the surrounding rural settlement totals.  Likewise the ~6 provincial cities of a domain - each ~2,000-4,000 inside the walls, surrounded by farming villages counted in other population totals.

## What the Samurai Counts Mean

The samurai populations in the per-tier sub-tables (~1,000 in the capital, ~250 per provincial city, ~15 per county town, for a per-domain total of ~3,000) refer specifically to the **useful working cohort**: samurai past their gempukku and not yet retired.  The total samurai population per domain, including children and retirees living in their family households, is approximately **5,000** (per [`l7r.md` - The Median Domain](l7r.md#the-median-domain)).  The 60% useful figure replaces an older 80% estimate; earlier versions of these tables showed ~4,000 working samurai under that older rule.  Children and retirees consume from their family's resources rather than from a separate government allocation, so they do not appear as line items in these budgets.

## Samurai Stipend Convention

The Stipend column in the per-tier Samurai sub-tables shows the mean **average** annual stipend per working samurai at each tier.  Individual stipends follow the rank-squared rule (`stipend = rank^2`, per [`l7r.md` - Accordances of Rank](l7r.md#accordances-of-rank)): a Rank 1 bushi receives 1 koku, a Rank 5 county magistrate receives 25 koku, a Rank 10 minister 100 koku, a Rank 12 daimyo 144 koku.

The average varies by tier because the rank distribution does:

- **County town samurai**: ~10 koku average (avg rank ~3).  A typical county town's 15 samurai include 1 magistrate (Rank 5, 25 koku), the magistrate's karo and ~3 squad sergeants (Rank 4, 16 koku each), ~3 squad corporals (Rank 3, 9 koku each), and the remainder mostly Rank 2-3 bushi.
- **Provincial city samurai**: ~15 koku average (avg rank ~3-4).  Provincial cities house the provincial governor (Rank 8), six provincial ministers (Rank 7) and their deputies (Rank 6), mid-rank clerks (Rank 3-5), and rank-and-file bushi assigned to provincial administrative and military duties.
- **Capital city samurai**: ~35 koku average (avg rank ~5-6).  The capital is staffed with the senior cohort - the daimyo (Rank 12), councilors (Rank 11), domain ministers (Rank 10) and their deputies (Rank 9), high-rank clerks (Rank 7-8), castle guards and household retainers from the daimyo's elite retinue, and junior officials in training for higher posts.  Low-rank samurai compose a lower proportion of retainers in the capital than in the provinces.

**Stipends are paid by whoever holds the relevant tax-farming cut at the tier where the samurai serves**: the median daimyo's ~100,000-koku cut covers capital stipends; each provincial governor's (on average) ~10,000-koku cut covers their province; each county magistrate's (on average) ~1,000-koku cut covers their county.  Cross-tier flow does not happen for stipends as it does for gifts and lineage finances - a provincial samurai is paid by their governor regardless of which lineage the samurai or governor belongs to (see [`l7r.md` - Samurai Lineages](l7r.md#samurai-lineages) for the discussion of how lineage politics and fiscal flow interact).

## Domain

| Place | N | T | P | Total Tax | Total Pop |
| --- | --- | --- | --- | --- | --- |
| Capital city | 1 | 24888 | 12000 | 24888 | 12000 |
| Provincial city | 6 | 6222 | 3000 | 37332 | 18000 |
| Town | 36 | 1603.2 | 1200 | 57715 | 43200 |
| Village | 216 | 350 | 350 | 75600 | 75600 |
| Hamlet | 1296 | 75 | 75 | 97200 | 97200 |
| **Total** |  |  |  | 292735 | 246000 |

### Samurai

| Place | N | P | Stipend | Food | Housing | Equipment | Other | Population | Payroll | Total Food | Total Housing | Total Equipment | Total Cost |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Capital city | 1 | 1000 | 35 | 3 | 0 | 2 | 0 | 1000 | 35000 | 3000 | 0 | 2000 | 40000 |
| Provincial city | 0 | 250 | 15 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Town | 0 | 0 | 10 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Village | 0 | 0 | 10 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Hamlet | 0 | 0 | 10 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** |  |  |  |  |  |  |  | 1000 | 35000 | 3000 | 0 | 2000 | 40000 |

### Budget

| Category | Expense |
| --- | --- |
| Staff | 1000 |
| Samurai | 40000 |
| Ashigaru | 0 |
| Servants | 240 |
| Supplies | 120 |
| **Total** | 41360 |

### Combined Budgets

| Place | N | Cost | Tax Farming | Total Cost |
| --- | --- | --- | --- | --- |
| Domain | 1 | 41360 | 100000 | 141360 |
| Province | 6 | 5030 | 10000 | 90180 |
| County | 36 | 445 | 1000 | 52020 |
| **Total** |  |  |  | 283560 |

## Province

| Place | N | T | P | Total Tax | Total Pop |
| --- | --- | --- | --- | --- | --- |
| Capital city | 0 | 24888 | 12000 | 0 | 0 |
| Provincial city | 1 | 6222 | 3000 | 6222 | 3000 |
| Town | 6 | 1603.2 | 1200 | 9619 | 7200 |
| Village | 36 | 350 | 350 | 12600 | 12600 |
| Hamlet | 216 | 75 | 75 | 16200 | 16200 |
| **Total** |  |  |  | 44641 | 39000 |

### Samurai

| Place | N | P | Stipend | Food | Housing | Equipment | Other | Population | Payroll | Total Food | Total Housing | Total Equipment | Total Cost |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Capital city | 0 | 1000 | 35 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Provincial city | 1 | 250 | 15 | 3 | 0 | 2 | 0 | 250 | 3750 | 750 | 0 | 500 | 5000 |
| Town | 0 | 15 | 10 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Village | 0 | 0 | 10 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Hamlet | 0 | 0 | 10 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** |  |  |  |  |  |  |  | 250 | 3750 | 750 | 0 | 500 | 5000 |

### Budget

| Category | Expense |
| --- | --- |
| Staff | 0 |
| Samurai | 5000 |
| Ashigaru | 0 |
| Servants | 20 |
| Supplies | 10 |
| Tax Farming | 10000 |
| Total | 15030 |
| Remainder | 29611 |

### Tax Farming Cost by Tier

| N | C | Total |
| --- | --- | --- |
| 36 | 1000 | 36000 |
| 6 | 10000 | 60000 |
| 1 | 100000 | 100000 |

## County

| Place | N | T | P | Total Tax | Total Pop |
| --- | --- | --- | --- | --- | --- |
| Capital city | 0 | 24888 | 12000 | 0 | 0 |
| Provincial city | 0 | 6222 | 3000 | 0 | 0 |
| Town | 1 | 1603.2 | 1200 | 1603 | 1200 |
| Village | 6 | 350 | 350 | 2100 | 2100 |
| Hamlet | 36 | 75 | 75 | 2700 | 2700 |
| **Total** |  |  |  | 6403 | 6000 |

### Samurai

| Place | N | P | Stipend | Food | Housing | Equipment | Other | Population | Payroll | Total Food | Total Housing | Total Equipment | Total Cost |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Capital city | 0 | 1000 | 35 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Provincial city | 0 | 250 | 15 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Town | 1 | 15 | 10 | 3 | 0 | 2 | 0 | 15 | 150 | 45 | 0 | 30 | 225 |
| Village | 6 | 0 | 10 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Hamlet | 36 | 0 | 10 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** |  |  |  |  |  |  |  | 15 | 150 | 45 | 0 | 30 | 225 |

### Skilled Ashigaru

| Place | N | P | Rate | Stipend | Population | Payroll |
| --- | --- | --- | --- | --- | --- | --- |
| Capital city | 0 | 0 | 0.02 | 2 | 0 | 0 |
| Provincial city | 0 | 0 | 0.02 | 2 | 0 | 0 |
| Town | 1 | 0 | 0.02 | 2 | 0 | 0 |
| Village | 6 | 6.93 | 0.02 | 2 | 42 | 83 |
| Hamlet | 36 | 1.49 | 0.02 | 2 | 53 | 107 |
| **Total** |  |  |  |  | 95 | 190 |

### Ashigaru

| Place | N | P | Rate | Population |
| --- | --- | --- | --- | --- |
| Capital city | 0 | 0 | 0.1 | 0 |
| Provincial city | 0 | 0 | 0.1 | 0 |
| Town | 1 | 0 | 0.1 | 0 |
| Village | 6 | 31.5 | 0.1 | 189 |
| Hamlet | 36 | 6.75 | 0.1 | 243 |
| **Total** |  |  |  | 432 |

### Budget

| Category | Expense |
| --- | --- |
| Staff | 0 |
| Samurai | 225 |
| Ashigaru | 190 |
| Servants | 20 |
| Supplies | 10 |
| Tax Farming | 1000 |
| Total | 1445 |
| Remainder | 4958 |

## Ministry Budgets

**Note on the term "tax farming"**: This document uses "tax farming" in its loose modern English sense - the structural pattern of officials keeping a share of taxes they collect as their compensation.  Strictly, tax farming refers to the Roman *publicani* model where collection rights were auctioned to private contractors who paid the state a fixed sum upfront and pocketed whatever they could extract above it.  The Rokugan system isn't that: Rokugani officials are appointed through the civil-service examination and chancellery selection process, not auctioned, and the size of each office's cut is fixed by tradition rather than competitive bidding.  Structurally, the Rokugan arrangement is closer to the Tokugawa *chigyō* (fief grant) or the medieval European prebend (office-attached income), where the official is a state official whose compensation is an attached tax allocation.  "Tax farming" is used here because it conveys the right intuition (the office-holder profits from extraction efficiency) and is the established casual English usage for this broader pattern, including in modern descriptions of the Mughal *jagir* and Ottoman *timar* systems which were similarly appointment-based rather than auctioned.

The Tax Farming line items in the Budget tables (~100,000 for the daimyo, ~10,000 per provincial governor, ~1,000 per county magistrate) are **total allocations** that cover both the office-holder's personal household income AND the ministry/operational obligations of their office.  An office-holder is expected to fund the activities of their tier's ministries out of their tax-farming cut.  How much they allocate to which ministry is partially fixed by tradition and necessity, partially negotiable.

The breakdowns below show the typical allocation at each tier.  Numbers are approximate and vary by domain, province, and the personalities and politics of the office-holders.  The **informal income** column shows the office-holder's effective personal take above their formal stipend, calculated as a ~10% skim on the ministry budget they administer ("a tithe", a customary rate built into many Rokugani fiscal formalities, e.g. the 10-koku Imperial registration fee on a 100-koku bounty).  Strictly speaking, this is not built into the budget, and in fact office holders are expected to pay all expenses related to their duties even if those expenses exceed their income.  As with tax farming, the presumption is that forward-thinking appointees will save their money in years of plenty so that they can spend their savings and/or make use of lineage reserves as needed in lean years as needed.  The 10% figure is thus only a loose average, and corrupt officials may extract more, while scruplulous samurai might consistently draw on family connections to make up chronic shortfalls without ever personally enriching themselves.

### Domain Ministry Budgets

The daimyo has approximately 109,000 koku/year available (their ~100,000 tax-farming cut plus the ~9,000-koku domain surplus residual).  Of this, roughly half funds domain ministry budgets:

| Allocation | Annual koku |
| --- | --- |
| **Daimyo's personal/household** | ~50,000 |
| **Domain ministry budgets** (sum) | ~50,000 |
| **Reserves / contingency** | ~9,000 |
| **Total** | ~109,000 |

The 50,000-koku ministry breakdown, with the resulting effective income for each Rank 10 minister:

| Ministry | Budget | Minister's stipend | Informal income (10% skim + throughput where applicable) | Minister's effective income |
| --- | --- | --- | --- | --- |
| Works | 30,000 | 100 | ~3,000 | **~3,100** |
| War | 7,000 | 100 | ~700 | **~800** |
| Rites | 6,000 | 100 | ~600 | **~700** |
| Justice | 3,000 | 100 | ~300 (formal) + variable from gifts and fines | **~400 (virtuous) to ~3,000+ (corrupt in a wealthy domain)** |
| Retainers | 3,000 | 100 | ~300 (formal) + ~2,000 (rice/coin arbitrage on capital stipend throughput of ~35,000) | **~2,400** |
| Revenue | 1,000 | 100 | ~100 (formal) + ~2,000 (tax-collection fees on throughput) | **~2,200** |
| **Total** | **50,000** |  |  |  |

Notice the **structural floor for the Minister of Justice is the lowest** of the six (~400 koku effective income at the modest end), but the **ceiling is uncapped**.  Ministers of Justice in wealthy domains can accept significant "gifts" from those under their judicial authority and assess fines whose amounts they set within wide precedential limits.  A virtuous Minister of Justice lives modestly on the formal ~400; a corrupt one in a wealthy domain can exceed even the Minister of Works; both extremes are well-attested in Rokugan.

The other ministries cluster more tightly around their budget-determined income.

### Provincial Ministry Budgets

Each provincial governor has 10,000 koku to work with (their entire tax-farming cut).  This splits roughly:

| Allocation | Annual koku per governor |
| --- | --- |
| **Governor's personal/household** | ~5,000 |
| **Provincial ministry budgets** (sum) | ~5,000 |
| **Total** | ~10,000 |

The 5,000-koku provincial ministry breakdown, with effective income for each Rank 7 provincial minister:

| Ministry | Budget per province | Minister's stipend | Informal income | Minister's effective income |
| --- | --- | --- | --- | --- |
| Works | 3,000 | 49 | ~300 | **~350** |
| War | 700 | 49 | ~70 | **~120** |
| Rites | 600 | 49 | ~60 | **~110** |
| Justice | 300 | 49 | ~30 (formal) + variable from gifts and fines | **~80 (virtuous) to ~500+ (corrupt in a wealthy province)** |
| Retainers | 250 | 49 | ~25 (formal) + ~200 (rice/coin arbitrage on ~3,750-koku provincial stipend throughput) | **~275** |
| Revenue | 150 | 49 | ~15 (formal) + ~450 (collection fees on ~44,000-koku province revenue throughput, ~1%) | **~510** |
| **Total** | **5,000** |  |  |  |

A few things to notice:

- The **provincial governor** at ~5,000 koku is the wealthiest provincial-tier official by a substantial margin - almost 10x the next-highest provincial minister (Revenue).
- The **county magistrate** at ~800-900 koku effective (their ~1,000 tax-farming cut minus ~100-200 for county operations) is actually wealthier than every provincial minister except Revenue, despite holding a lower rank (Rank 5 vs Rank 7).  This is well-known in Rokugan and explains why ambitious junior samurai often prefer a county magistrate appointment to a provincial ministry appointment.
- The **provincial Minister of Justice** at the virtuous floor (~80 koku) is genuinely poor for a Rank 7 official, comparable to a Tokugawa-era ordinary hizamurai.  The ceiling for a corrupt one in a wealthy province can exceed the Minister of Works.

### Cross-cutting project negotiation

For projects that span multiple tiers (a new canal across the domain, maintenance of a road that crosses several provinces, mobilization for clan warfare), the question of who pays which share is a major source of domain politics.  The general pattern:

- **Routine maintenance** stays at the tier responsible for that scope (county roads = magistrate; provincial roads = governor; capital infrastructure = daimyo)
- **Capital projects** are negotiated, often with the daimyo expecting affected governors to contribute from their provincial Works budgets, and governors arguing that domain-spanning projects should come from the domain Works budget alone
- **Emergencies** (war, famine relief) involve the daimyo drawing from their contingency reserves and demanding "emergency contributions" from governors above their normal budgets

A 10,000-koku canal project, for example, might be funded purely from domain Works (using 33% of that year's domain Works budget), or split as 6,000 from domain Works + 600-700 from each of 6 affected provinces' Works budgets.  Which solution prevails depends on the daimyo's bargaining position, the governors' political weight, and the lineage chancellors' opinions in the chancellery.

## Example Office-Holder Budgets

### Magistrate Kakita Hikai of Seitoyama County

Seitoyama is a county in Tsurugamine province of the Kakita domain (Crane clan).  Kakita Hikai is its current magistrate, a moderately conscientious official well-regarded by peasants and respected by their retainers.  The breakdowns below show Hikai's specific allocation choices; other magistrates with the same canonical 1,000-koku discretionary allocation but different personalities, lineage politics, or local circumstances allocate very differently.

#### Income

| Source | Households | Tax type | Total |
| --- | --- | --- | --- |
| Town farmers (1 town × ~156 households) | ~156 | Land tax (~5 koku/household) | ~780 |
| Village farmers (6 villages × ~70 households each) | ~420 | Land tax (~5 koku/household) | ~2,100 |
| Hamlet farmers (36 hamlets × ~15 households each) | ~540 | Land tax (~5 koku/household) | ~2,700 |
| Town merchants (very rich, rich, poor, and ordinary) | ~24 | Property + business | ~700 |
| Town laborers, servants, and burakumin | ~55 | Property + business | ~125 |
| **Total county tax revenue** |  |  | **~6,400** |

Math note: each farming household has ~5 members and pays ~5 koku per year in land tax (following the Rice and Arable-Land Math in [`l7r.md`](l7r.md#rice-and-arable-land-math)).  The ~1,116 farm families in the county contribute ~5,580 koku in farm taxes.  The remaining ~825 koku is property and business tax from town residents, dominated by the wealthy merchants - the very-rich merchant families pay ~235 koku each in combined property + business tax, while the ordinary "merchants, other" households pay ~5 koku each.  Per-household rates by caste sub-category are detailed in the [Town](#town) caste table further down in this document.

Seitoyama is a heavily agrarian county, so Magistrate Hikai's tax revenue comes almost entirely from land tax and ordinary town property/business taxes.  Local specialized industries do exist, e.g. the local clothier, sake brewer, etc, but their licenses are captured in the business tax column above and do not constitute a separate revenue stream.  Counties with major specialized industries (coastal counties with substantial fishing or salt-making operations, mountain counties with mining, river-junction counties with major brewing or paper-making) collect additional "small assessments" (in the Tokugawa *komononari* sense) beyond what is shown here, sometimes amounting to several hundred koku per year, occasionally more for an exceptional county.

#### Mandatory expenses

| Category | Annual koku | Notes |
| --- | --- | --- |
| Tax obligation to Governor Kakita Asuka | ~5,000 | The county's share of provincial revenue, passed up the chain |
| Samurai stipends (~15 useful samurai × ~10 koku avg) | ~150 | Rank-squared rule, avg rank ~3 |
| Samurai food allowance (~15 × ~3 koku) | ~45 |  |
| Samurai equipment allowance (~15 × ~2 koku) | ~30 |  |
| Ashigaru stipends | ~190 |  |
| Office servants | ~20 |  |
| Office supplies | ~10 |  |
| **Total mandatory** |  | **~5,445** |

#### Gift income (in addition to tax revenue)

Beyond tax revenue, Magistrate Hikai receives approximately **~150 koku per year in seasonal gifts** from local notables - primarily merchant landlords (the largest single category, since they hold most rural rentable land in the county), wealthy artisans and tradesmen (the sake brewer, the master smith, the dye-house owner), and ceremonial visitors from the magistrate's own lineage.

Unlike gifts to a Minister of Justice (which can shade into transactional bribery, since a Minister of Justice can directly grant rulings whose value far exceeds the gift), gifts to a county magistrate are predominantly **relational rather than transactional**.  The structural reason is that the magistrate's discretionary income depends on meeting their tax obligation to the governor: forgiving 1,000 koku of land tax owed by a merchant landlord in exchange for a 100-koku gift would be forgiving the county magistrate's own income, since the magistrate must make up any shortfall in their tax obligation to the provincial governor.  The most effective way for a landlord to keep a magistrate happy is therefore not large gifts but rather **efficient rent collection and avoidance of tenant disputes** that would otherwise require the magistrate's costly intervention.

Gifts to county magistrates therefore tend to be modest in size and timed to ceremonial occasions (New Year, the major festivals, the magistrate's birthday, etc).  A typical gift is a fine bolt of silk, a small barrel of premium sake, a piece of calligraphy by a renowned artist, or a brace of seasonal fish from a fortunate angler.  They communicate respect and maintain good relations rather than purchasing specific rulings.  A magistrate who receives unusually large gifts, or gifts at unusual times, has reason to wonder what specific favor the giver is preparing to request.

The size of an individual gift conventionally reflects the **rank of the recipient official**: the unit is one increment per rank, in whatever denomination matches the giver's means (or for gifts soliciting a specific action, the denomination is determined by the significance of the service being requested).  Since county magistrates are of the 5th rank (see [`l7r.md` - Accordances of Rank](l7r.md#accordances-of-rank)), a lavish birthday gift from a wealthy merchant landlord is expected to be ~5 koku worth (in gold coin or goods valued accordingly); a more modest local business might give a ~5-bu gift (silver, 1/10 the value); a freeholding peasant offering respects at New Year would give a ~5-zeni gift (copper, 1/100 the value).  The shared "5" makes the gesture immediately recognizable as proper to the magistrate's rank, while the denomination signals the giver's station.  A senior official receives gifts in correspondingly larger increments scaled to their own rank rather than the giver's: a wealthy merchant landlord might give a Rank 10 domain minister ~10 koku as a lavish gift, while a peasant offering respects to a Rank 8 provincial governor would give ~8 zeni.

#### Discretionary residual

Of the ~6,400-koku tax income, ~5,445 goes to mandatory expenses (~5,000 tax obligation to Governor Asuka + ~445 in stipends and office operations), leaving Magistrate Hikai with a **~955-koku tax-derived discretionary allocation**.  Combined with the ~150-koku gift income above, Hikai's effective total discretionary income is **~1,105 koku per year**.

#### Hikai's discretionary breakdown

This is specifically how Magistrate Hikai chooses to allocate their ~1,105-koku total discretionary income (~955 from tax surplus + ~150 from gifts).  Other magistrates with the same allocation distribute very differently (see below).

| Category | Annual koku | Type | Notes |
| --- | --- | --- | --- |
| Festival hosting and almsgiving (combined) | ~230 | Expected | Majority of this budget goes to almsgiving on festival days; the actual festival hosting costs are smaller than the alms distributed during them |
| County operations (prisoner food, jail upkeep, court materials, minor road and bridge repairs within the county) | ~100 | Expected | The samurai and ashigaru stipends in the mandatory section cover the *labor* of running the court and jail and patrolling the county roads; this line covers the *materials* and the minor infrastructure work that doesn't rise to provincial Works' attention |
| Retainer hospitality (food, sake, occasional lodging supplements for the ~15 samurai) | ~150 | Expected | Notionally retainers' stipends cover this, but in practice failure to provide leads to resentment and weak loyalty |
| Visitor hospitality (lineage chancellor visits, imperial inspectors, neighboring magistrates) | ~50 | Expected |  |
| Religious patronage (donations to county-town temple and small village shrines beyond the formal Rites budget) | ~50 | Expected |  |
| Lineage patronage donation to the Kakita chancellor | ~110 | Expected (~10%) | "Voluntary" but socially-pressured; the customary tithe on total discretionary income |
| **Subtotal: expected donations** | **~690** |  | ~62% of the allocation, consumed by never-required-but-always-expected obligations |
| Lean-year savings (forward-thinking reserve) | ~250 | Personal | ~23% put away against bad harvests; well above the irresponsible ~5-10% range that many magistrates of lesser foresight accept |
| Personal household and lifestyle (clothing, sword maintenance, family expenses) | ~105 | Personal | Gift income particularly helps here; many of the gifts received (silk, sake, fine goods) are themselves household-quality items that reduce out-of-pocket personal spending |
| Truly free (small luxuries, gifts to others, personal indulgences) | ~60 | Personal | About 1 koku per week of unconstrained spending |
| **Subtotal: personal/discretionary** | **~415** |  | ~38% of allocation, of which ~60 koku is truly unconstrained |
| **Total** | **~1,105** |  |  |

#### Summary

Magistrate Kakita Hikai is responsible for collecting ~6,400 koku in taxes annually from Seitoyama county, of which ~5,000 goes up to Governor Kakita Asuka and ~445 covers stipends and office expenses.  The remaining ~955 koku is Hikai's tax-derived discretionary income, supplemented by ~150 koku in seasonal gifts from local notables, for a total of ~1,105 koku per year.  After festivals, almsgiving, county operations, retainer hospitality, and the customary lineage tithe, ~415 koku is truly personal - of which Hikai is forward-thinking enough to save ~250 against future lean years.  Hikai's truly-unconstrained spending is around ~60 koku per year, comfortable but not lavish.

By all accounts Hikai is a virtuous magistrate.  One in their position who skimped on festivals or pocketed the lineage donation might keep two to three times that amount for themselves, at the cost of their standing in the lineage and the community.

### Governor Kakita Asuka of Tsurugamine Province

Tsurugamine is a province in the Kakita domain (Crane clan), containing Seitoyama county (administered by Magistrate Hikai, above) among its six counties.  Kakita Asuka is its current governor, a moderately accomplished official well-regarded within the Kakita Chancellery though not particularly distinguished in the broader Crane political landscape.  The breakdowns below show Asuka's specific allocation choices; other governors with the same canonical 10,000-koku tax-farming cut allocate very differently depending on the wealth of their province and their personal temperament.

#### Income

| Source | Annual koku | Notes |
| --- | --- | --- |
| Tax obligation from 6 county magistrates (~5,000 each) | ~30,000 | Standard provincial-tier share of county tax revenue; Hikai's ~5,000 obligation is one of these six |
| Provincial city direct tax base (property + business; dominated by very-rich and rich merchant households) | ~6,200 | Per the Provincial City caste table below |
| Provincial city import tariffs (Yasuki Taka system at the city gates) | ~7,800 | Varies by trade volume; Tsurugamine is a moderately trafficked province on the Kakita-Daidoji border |
| **Total provincial throughput** |  | **~44,000** |

#### Mandatory expenses

| Category | Annual koku | Notes |
| --- | --- | --- |
| Tax obligation to the Kakita family daimyo | ~34,000 | The province's share of domain revenue, passed up the chain |
| Provincial ministry budgets (sum across the six ministries) | ~5,000 | Per the [Provincial Ministry Budgets](#provincial-ministry-budgets) table above; covers samurai stipends across all six provincial ministries plus ministry operations |
| Asuka's personal samurai retinue (~10 samurai serving the governor directly, outside ministry assignments) | ~150 | Captain of the guard, household secretaries, personal yoriki; ~15 koku average for provincial-tier samurai |
| Governor's manor operations (servants, food, security, maintenance, stables) | ~1,000 |  |
| Governor's office operations (clerks, scribes, runners, supplies, courier service) | ~250 |  |
| **Total mandatory** |  | **~40,400** |

Math note: the 6 county magistrates pass up ~30,000 koku, the provincial city's own tax base contributes ~6,200, and the Yasuki Taka tariff system at the provincial city gates contributes the remaining ~7,800 - bringing total throughput to ~44,000.  Of this, ~34,000 goes up to the Kakita daimyo, leaving Asuka with her canonical 10,000-koku tax-farming cut.  Within that 10,000, the six provincial ministry budgets consume ~5,000 (covering all ministry samurai stipends and operations per the breakdown above); Asuka's personal retinue, manor, and office operations consume another ~1,400; the remaining ~3,600 is her tax-derived discretionary allocation.

#### Gift income

Beyond tax revenue, Governor Asuka receives approximately **~1,000 koku per year in seasonal gifts** from notables across Tsurugamine.  The major categories:

- **The 6 county magistrates under her authority** each give ceremonial gifts on New Year and the major festivals (~8 koku per occasion per magistrate, following the rank-scaled gift convention for the Rank 8 provincial governor; ~200 koku/year total)
- **Very-rich and rich merchant families in the provincial city** (~30 households between them; gifts scale by household wealth, totaling ~400 koku/year)
- **Wealthy merchant landlords from outlying counties** whose holdings span multiple counties and who therefore have province-wide rather than purely county-level concerns (~6 counties × 2-3 such families × ~5 koku/year ≈ ~80 koku)
- **Major sake brewers** in the province (a handful of large operations whose annual licenses approach 100 koku; gifts of ~15-20 koku/year each, totaling ~75 koku)
- **The six provincial ministers serving under Asuka** (~30 koku/year each; partially reciprocated since Asuka also gifts subordinates downward, so the net inflow is closer to ~100 koku)
- **Lineage chancellor and senior lineage members** (~75-100 koku, exchanged in both directions with substantial net symmetry)
- **Peer governors and visiting daimyo representatives** (variable, ~50 koku net inflow in a typical year)

This totals roughly 6-7x Magistrate Hikai's ~150-koku gift income.  The increase reflects the broader jurisdiction and richer pool of potential gifters - and the larger denominational increments scaled to the governor's higher rank - but NOT a qualitatively different scale that would mark transactional bribery.  A governor reporting 10x or more in gift income relative to a county magistrate is generally operating somewhere on the corrupt end of the spectrum.

Like gifts to a county magistrate, gifts to a provincial governor are predominantly **relational rather than transactional** for the same fiscal reasons: forgiving merchant tax obligations in exchange for gifts would forgive Asuka's own income, since she must meet her ~34,000-koku tribute obligation to the Kakita daimyo regardless.  The governor's structural temptation toward transactional gifts comes not from tax forgiveness but from **policy discretion** - provincial-level decisions about tariff rates on specific goods, road maintenance priorities between counties, market regulations at the provincial city, and recommendations to the daimyo about appointments can favor or harm specific merchant houses by amounts far exceeding any individual gift.  A virtuous governor declines gifts that arrive too close to such decisions; a corrupt governor in a wealthy province can extract substantially more than the ~1,000-koku baseline, with the ceiling set by the same factors that limit the Minister of Justice (visibility within the lineage, the daimyo's attention, the Imperial magistrate stationed in the domain capital).

#### Discretionary residual

Of the ~44,000-koku provincial throughput, ~40,400 goes to mandatory expenses, leaving Asuka with **~3,600-koku tax-derived discretionary allocation**.  Combined with the ~1,000-koku gift income, Asuka's effective total discretionary income is **~4,600 koku per year**.

#### Asuka's discretionary breakdown

This is specifically how Governor Asuka chooses to allocate her ~4,600-koku total discretionary income (~3,600 from tax surplus + ~1,000 from gifts).  Other governors with the same canonical allocation distribute very differently.

| Category | Annual koku | Type | Notes |
| --- | --- | --- | --- |
| Provincial festival hosting and almsgiving (combined) | ~800 | Expected | Provincial festivals are more elaborate than county festivals; almsgiving at provincial scale is more visible and politically important |
| Retainer hospitality (food, sake, occasional lodging for the ~10 personal retainers and the ~6 visiting county magistrates and ~6 provincial ministers Asuka entertains regularly) | ~600 | Expected | Notionally retainers' stipends cover their day-to-day; in practice failure to host generously erodes loyalty across the entire provincial command |
| Visitor hospitality (lineage chancellor visits, the Kakita daimyo's representatives, the Imperial magistrate, peer governors, Doji clan officials) | ~300 | Expected |  |
| Religious patronage (donations to the provincial abbot's temples and minor village shrines beyond the formal Rites budget) | ~200 | Expected |  |
| Lineage patronage donation to the Kakita chancellor | ~460 | Expected (~10%) | Customary tithe on total discretionary income; somewhat higher in absolute terms than Hikai's because Asuka's discretionary base is larger |
| **Subtotal: expected donations** | **~2,360** |  | ~51% of allocation, consumed by the same never-required-but-always-expected obligations that consume the majority of a county magistrate's discretionary income |
| Lean-year savings (forward-thinking reserve) | ~1,200 | Personal | ~26% put away against bad harvests, blight years, military levies, or unexpected provincial obligations |
| Personal household and lifestyle (clothing, sword maintenance, family expenses, political wardrobe for chancellery appearances) | ~700 | Personal | Higher than Hikai's because the governor's household includes a wider family circle plus visible political wardrobe expectations at the chancellery |
| Truly free (small luxuries, gifts to subordinates above the customary, personal indulgences) | ~340 | Personal | Around ~28 koku per month of unconstrained spending |
| **Subtotal: personal/discretionary** | **~2,240** |  | ~49% of allocation, of which ~340 koku is truly unconstrained |
| **Total** | **~4,600** |  |  |

#### Summary

Governor Kakita Asuka is responsible for collecting ~44,000 koku in tax revenue annually from Tsurugamine province, of which ~34,000 goes up to the Kakita family daimyo and ~5,000 funds the six provincial ministry budgets.  Another ~1,400 covers her personal samurai retinue and manor/office operations, leaving Asuka with a ~3,600-koku tax-derived discretionary allocation, supplemented by ~1,000 koku in seasonal gifts from the province's notables, for a total of ~4,600 koku per year.  After festivals, almsgiving, retainer and visitor hospitality, religious patronage, and the customary lineage tithe, ~2,240 koku is truly personal - of which Asuka is forward-thinking enough to save ~1,200 against future lean years.  Her truly-unconstrained spending is around ~340 koku per year, roughly 5-6x Magistrate Hikai's discretionary scale.

This reflects Asuka's higher tier and broader responsibilities, but it is NOT a fundamentally different lifestyle - the governor of a typical province lives perhaps as a wealthier-than-average mounted samurai might, not as a minor daimyo.  By all accounts Asuka is a virtuous-but-not-exceptional governor: she meets her obligations to the daimyo on time, refuses transactional gifts on contested policy decisions, hosts the expected festivals, and is well-regarded if not actively beloved within her lineage.  A more politically ambitious governor would cultivate the chancellery more aggressively (and pay for the cultivation out of personal savings); a less scrupulous one in the same role could extract two to three times Asuka's discretionary income through transactional policy gifts, at the cost of standing within the Kakita Chancellery and the Crane clan more broadly.

## Capital City

Total population: **~12,000**.

| P | Caste | Population | Families | Property | Business | Land | Total Tax |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20 | Servants | 2400 | 480 |  |  |  | 672 |
| 0 | servants, tutors | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | servants, temple | 0 | 0 | 0 | 0 | 0 | 0 |
| 5 | servants, wealthy samurai families | 600 | 120 | 2 | 0 | 0 | 240 |
| 3 | servants, wealthy merchant families | 360 | 72 | 2 | 0 | 0 | 144 |
| 7 | servants, non-wealthy samurai families | 840 | 168 | 1 | 0 | 0 | 168 |
| 3 | servants, non-wealthy merchant families | 360 | 72 | 1 | 0 | 0 | 72 |
| 2 | servants, miscellaneous | 240 | 48 | 1 | 0 | 0 | 48 |
| 40 | Laborers | 4800 | 960 |  |  |  | 5760 |
| 5 | laborers, master (rich) | 600 | 120 | 10 | 25 | 0 | 4200 |
| 5 | laborers, poor | 600 | 120 | 1 | 0 | 0 | 120 |
| 30 | laborers, other | 3600 | 720 | 2 | 0 | 0 | 1440 |
| 25 | Merchants | 3000 | 600 |  |  |  | 18240 |
| 2 | merchants, very rich | 240 | 48 | 25 | 225 | 0 | 12000 |
| 3 | merchants, rich | 360 | 72 | 10 | 25 | 0 | 2520 |
| 5 | merchants, poor | 600 | 120 | 1 | 3 | 0 | 480 |
| 15 | merchants, other | 1800 | 360 | 2 | 7 | 0 | 3240 |
| 5 | Burakumin | 600 | 120 |  |  |  | 216 |
| 0.5 | burakumin, well-off | 60 | 12 | 2 | 7 | 0 | 108 |
| 3 | burakumin, poor | 360 | 72 | 1 | 0 | 0 | 72 |
| 1.5 | burakumin, very poor | 180 | 36 | 1 | 0 | 0 | 36 |
| 0 | Farmers | 0 | 0 |  |  |  | 0 |
| 0 | farmer, urban tenant farmer | 0 | 0 | 2 | 0 | 15 | 0 |
| 0 | farmer, temple urban tenant farmer | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | farmer, rural tenant farmer | 0 | 0 | 2 | 0 | 15 | 0 |
| 0 | farmer, poor freeholder | 0 | 0 | 2 | 0 | 15 | 0 |
| 0 | farmer, freeholder | 0 | 0 | 2 | 0 | 15 | 0 |
| 0 | farmer, wealthy landowner | 0 | 0 | 5 | 0 | 15 | 0 |
| 10 | Samurai | 1200 | 240 |  |  |  | 0 |
| 1 | samurai, merchants | 120 | 24 | 0 | 0 | 0 | 0 |
| 1 | samurai, courtiers | 120 | 24 | 0 | 0 | 0 | 0 |
| 8 | samurai, bushi | 960 | 192 | 0 | 0 | 0 | 0 |
| 0 | samurai, shugenja | 0 | 0 | 0 | 0 | 0 | 0 |
| 100 | Total | 12000 | 2400 |  |  |  | 24888 |

## Provincial City

Total population: **~2,000-4,000, average ~3,000**.

| P | Caste | Population | Families | Property | Business | Land | Total Tax |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20 | Servants | 600 | 120 |  |  |  | 168 |
| 0 | servants, tutors | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | servants, temple | 0 | 0 | 0 | 0 | 0 | 0 |
| 5 | servants, wealthy samurai families | 150 | 30 | 2 | 0 | 0 | 60 |
| 3 | servants, wealthy merchant families | 90 | 18 | 2 | 0 | 0 | 36 |
| 7 | Indentured servants, non-wealthy samurai families | 210 | 42 | 1 | 0 | 0 | 42 |
| 3 | Indentured servants, non-wealthy merchant families | 90 | 18 | 1 | 0 | 0 | 18 |
| 2 | servants, miscellaneous | 60 | 12 | 1 | 0 | 0 | 12 |
| 40 | Laborers | 1200 | 240 |  |  |  | 1440 |
| 5 | laborers, master (rich) | 150 | 30 | 10 | 25 | 0 | 1050 |
| 5 | laborers, poor | 150 | 30 | 1 | 0 | 0 | 30 |
| 30 | laborers, other | 900 | 180 | 2 | 0 | 0 | 360 |
| 25 | Merchants | 750 | 150 |  |  |  | 4560 |
| 2 | merchants, very rich | 60 | 12 | 25 | 225 | 0 | 3000 |
| 3 | merchants, rich | 90 | 18 | 10 | 25 | 0 | 630 |
| 5 | merchants, poor | 150 | 30 | 1 | 3 | 0 | 120 |
| 15 | merchants, other | 450 | 90 | 2 | 7 | 0 | 810 |
| 5 | Burakumin | 150 | 30 |  |  |  | 54 |
| 0.5 | burakumin, well-off | 15 | 3 | 2 | 7 | 0 | 27 |
| 3 | burakumin, poor | 90 | 18 | 1 | 0 | 0 | 18 |
| 1.5 | burakumin, very poor | 45 | 9 | 1 | 0 | 0 | 9 |
| 0 | Farmers | 0 | 0 |  |  |  | 0 |
| 0 | farmer, urban tenant farmer | 0 | 0 | 2 | 0 | 15 | 0 |
| 0 | farmer, temple urban tenant farmer | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | farmer, rural tenant farmer | 0 | 0 | 2 | 0 | 15 | 0 |
| 0 | farmer, poor freeholder | 0 | 0 | 2 | 0 | 15 | 0 |
| 0 | farmer, freeholder | 0 | 0 | 2 | 0 | 15 | 0 |
| 0 | farmer, wealthy landowner | 0 | 0 | 5 | 0 | 15 | 0 |
| 10 | Samurai | 300 | 60 |  |  |  |  |
| 1 | samurai, merchants | 30 | 6 | 0 | 0 | 0 | 0 |
| 1 | samurai, courtiers | 30 | 6 | 0 | 0 | 0 | 0 |
| 8 | samurai, bushi | 240 | 48 | 0 | 0 | 0 | 0 |
| 0 | samurai, shugenja | 0 | 0 | 0 | 0 | 0 | 0 |
| 100 | Total | 3000 | 600 |  |  |  | 6222 |

## Town

Total population: **~900-1,500, average ~1,200**.

| P | Caste | Population | Families | Property | Business | Land | Total Tax |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5.5 | Servants | 66 | 13.2 |  |  |  | 18 |
| 0 | servants, tutors | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | servants, temple | 0 | 0 | 0 | 0 | 0 | 0 |
| 1.5 | servants, wealthy samurai families | 18 | 3.6 | 2 | 0 | 0 | 7.2 |
| 0.5 | servants, wealthy merchant families | 6 | 1.2 | 2 | 0 | 0 | 2.4 |
| 0.5 | Indentured servants, non-wealthy samurai families | 6 | 1.2 | 1 | 0 | 0 | 1.2 |
| 1 | Indentured servants, non-wealthy merchant families | 12 | 2.4 | 1 | 0 | 0 | 2.4 |
| 2 | servants, miscellaneous | 24 | 4.8 | 1 | 0 | 0 | 4.8 |
| 12 | Laborers | 144 | 28.8 |  |  |  | 86.4 |
| 1 | laborers, master (rich) | 12 | 2.4 | 5 | 20 | 0 | 60 |
| 1 | laborers, poor | 12 | 2.4 | 1 | 0 | 0 | 2.4 |
| 10 | laborers, other | 120 | 24 | 1 | 0 | 0 | 24 |
| 10 | Merchants | 120 | 24 |  |  |  | 698.4 |
| 1 | merchants, very rich | 12 | 2.4 | 10 | 225 | 0 | 564 |
| 1 | merchants, rich | 12 | 2.4 | 5 | 20 | 0 | 60 |
| 3 | merchants, poor | 36 | 7.2 | 1 | 1 | 0 | 14.4 |
| 5 | merchants, other | 60 | 12 | 1 | 4 | 0 | 60 |
| 5 | Burakumin | 60 | 12 |  |  |  | 20.4 |
| 0.5 | burakumin, well-off | 6 | 1.2 | 1 | 7 | 0 | 9.6 |
| 3 | burakumin, poor | 36 | 7.2 | 1 | 0 | 0 | 7.2 |
| 1.5 | burakumin, very poor | 18 | 3.6 | 1 | 0 | 0 | 3.6 |
| 0 | burakumin, maho-tsukai | 0 | 0 | 1 | 0 | 0 | 0 |
| 65 | Farmers | 780 | 156 |  |  |  | 780 |
| 0 | farmer, urban tenant farmer | 0 | 0 | 0 | 0 | 5 | 0 |
| 0 | farmer, temple urban tenant farmer | 0 | 0 | 0 | 0 | 0 | 0 |
| 55 | farmer, rural tenant farmer | 660 | 132 | 0 | 0 | 5 | 660 |
| 2.5 | farmer, poor freeholder | 30 | 6 | 0 | 0 | 5 | 30 |
| 5 | farmer, freeholder | 60 | 12 | 0 | 0 | 5 | 60 |
| 2.5 | farmer, wealthy landowner | 30 | 6 | 0 | 0 | 5 | 30 |
| 2.5 | Samurai | 30 | 6 |  |  |  |  |
| 0 | samurai, merchants | 0 | 0 |  |  |  |  |
| 0 | samurai, courtiers | 0 | 0 |  |  |  |  |
| 2.5 | samurai, bushi | 30 | 6 |  |  |  |  |
| 0 | samurai, shugenja | 0 | 0 |  |  |  |  |
| 100 | Total | 1200 | 240 |  |  |  | 1603.2 |

## Village

Total in-village population: **~200-500, average ~350**.

| P | Caste | Population | Families | Property | Business | Land | Total Tax |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Servants | 0 | 0 |  |  |  | 0 |
| 0 | servants, tutors | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | servants, temple | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | servants, wealthy samurai families | 0 | 0 | 2 | 0 | 0 | 0 |
| 0 | servants, wealthy merchant families | 0 | 0 | 2 | 0 | 0 | 0 |
| 0 | servants, non-wealthy samurai families | 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | servants, non-wealthy merchant families | 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | servants, miscellaneous | 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | Laborers | 0 | 0 |  |  |  | 0 |
| 0 | laborers, master (rich) | 0 | 0 | 5 | 25 | 0 | 0 |
| 0 | laborers, poor | 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | laborers, other | 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | Merchants | 0 | 0 |  |  |  | 0 |
| 0 | merchants, very rich | 0 | 0 | 10 | 225 | 0 | 0 |
| 0 | merchants, rich | 0 | 0 | 5 | 25 | 0 | 0 |
| 0 | merchants, poor | 0 | 0 | 1 | 3 | 0 | 0 |
| 0 | merchants, other | 0 | 0 | 1 | 7 | 0 | 0 |
| 0 | Burakumin | 0 | 0 |  |  |  | 0 |
| 0 | burakumin, well-off | 0 | 0 | 1 | 7 | 0 | 0 |
| 0 | burakumin, poor | 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | burakumin, very poor | 0 | 0 | 1 | 0 | 0 | 0 |
| 100 | Farmers | 350 | 70 |  |  |  | 350 |
| 0 | farmer, urban tenant farmer | 0 | 0 | 0 | 0 | 5 | 0 |
| 0 | farmer, temple urban tenant farmer | 0 | 0 | 0 | 0 | 0 | 0 |
| 80 | farmer, rural tenant farmer | 280 | 56 | 0 | 0 | 5 | 280 |
| 5 | farmer, poor freeholder | 17.5 | 3.5 | 0 | 0 | 5 | 17.5 |
| 10 | farmer, freeholder | 35 | 7 | 0 | 0 | 5 | 35 |
| 5 | farmer, wealthy landowner | 17.5 | 3.5 | 0 | 0 | 5 | 17.5 |
| 0 | Samurai | 0 | 0 |  |  |  |  |
| 0 | samurai, merchants | 0 | 0 |  |  |  |  |
| 0 | samurai, courtiers | 0 | 0 |  |  |  |  |
| 0 | samurai, bushi | 0 | 0 |  |  |  |  |
| 0 | samurai, shugenja | 0 | 0 |  |  |  |  |
| 100 | Total | 350 | 70 |  |  |  | 350 |

## Hamlet

Total population: **~50-100, average ~75**.

| P | Caste | Population | Families | Property | Business | Land | Total Tax |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Servants | 0 | 0 |  |  |  | 0 |
| 0 | servants, tutors | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | servants, temple | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | servants, wealthy samurai families | 0 | 0 | 2 | 0 | 0 | 0 |
| 0 | servants, wealthy merchant families | 0 | 0 | 2 | 0 | 0 | 0 |
| 0 | servants, non-wealthy samurai families | 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | servants, non-wealthy merchant families | 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | servants, miscellaneous | 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | Laborers | 0 | 0 |  |  |  | 0 |
| 0 | laborers, master (rich) | 0 | 0 | 5 | 25 | 0 | 0 |
| 0 | laborers, poor | 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | laborers, other | 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | Merchants | 0 | 0 |  |  |  | 0 |
| 0 | merchants, very rich | 0 | 0 | 10 | 225 | 0 | 0 |
| 0 | merchants, rich | 0 | 0 | 5 | 25 | 0 | 0 |
| 0 | merchants, poor | 0 | 0 | 1 | 3 | 0 | 0 |
| 0 | merchants, other | 0 | 0 | 1 | 7 | 0 | 0 |
| 0 | Burakumin | 0 | 0 |  |  |  | 0 |
| 0 | burakumin, well-off | 0 | 0 | 1 | 7 | 0 | 0 |
| 0 | burakumin, poor | 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | burakumin, very poor | 0 | 0 | 1 | 0 | 0 | 0 |
| 100 | Farmers | 75 | 15 |  |  |  | 75 |
| 0 | farmer, urban tenant farmer | 0 | 0 | 0 | 0 | 5 | 0 |
| 0 | farmer, temple urban tenant farmer | 0 | 0 | 0 | 0 | 0 | 0 |
| 80 | farmer, rural tenant farmer | 60 | 12 | 0 | 0 | 5 | 60 |
| 5 | farmer, poor freeholder | 3.75 | 0.75 | 0 | 0 | 5 | 3.75 |
| 10 | farmer, freeholder | 7.5 | 1.5 | 0 | 0 | 5 | 7.5 |
| 5 | farmer, wealthy landowner | 3.75 | 0.75 | 0 | 0 | 5 | 3.75 |
| 0 | Samurai | 0 | 0 |  |  |  |  |
| 0 | samurai, merchants | 0 | 0 |  |  |  |  |
| 0 | samurai, courtiers | 0 | 0 |  |  |  |  |
| 0 | samurai, bushi | 0 | 0 |  |  |  |  |
| 0 | samurai, shugenja | 0 | 0 |  |  |  |  |
| 100 | Total | 75 | 15 |  |  |  | 75 |

## Tax Pie

![Annual tax revenue by settlement tier (typical domain, 292,735 koku/year)](tax_pie.svg)

A typical domain's 292,735 koku/year tax base, broken down by where it comes from. The single capital city contributes less than a third of what the 1,296 hamlets contribute in aggregate, despite each hamlet paying only ~75 koku/year - the long tail of small settlements outweighs the head.

## Land Productivity

### Unit Conversions: land area to rice koku

| Unit | Area | Yield (koku) |
| --- | --- | --- |
| Square mile | 1 | 3000 |
| Acre | 1 | 4.69 |
| Mu | 1 | 0.12 |
| Hectare | 1 | 11.58 |

### Per-Family Reference

| Family | Acres | Koku |
| --- | --- | --- |
| 1 | 2 | 9.38 |

### Farm Families by Tier (per Domain)

These are the farming households living inside each settlement type (per the caste percentages elsewhere in this document).  Capital and provincial cities have no in-walls farmers - the fertile land surrounding them is worked by villagers counted under the rural tiers.

| Tier | Settlements (N) | Farm families per settlement | Total farm families |
| --- | --- | --- | --- |
| Capital city | 1 | 0 | 0 |
| Provincial city | 6 | 0 | 0 |
| Town | 36 | 156 | 5,616 |
| Village | 216 | 70 | 15,120 |
| Hamlet | 1,296 | 15 | 19,440 |
| **Total** |  |  | **40,176** |

### Arable Land Allocation (per Domain)

| Type | Total land | Arable area | Arability | Not fallow | Use rate | In acres | Families |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Rice | 3750 | 187.5 | 0.05 | 178.13 | 0.95 | 114000 | 37752 |
| Non-rice | 3750 | 375 | 0.10 | 356.25 | 0.95 | 228000 | 37752 |

Divided evenly: rice ~3.02 acres/family, non-rice ~6.04 acres/family. Yield: rice 15.02 koku/family at a rate of 4.97 koku/acre; non-rice 18.12 koku/family at 3.00 koku/acre.

**Note on labor utilization vs. land utilization**: The 95% use rate above describes short-cycle fallow within actively-cropped land - the rice and non-rice arable shown is in normal year-round productive use.  The empire-wide framing in [l7r.md - Total Rice Production](l7r.md#total-rice-production) treats Rokugan as currently labor-limited: only about 1/3 of total rice-suitable terrain is in active wet-paddy production in any given year, with the remainder split between hillside soybean and azuki fields supporting the paddies, upland rice in multi-year rotation, dryland aftercrops, and labor-fallow land waiting for population to catch up.  The per-domain figures here can be read as describing the actively-worked portion of a domain's rice arable; the latent rice-suitable land that would come under the plow if labor caught up is roughly 2-3x larger.  This is consistent with the canonical empire-wide figure of ~60M koku of rice per year (versus a theoretical maximum closer to 160-180M).

### Rice Productivity by Land Quality

| Land | k/ha | k/mi² | P (share) | Proportional production | k/acre |
| --- | --- | --- | --- | --- | --- |
| High | 20 | 5180 | 0.27 | 1398.60 | 8.00 |
| Medium | 15 | 3885 | 0.17 | 660.45 | 6.00 |
| Med-low | 11.4 | 2952.6 | 0.17 | 501.94 | 4.56 |
| Low | 8 | 2072 | 0.26 | 538.72 | 3.20 |
| Awful | 5.4 | 1398.6 | 0.06 | 83.92 | 2.16 |
| **Total** |  |  |  | **3183.63** |  |
| Average | 12.29 | 3183.63 |  | 3183.63 |  |

### Wheat Productivity by Land Quality

| Land | bush/acre | bush/ha | bush/mi² | koku/ha | koku/mi² | koku/acre |
| --- | --- | --- | --- | --- | --- | --- |
| High | 50 | 123.55 | 32000 | 17.65 | 4571.43 | 7.14 |
| Medium | 40 | 98.84 | 25600 | 14.12 | 3657.14 | 5.71 |
| Med-low | 30 | 74.13 | 19200 | 10.59 | 2742.86 | 4.29 |
| Low | 20 | 49.42 | 12800 | 7.06 | 1828.57 | 2.86 |
| Awful | 10 | 24.71 | 6400 | 3.53 | 914.29 | 1.43 |

Wheat reference: 1 bushel of wheat = 60 lbs = 55 loaves of bread. 1 koku of rice ≈ 7 bushels of wheat.
