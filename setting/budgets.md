# Domain Budgets

Per-tier budget breakdowns for the median domain hierarchy, plus supporting tables.  Generated from `budgets.ods` - formulas are not preserved, only computed values.

## What These Populations Count

The "population" figures in this document mean different things at different tiers, and the differences matter for the math downstream:

- **Hamlet (75) and Village (350)**: counts every person living in that settlement.  These are essentially pure farming communities - a hamlet is just a cluster of farmhouses; a village adds a small number of burakumin (~10%) for ritually-unclean labor.
- **Town (1,200)**: counts the in-and-around population.  Most townies are farmers (~60%) because the working farmland immediately surrounding a county town is included in the town's population.  A "county" is the town plus its surrounding village districts.
- **Provincial city (3,000) and Capital city (12,000)**: counts ONLY the population living within the city walls / on the city's footprint proper.  Cities are nearly always built on top of (or beside) very fertile land, and that land is farmed - but the farmers who work it live in villages and hamlets in the *surrounding county*, not in the city itself.  That is why both city tiers show zero farmers in their caste tables.

The practical upshot: a "capital city" of 12,000 is a city of 12,000 administrators / artisans / soldiers / merchants / servants, ringed by farming villages whose people are counted under the surrounding rural settlement totals.  Likewise the 6 provincial cities of a domain - each ~3,000 inside the walls, surrounded by farming villages counted elsewhere.

## What the Samurai Counts Mean

The samurai populations in the per-tier sub-tables (~1,000 in the capital, ~250 per provincial city, ~15 per county town, for a per-domain total of ~3,000) refer specifically to the **useful working cohort**: samurai past their gempukku and not yet retired.  The total samurai population per domain, including children and retirees living in their family households, is approximately **5,000** (per `l7r.md`).  The 60% useful figure replaces an older 80% estimate; earlier versions of these tables showed ~4,000 working samurai under that older rule.  Children and retirees consume from their family's resources rather than from a separate government allocation, so they do not appear as line items in these budgets.

## Samurai Stipend Convention

The Stipend column in the per-tier Samurai sub-tables shows the **average** annual stipend per working samurai, currently set at **6 koku/year**.  Individual stipends follow the rank-squared rule (`stipend = rank^2`, per `l7r.md`): a Rank 1 bushi receives 1 koku, a Rank 5 county magistrate receives 25 koku, a Rank 7 governor receives 49 koku, a Rank 12 daimyo would nominally receive 144 koku.  The 6-koku average reflects a population dominated by low-rank bushi (most useful samurai are Rank 1-2 serving in military or court positions) with a tail of senior officials in the formal civil service driving the average up.  Earlier versions of these tables used 2.5 koku/year, which reflected the older linear-rank rule (stipend equals rank, not rank-squared).

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

| Place | N | P | Stipend | Food | Housing | Equipment | Other | Population | Payroll | Food (2) | Housing (2) | Equipment (2) | Total Cost |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Capital city | 1 | 1000 | 6 | 3 | 0 | 2 | 0 | 1000 | 6000 | 3000 | 0 | 2000 | 11000 |
| Provincial city | 0 | 250 | 6 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Town | 0 | 0 | 6 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Village | 0 | 0 | 6 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Hamlet | 0 | 0 | 6 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** |  |  |  |  |  |  |  | 1000 | 6000 | 3000 | 0 | 2000 | 11000 |

### Budget

| Category | Expense |
| --- | --- |
| Staff | 1000 |
| Samurai | 11000 |
| Ashigaru | 0 |
| Servants | 240 |
| Supplies | 120 |
| **Total** | 12360 |

### Combined Budgets

| Place | N | Cost | Tax Farming | Total Cost |
| --- | --- | --- | --- | --- |
| Domain | 1 | 12360 | 100000 | 112360 |
| Province | 6 | 2780 | 10000 | 76680 |
| County | 36 | 385 | 1000 | 49860 |
| **Total** |  |  |  | 238900 |

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

| Place | N | P | Stipend | Food | Housing | Equipment | Other | Population | Payroll | Food (2) | Housing (2) | Equipment (2) | Total Cost |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Capital city | 0 | 1000 | 6 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Provincial city | 1 | 250 | 6 | 3 | 0 | 2 | 0 | 250 | 1500 | 750 | 0 | 500 | 2750 |
| Town | 0 | 15 | 6 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Village | 0 | 0 | 6 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Hamlet | 0 | 0 | 6 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** |  |  |  |  |  |  |  | 250 | 1500 | 750 | 0 | 500 | 2750 |

### Budget

| Category | Expense |
| --- | --- |
| Staff | 0 |
| Samurai | 2750 |
| Ashigaru | 0 |
| Servants | 20 |
| Supplies | 10 |
| Tax Farming | 10000 |
| Total | 12780 |
| Remainder | 31861 |

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

| Place | N | P | Stipend | Food | Housing | Equipment | Other | Population | Payroll | Food (2) | Housing (2) | Equipment (2) | Total Cost |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Capital city | 0 | 1000 | 6 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Provincial city | 0 | 250 | 6 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Town | 1 | 15 | 6 | 3 | 0 | 2 | 0 | 15 | 90 | 45 | 0 | 30 | 165 |
| Village | 6 | 0 | 6 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Hamlet | 36 | 0 | 6 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** |  |  |  |  |  |  |  | 15 | 90 | 45 | 0 | 30 | 165 |

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
| Samurai | 165 |
| Ashigaru | 190 |
| Servants | 20 |
| Supplies | 10 |
| Tax Farming | 1000 |
| Total | 1385 |
| Remainder | 5018 |

## Capital City

Total population: **12,000**.

| P | Caste | Population | Families | Property | Business | Land | Total Tax |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20 | Servants | 2400 | 480 |  |  |  | 672 |
| 0 | servants, tutors | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | servants, temple | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | servants, wealthy samurai families | 240 | 48 | 2 | 0 | 0 | 96 |
| 6 | servants, wealthy merchant families | 720 | 144 | 2 | 0 | 0 | 288 |
| 6 | servants, non-wealthy samurai families | 720 | 144 | 1 | 0 | 0 | 144 |
| 4 | servants, non-wealthy merchant families | 480 | 96 | 1 | 0 | 0 | 96 |
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

Total population: **3,000**.

| P | Caste | Population | Families | Property | Business | Land | Total Tax |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20 | Servants | 600 | 120 |  |  |  | 168 |
| 0 | servants, tutors | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | servants, temple | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | servants, wealthy samurai families | 60 | 12 | 2 | 0 | 0 | 24 |
| 6 | servants, wealthy merchant families | 180 | 36 | 2 | 0 | 0 | 72 |
| 6 | Indentured servants, non-wealthy samurai families | 180 | 36 | 1 | 0 | 0 | 36 |
| 4 | Indentured servants, non-wealthy merchant families | 120 | 24 | 1 | 0 | 0 | 24 |
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

Total population: **1,200**.

| P | Caste | Population | Families | Property | Business | Land | Total Tax |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5.5 | Servants | 66 | 13.2 |  |  |  | 18 |
| 0 | servants, tutors | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | servants, temple | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | servants, wealthy samurai families | 12 | 2.4 | 2 | 0 | 0 | 4.8 |
| 1 | servants, wealthy merchant families | 12 | 2.4 | 2 | 0 | 0 | 4.8 |
| 0 | Indentured servants, non-wealthy samurai families | 0 | 0 | 1 | 0 | 0 | 0 |
| 1.5 | Indentured servants, non-wealthy merchant families | 18 | 3.6 | 1 | 0 | 0 | 3.6 |
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

Total in-village population: **350**.

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

Total population: **75**.

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
