# Domain budgets

Per-tier budget breakdowns for the median domain hierarchy, plus supporting tables.

## Contents

- [What these populations count](#what-these-populations-count)
- [What the samurai counts mean](#what-the-samurai-counts-mean)
- [Samurai stipend convention](#samurai-stipend-convention)
- [Samurai rank distribution](#samurai-rank-distribution)
- [The two Empire-wide multipliers](#the-two-empire-wide-multipliers)
- [Domain](#domain)
  - [Capital city](#capital-city)
  - [Province](#province)
  - [Provincial city](#provincial-city)
  - [County](#county)
  - [Town](#town)
  - [Village](#village)
  - [Hamlet](#hamlet)
  - [Populations outside named settlements](#populations-outside-named-settlements)
  - [Discretionary budgets](#discretionary-budgets)
- [Samurai concentration by city size](#samurai-concentration-by-city-size)
  - [The sub-linear scaling principle](#the-sub-linear-scaling-principle)
  - [The by-size schedule](#the-by-size-schedule)
  - [Otosan Uchi: ~40,000 samurai](#otosan-uchi-40000-samurai)
  - [What this means for the median domain](#what-this-means-for-the-median-domain)
- [Ministry budgets](#ministry-budgets)
  - [Domain ministry budgets](#domain-ministry-budgets)
  - [Provincial ministry budgets](#provincial-ministry-budgets)
  - [Cross-cutting project negotiation](#cross-cutting-project-negotiation)
- [Example office-holder budgets](#example-office-holder-budgets)
  - [Magistrate Hida no Reiji Hikai of Seitoyama County](#magistrate-hida-no-reiji-hikai-of-seitoyama-county)
    - [Income](#income)
    - [Mandatory expenses](#mandatory-expenses)
    - [Gift income (in addition to tax revenue)](#gift-income-in-addition-to-tax-revenue)
    - [Discretionary residual](#discretionary-residual)
    - [Hikai's discretionary breakdown](#hikais-discretionary-breakdown)
    - [Summary](#summary)
  - [Governor Hida no Reiji Asuka of Nagahara Province](#governor-hida-no-reiji-asuka-of-nagahara-province)
    - [Income](#income-1)
    - [Mandatory expenses](#mandatory-expenses-1)
    - [Gift income](#gift-income)
    - [Discretionary residual](#discretionary-residual-1)
    - [Asuka's discretionary breakdown](#asukas-discretionary-breakdown)
    - [Summary](#summary-1)
  - [Daimyo Hida no Reiji Isao of the Reiji Domain](#daimyo-hida-no-reiji-isao-of-the-reiji-domain)
    - [Income](#income-2)
    - [Mandatory expenses](#mandatory-expenses-2)
    - [Gift income](#gift-income-1)
    - [Discretionary residual](#discretionary-residual-2)
    - [Isao's discretionary breakdown](#isaos-discretionary-breakdown)
    - [Summary](#summary-2)
- [The Imperial budget](#the-imperial-budget)
  - [Imperial revenue](#imperial-revenue-34-36-million-koku-per-year-at-baseline)
  - [Imperial spending](#imperial-spending-30-31-million-koku-per-year)
  - [Imperial budget scale: historical context](#imperial-budget-scale-historical-context)
  - [Imperial roads and waystations: line-item detail](#imperial-roads-and-waystations-line-item-detail)
  - [Imperial roads: a special case](#imperial-roads-a-special-case)
  - [Imperial legions: line-item detail](#imperial-legions-line-item-detail)
  - [Kaiu Wall direct contributions: line-item detail](#kaiu-wall-direct-contributions-line-item-detail)
  - [Imperial magistrates and their staff: line-item detail](#imperial-magistrates-and-their-staff-line-item-detail)
  - [Imperial savings: the "wealth in favors owed" model](#imperial-savings-the-wealth-in-favors-owed-model)
- [Land productivity](#land-productivity)
  - [Rice and arable-land math](#rice-and-arable-land-math)
    - [Historical units](#historical-units)
    - [Yield reference](#yield-reference)
    - [Historical household-size guidelines](#historical-household-size-guidelines)
    - [Rokugan arable-land extrapolation](#rokugan-arable-land-extrapolation)
    - [Total rice production](#total-rice-production)
    - [Other per-domain derivations](#other-per-domain-derivations)
  - [Unit conversions: land area to rice koku](#unit-conversions-land-area-to-rice-koku)
  - [Per-family reference](#per-family-reference)
  - [Farm families by tier (per domain)](#farm-families-by-tier-per-domain)
  - [Arable land allocation (per domain)](#arable-land-allocation-per-domain)
  - [Rice productivity by land quality](#rice-productivity-by-land-quality)
  - [Wheat productivity by land quality](#wheat-productivity-by-land-quality)

## What these populations count

The "population" figures in this document mean different things at different tiers, and the differences matter for the math downstream (see [`l7r.md` - The Median Domain](l7r.md#the-median-domain) for per-tier population ranges):

- **Hamlet (~50-100, average ~75) and Village (~200-500, average ~350)**: counts every person living in that settlement.  These are pure farming communities - a hamlet is just a cluster of farmhouses, often around a common field; a village is several clusters around multiple large fields plus a slightly larger headman's household.  No burakumin in most rural settlements, as burakumin live in towns and cities where their specialty trades have customers.
- **Town (~900-1,500, average ~1,200)**: counts the in-and-around population.  Most town residents are farmers (~65%) because the working farmland immediately surrounding a county town is included in the town's population.  Border towns tend to be walled, whereas towns which do not need to maintain this level of military preparedness have a much more porous boundary and lack a clear inside-vs-outside boundary.  A "county" is the town plus its surrounding village districts.
- **Provincial city (~2,000-4,000, average ~3,000) and Capital city (~12,000)**: counts ONLY the population living within the city walls / on the city's footprint proper.  Cities are nearly always built on top of (or beside) very fertile land, and that land is farmed - but the farmers who work it live in villages and hamlets in the *surrounding county*, not in the city itself, which will almost always be walled and thus have rigorous demarcation between their urban interior and agricultural exterior.  That is why both city tiers show zero farmers in their caste tables.

The practical result: a capital city of ~12,000 is a city of ~12,000 administrators / artisans / soldiers / merchants / servants / etc, ringed by farming villages whose inhabitants are counted under the surrounding rural settlement totals.  Likewise the ~6 provincial cities of a domain - each ~2,000-4,000 inside the walls, surrounded by farming villages counted in other population totals.

## What the samurai counts mean

The samurai populations in the per-tier sub-tables (~800 in the capital, ~225 per provincial city, ~15 per county town, for an **in-domain** working total of ~2,700) refer specifically to the **useful working cohort serving inside the domain**: samurai past their gempukku and not yet retired.  The domain's *full* working cohort is ~2,900; the other **~200 work in Imperial posts outside the domain** (Imperial Legions, cross-clan yoriki tours, central court roles at Otosan Uchi), paid by the Empire rather than the daimyo - see [Per-domain outflow](#per-domain-outflow-how-many-of-a-daimyos-samurai-are-serving-elsewhere) below.  The total samurai population per domain, including children and retirees living in their family households, is approximately **5,000** (per [`l7r.md` - The Median Domain](l7r.md#the-median-domain)).  Every samurai is counted **once, at their home domain**, so the ~200 serving abroad are *part of* the 5,000, not added on top of it - this is important for understanding the Empire-wide samurai share as being 2% (~5,000 = 2% of ~250,000 = 1/400 of the Empire's ~2 million samurai).

**Two distinct counts, used for two distinct purposes**: city *population* figures (the samurai shown in the [Capital city](#capital-city) caste table) count **all resident samurai - working, pre-gempukku children, and retirees alike** - because all of them physically live in the city and consume its housing, food, and services, and they additionally include a small cohort of **foreign Imperial appointees** stationed in the city (the Imperial Magistrate's office, the tariff-audit yoriki) who reside there without drawing the daimyo's stipend.  *Stipend* figures, by contrast, are paid by the daimyo to his **in-domain working cohort only** (~800 in the capital): **pre-gempukku children and post-retirement samurai draw no government stipend**, samurai serving the Empire abroad are paid by the Empire, and foreign appointees are paid by their own home domains.  This is why the caste tables (resident population) and the Samurai sub-tables (the daimyo's stipend payroll) show different samurai numbers for the same settlement - they are counting different things, not contradicting each other.

## Samurai stipend convention

The Stipend column in the per-tier Samurai sub-tables shows the mean **average** annual stipend per working samurai at each tier.  Individual stipends follow the rank-squared rule (`stipend = rank^2`, per [`l7r.md` - Accordances of Rank](l7r.md#accordances-of-rank)): a Rank 2 bushi receives 4 koku, a Rank 6 Deputy Provincial Minister receives 36 koku, a Rank 10 minister receives 100 koku, etc.

The average varies by tier because the rank distribution does:

- **County town samurai**: ~10 koku average (avg rank ~3).  A typical county town's 15 samurai include 1 magistrate (Rank 5, 25 koku), the magistrate's karo and ~3 squad sergeants (Rank 4, 16 koku each), ~3 squad corporals (Rank 3, 9 koku each), and the remainder mostly Rank 2-3 bushi.
- **Provincial city samurai**: ~15 koku average (avg rank ~3-4).  Provincial cities house the provincial governor (Rank 8), six provincial ministers (Rank 7) and their deputies (Rank 6), mid-rank clerks (Rank 3-5), and rank-and-file bushi assigned to provincial administrative and military duties.
- **Capital city samurai**: ~35 koku average (avg rank ~5-6).  The capital is staffed with the senior cohort - the daimyo (Rank 12, who draws no stipend), councilors (Rank 11), domain ministers (Rank 10) and their deputies (Rank 9), high-rank clerks (Rank 7-8), castle guards and household retainers from the daimyo's elite retinue, and junior officials in training for higher posts.  Low-rank samurai compose a lower proportion of retainers in the capital than in the provinces.

**Stipends are paid out of the broader tax-farming allocation at the tier where the samurai serves** (*not* out of the discretionary "tax-farming cut" that defines the post's value): capital samurai stipends are funded by the daimyo's broader allocation as a separate ~32,000-koku mandatory line (~800 working capital samurai); provincial samurai stipends by the governor's broader allocation as a separate ~4,500-koku mandatory line (~225 per province); county samurai stipends as part of the magistrate's mandatory expenses.  The ~1,000 / ~10,000 / variable "cuts" at the magistrate / governor / daimyo tiers are the discretionary income remaining after all mandatory expenses (tax obligations up, stipends, ministry overhead, kick-ups, etc.) - not the working budget out of which everything is paid.  Cross-tier flow does not happen for stipends as it does for gifts and lineage finances - a provincial samurai is paid by their governor regardless of which lineage the samurai or governor belongs to (see [`l7r.md` - Samurai Lineages](l7r.md#samurai-lineages) for the discussion of how lineage politics and fiscal flow interact).

## Samurai rank distribution

The per-tier average stipends above (capital ~35, province ~15, county ~10 koku) imply a specific distribution of the domain's **in-domain working samurai** across the 15 ranks.  The table below shows that distribution per settlement and aggregated for the whole median domain.  Counts are for **working samurai the daimyo pays** (past gempukku, not yet retired); the ~203 of the domain's working samurai who serve in *Empire-paid* posts elsewhere are not in this stipend table (they appear in [Per-domain outflow](#per-domain-outflow-how-many-of-a-daimyos-samurai-are-serving-elsewhere) below), and the rank a samurai holds is retained into retirement but retirees are not counted here.

| Rank | Stipend (koku) | Per capital (×1) | Per province (×6) | Per county (×36) | Domain total |
| --- | --- | --- | --- | --- | --- |
| 12 | 144 | 1 | - | - | 1 |
| 11 | 121 | 8 | - | - | 8 |
| 10 | 100 | 7 | - | - | 7 |
| 9 | 81 | 25 | - | - | 25 |
| 8 | 64 | 119 | 1 | - | 125 |
| 7 | 49 | 127 | 6 | - | 163 |
| 6 | 36 | 134 | 14 | - | 218 |
| 5 | 25 | 142 | 40 | 1 | 418 |
| 4 | 16 | 103 | 54 | 4 | 571 |
| 3 | 9 | 72 | 59 | 4 | 570 |
| 2 | 4 | 47 | 36 | 4 | 407 |
| 1 | 1 | 15 | 15 | 2 | 177 |
| **Total** | | **800** | **225** | **15** | **2,690** |
| *Avg stipend* | | *~35* | *~15* | *~10* | *~20* |

(The "Domain total" column = 1 capital + 6 provinces + 36 counties, so e.g. Rank 5 = 142 + 6×40 + 36×1 = 418.  Per-settlement stipend totals: capital ~28,400, province ~3,400, county ~143, each matching the Samurai sub-tables below.  The lone Rank-12 daimyo draws no stipend - he lives from the domain's discretionary cut, not a salary - so although he is counted in the capital's 800, the ~28,400 capital total excludes his notional 144 koku (the rank-squared column shows the rule; the total shows what is actually paid).  The capital column otherwise counts everyone the daimyo pays - which includes a handful of samurai physically posted *abroad* as the House's emissaries, explained below - but excludes samurai the *Empire* pays, such as those serving in the Imperial Legions or as Imperial yoriki elsewhere, who are tallied separately in the outflow synthesis.)

**The headline number: roughly 36% of a domain's in-domain working samurai are Rank 5 or above** (~965 of ~2,690); counting the ~203 who serve abroad (who skew low-rank, being mostly rank-and-file legionnaires, but include ~58 at Rank 5+ in central court and command roles), it is ~35% of the full ~2,900 working cohort, or about **21% of all ~5,000 samurai** including children and retirees.  Note how *few* samurai sit at Ranks 10-12 (only ~16 in the whole domain) versus the broad bulge at Ranks 5-8: the very top of the pyramid is genuinely narrow, but "senior-ish" rank (5 through 8) is common.

### Why so many high ranks - and why county magistrate is "the median"

Three features of this distribution surprise newcomers, and all are deliberate:

**Rank tracks birth and post far more than personal power.**  Unlike a level-based fantasy game, a Rokugani samurai's rank is determined chiefly by their **birth family and the post they hold**, not by their accumulated experience (XP).  Rokugan is unusually merit-based by historical standards - it even runs Chinese-style civil-service examinations - but family connections remain a much stronger determinant of rank than raw competence.  The Empire is full of high-XP samurai stalled in middle-management posts because they lack the connections to be handed the big jobs, and many comfortably-ranked samurai owe their position to a well-placed relative.  Thus, rank and XP are only loosely correlated, and a "senior-ish rank" is not the rarity it would be in a system where rank purely tracked ability.

**The very top of the pyramid is narrow, but "rank by association" fills the upper-middle.**  Within a vassal House almost no one holds a *title* above Rank 9: there is one Rank 12 (the daimyo), a small handful of Rank 11 (the ~6 lineage chancellors on the House Chancellery), the six Rank 10 Ministers, and their six Rank 9 Deputy Ministers - and that is nearly the entire in-domain officer corps at Ranks 9-12.  That said, higher Ranks have their numbers bolstered due to [the Doctrine of Three Steps](l7r.md#the-doctrine-of-three-steps):

- **External representation.**  A House posts standing emissaries to the courts above it, each ranked high enough to deal with that court on accordant terms: its representative on the Imperial Chancellery (upper Rank 11), its emissary to the Clan capital (lower Rank 11), its emissary to the Family capital (Rank 10), and its ambassadors to peer vassal Houses (usually Rank 9).  These samurai serve *outside* the domain but remain on the daimyo's payroll - which is why they appear in the capital stipend column above (the ~8 Rank-11 and ~7 Rank-10 figures are the ~6 in-domain chancellors and ~6 in-domain Ministers plus these abroad-posted emissaries), even though they are not physically in the capital.
- **Family by association.**  No samurai may be more than three ranks below their immediate family, so the daimyo's adult children, siblings, and parents are at least Rank 9 (12 minus 3) even when holding no office of their own; the chancellors' close kin are at least Rank 8; and so on down.  This "rank by association" is what populates the broad Rank 8-9 band with samurai who hold no post at all - they have standing because of who they are related to, and the daimyo supports them at the rank their blood commands.

So the **~16 samurai at Ranks 10-12 are almost all genuine office-holders or emissaries**, while the large Rank 5-9 cohort is a mix of mid-level posts, the elite bushi and household of the capital, and the titled-by-blood.  (Samurai a daimyo sends into *Imperial* service - the legions, cross-clan yoriki tours - are paid by the Empire rather than the daimyo, so they are counted in the [outflow synthesis](#per-domain-outflow-how-many-of-a-daimyos-samurai-are-serving-elsewhere) below, not in this stipend table.)

**A capital posting is high-prestige even when the job itself is menial**, which is why the capital is so rank-heavy.  Consider a samurai walking a patrol route in the domain capital: they may hold the **same Rank 5 as a county magistrate**, drawing a 25-koku stipend, while the magistrate rules over a hundred-plus square miles with ~1,000 koku of discretionary income.  The magistrate is vastly wealthier and more powerful - and yet a move "out into the counties" is not unambiguously a promotion.  Some capital samurai would leap at the magistracy; others would politely decline, especially if a different family member could take the post instead and secure the income for the lineage.

Those who decline are not being irrational.  Leaving the capital means leaving the **cultural and social center of the domain** - family, friends, teahouses, theaters, restaurants, drinking houses, and businesses that no county town will ever match - for a remote posting that is, in practical terms, removed from civilized society.  The patroller is *already* fantastically wealthy by the standards of the ~98% of Rokugan that is not samurai; trading "fantastically wealthy and surrounded by civilization" for "obscenely wealthy and isolated" is not an obvious win.  And samurai are socialized **not to display interest in money** - openly chasing wealth is unseemly.  Wealth and power do drive nearly every decision in the society, but ambitious samurai speak of it only obliquely, as a wish "to increase our family's position" or "to fund the schooling of the next generation."  (Even in Yasuki lands, samurai merchants discuss money frankly among themselves but know to be circumspect around outsiders.)  Plenty of samurai are simply not ambitious enough to uproot themselves for a richer-but-lonelier life, especially when they can instead pursue other promotions within the capital (many of which are for similarly menial jobs but nonetheless come with greater prestige).

A **provincial governorship** is a different matter, and is keenly sought after - because a provincial city is *still a city*.  The governor gets the wealth and power of a senior post without surrendering urban life.  The reluctance attaches specifically to the county tier, where the post means genuine rural exile.  This is the structural reason the county magistracy is simultaneously one of the most lucrative posts below the daimyo (per [Provincial ministry budgets](#provincial-ministry-budgets), a magistrate's ~1,000-koku cut beats every provincial minister but Revenue) and, for many of the capital-born samurai eligible for it, a posting they regard as a demotion.

## The two Empire-wide multipliers

Empire-wide aggregations in this document use one of **two different multipliers** depending on what type of quantity is being aggregated.  Both are correct in their respective contexts; choosing the wrong one is the most common source of arithmetic confusion in the budget math.

| Multiplier | Value | Used For |
| --- | --- | --- |
| **Actual-domain multiplier** | **~284** | Quantities that exist exactly once per domain no matter how large it is: capital cities, Imperial Magistrate main offices (one per the Emerald Charter), and the **capital-city tariff** (each domain has a single capital-scale trade hub even when it spans many provinces) |
| **Median domain (MD) multiplier** | **~400** | Everything that scales with a domain's land, population, and provinces. Sub-unit counts and geographic distributions: provincial cities (× 6 per MD = ~2,400), towns (× 36 per MD = ~14,400), villages (× 216 per MD = ~86,400), hamlets (× 1,296 per MD = ~518,400), counties (× 36 per MD = ~14,400), waystations (~12.5 per MD = ~5,000), Imperial road mileage (~125 per MD = ~50,000 miles). **And every size-scaling monetary quantity**: land output and its land tax, the kick-ups levied on land output, provincial-city tariffs, operations budgets, daimyo discretionary cuts, and total tax throughput - because all of these grow with the domain's land and province count, not with the bare number of daimyo |

A **median domain (MD)** is one median domain's worth of the Empire: **~1/400th of both the Empire's land area and its population** (the Empire is ~1.5 million square miles and ~100 million inhabitants; ÷ 400 gives the median domain's ~3,750 square miles and ~250,000 people).  Land and population both divide into ~400 MDs because a median domain holds ~1/400 of each - two measures of the same unit, not two different units (see [`l7r.md` - The Median Domain](l7r.md#the-median-domain)).  **MD** is shorthand for this median-domain-sized unit of land and population; it is deliberately distinct from the **~284 actual domains** (the administrative units headed by daimyo), which average ~1.41 MD apiece - the Empire holds ~400 median-domain-sized units of land but only ~284 actual domains, because the typical actual domain is larger than the median.

The reason there are two multipliers is a structural feature of the Empire's geography and political organization.  The Great Clans and Families together carve the Empire into ~284 administrative domains headed by daimyo.  These domains vary substantially in size: the smallest (frontier vassal-house holdings, lean Phoenix mountain territories) are well under 1 MD; the largest (Clan capitals, major Family seats, Yasuki coastal trade hubs) can be 5-10 MDs or more.  The average actual domain is therefore **~1.41 MDs** (Empire total ÷ 284 = 1.41 MD per actual, in either land or population), but each domain still has exactly **1 capital city**, **1 Imperial magistrate main office**, and **1 capital-scale trade hub**.  So the count of these once-per-domain institutions (× 284) does not match the per-MD aggregation (× 400) used for everything that scales with land and provinces.

The numerical ratio between the two multipliers is exactly **400 / 284 = 1.41 MD per actual domain**, which is the same as saying the average actual domain has 1.41 MDs of land area.

**The tax kick-up to the Emperor is a mixed-basis quantity** - and the most important place to get this right.  A domain's kick-up is overwhelmingly driven by its land output and its provincial-city trade, both of which scale with the number of provinces, so those parts aggregate on the **× 400** basis; only the **capital-city tariff** portion, tied to the single capital trade hub, aggregates on **× 284**.  Multiplying the whole median-domain kick-up by 284 (as if it were a once-per-domain quantity) would undercount the land-and-province-driven bulk of it by the full 1.41 factor.

**Why the 284 carries a tilde**: at the campaign's present moment the figure is *exact* - there are precisely 284 daimyo-headed domains in the Empire right now - but it is written with a tilde throughout this document because it drifts slowly over time.  Vassal domains occasionally conquer one another or split apart under civil infighting, and across the last several centuries the total has stayed within a 275-300 range, and has remained within a narrow 280-290 band for the past hundred years.  That makes it stable enough to anchor Empire-wide aggregations, but it is nearly certain to move within the next decade.  Two illustrative ways it might change:

- A provincial city somewhere in Matsu lands grows wealthy enough to declare its independence from the vassal house it pays taxes to, taking a cluster of neighboring provinces with it, and makes the claim stick after a brief but intense period of fighting - adding a domain to the count.
- A small Hida vassal domain offends a neighboring daimyo so deeply that conquering the whole vassal house is seen as justified.  The combined territory is not large enough to prompt the Crab Clan daimyo or the Emperor to insist that the conquered domain be preserved as a distinct vassal house under new leadership, so it is simply absorbed - removing a domain from the count.

Rokugan has nothing like the constant warfare of the Warring States period, but this sort of low-level conflict is a steady backdrop across the Empire, and the domain count breathes slowly with it.  The ~284 should therefore be read as "284 today, and reliably in the 280s for the forseeable future, but not a fixed constant of nature."

### Why "median domain" means two things in this document

The worked examples in this document (Magistrate Hikai's county, Governor Asuka's province, **Daimyo Isao's Reiji domain**) treat Reiji as a **hybrid "median" domain** that uses whichever multiplier produces clean worked-example numbers:

- **As a median domain by land area (MD)** (everything that scales with land and provinces): Reiji has 6 provincial cities, 36 towns, 216 villages, 1,296 hamlets, ~12 waystations, ~125 miles of Imperial road - plus its land output, land tax, the kick-ups on land output, provincial-city tariffs, operations, and ~58,000-koku typical-median discretionary daimyo cut (the Reiji's own Hida-vassal cut is the higher ~71,000).  Multiply each of these by **~400 MD** to reach Empire-wide totals.
- **As a "median actual domain"** (once-per-domain institutions): Reiji has 1 capital city, 1 Imperial magistrate main office, and 1 capital-scale trade hub - whose capital-city tariff is the single tax-flow that aggregates this way.  Multiply each of these by **~284 actual domains** to reach Empire-wide totals.

The hybrid framing is intentional and lets worked examples use clean integer counts (6 provincial cities reads more naturally than the strict per-actual-domain 8.45), while still producing correct Empire-wide aggregations as long as the right multiplier is applied to each line.

### The most common mistake

The most common arithmetic mistake is **multiplying a sub-unit count by 284 instead of 400** (e.g., "6 provincial cities × 284 = 1,704" - this undercounts the actual ~2,400 provincial cities Empire-wide because it does not account for larger actual domains having proportionally more provincial cities than the median).  The converse mistake - multiplying a whole-domain quantity by 400 - overshoots Empire-wide totals (e.g., "1 capital city × 400 = 400" overcounts the actual ~284 capital cities Empire-wide).

**The diagnostic question** to ask before multiplying any per-Reiji quantity by an Empire-wide divisor: *Does this quantity scale with the number of daimyo (× 284) or with the land area (× 400)?*  Whole-domain political and administrative quantities use 284; geographic distributions and sub-unit counts use 400.

## Domain

This section breaks down the total population for the median domain at a high level, and the following subsections each correspond to different administrative areas and population centers.

| Place | N | Pop each | Total Pop |
| --- | --- | --- | --- |
| Capital city | 1 | 12360 | 12360 |
| Provincial city | 6 | 3000 | 18000 |
| Town | 36 | 1190 | 42840 |
| Village | 216 | 350 | 75600 |
| Hamlet | 1296 | 75 | 97200 |
| **Named-settlement total** |  |  | 246000 |

### Capital city

Total population: **~12,000**.

| P | Caste | Population | Families | Property | Business | Land | Total Tax |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20 | Servants | 2400 | 480 |  |  |  | 672 |
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
| 10 | Samurai (domestic) | 1200 | 240 |  |  |  | 0 |
| 1 | samurai, merchants | 120 | 24 | 0 | 0 | 0 | 0 |
| 1 | samurai, courtiers | 120 | 24 | 0 | 0 | 0 | 0 |
| 8 | samurai, bushi | 960 | 192 | 0 | 0 | 0 | 0 |
| 100 | Total | 12000 | 2400 |  |  |  | 24888 |
| +3 | samurai, relocated county families (non-working) | ~360 | ~72 | 0 | 0 | 0 | 0 |
| +0.4 | samurai, foreign (Imperial appointees) | ~45 | ~12 | 0 | 0 | 0 | 0 |

**Samurai composition note**: the capital's settled-population breakdown (~12,000) shows ~1,200 domestic samurai (10%), but its true resident samurai count is higher because the capital is the domain's schooling-and-retirement magnet.  Adding the **~360 non-working samurai whose families relocate here from the domain's county towns** (children sent to the capital's schools, elders retiring near the daimyo's court) brings the domestic total to **~1,560**, and the ~1,200 base itself is ~800 working (the cohort the daimyo pays, per [Samurai rank distribution](#samurai-rank-distribution)) plus ~400 non-working (children, retirees, and the families of the ~150 capital-born samurai serving the Empire abroad).  So the capital's resident domestic samurai run **~1,560 (~13% of its ~12,360 physical population)** - the highest samurai concentration of any settlement tier, exactly as a daimyo's castle-town seat should be (provincial cities sit at ~10%, county towns at ~1.7%, and the great mega-cities fall back toward ~4-6% as commerce dilutes them).  The working share is correspondingly low (~800 of ~1,560 ≈ 51%) because so many of the residents are dependents.  The **~45 foreign samurai** are the Imperial Magistrate's office (the Imperial magistrate, karo, ~5 household, ~25 office yoriki, plus ~12 accompanying family) - resident but paid by the Empire and their own home domains, not by Daimyo Isao.  Both the relocated and foreign cohorts are listed *additional* to the 12,000-person settled-population breakdown; with them the capital physically holds ~12,400 people.

### Province

| Place | N | Pop each | Total Pop |
| --- | --- | --- | --- |
| Provincial city | 1 | 3000 | 3000 |
| Town | 6 | 1190 | 7140 |
| Village | 36 | 350 | 12600 |
| Hamlet | 216 | 75 | 16200 |
| **Named-settlement total** |  |  | 38940 |

As with the [Domain population table](#domain) above, this sums only named settlements; the province's full population is slightly higher (~39,600), the small remainder being the same off-the-books peasantry explained under [Population outside named settlements](#populations-outside-named-settlements).

### Provincial city

Total population: **~2,000-4,000, average ~3,000**.

| P | Caste | Population | Families | Property | Business | Land | Total Tax |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 20 | Servants | 600 | 120 |  |  |  | 168 |
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
| 10 | Samurai (domestic) | 300 | 60 |  |  |  |  |
| 1 | samurai, merchants | 30 | 6 | 0 | 0 | 0 | 0 |
| 1 | samurai, courtiers | 30 | 6 | 0 | 0 | 0 | 0 |
| 8 | samurai, bushi | 240 | 48 | 0 | 0 | 0 | 0 |
| 100 | Total | 3000 | 600 |  |  |  | 6222 |
| +0.2 | samurai, foreign (Imperial appointees) | ~5 | ~1 | 0 | 0 | 0 | 0 |

**Samurai composition note**: the 10% domestic samurai (~300) break down as ~225 working (the cohort the governor pays) plus ~75 non-working (children, retirees, and resident families of the ~25 provincial-born samurai serving the Empire abroad).  The **~5 foreign samurai** are the small Imperial yoriki sub-station that audits tariff collection at the provincial city's gate - resident but Empire-paid, listed additional to the 3,000-person settled-population breakdown.

### County

| Place | N | Pop each | Total Pop |
| --- | --- | --- | --- |
| Town | 1 | 1190 | 1190 |
| Village | 6 | 350 | 2100 |
| Hamlet | 36 | 75 | 2700 |
| **Named-settlement total** |  |  | 5990 |

As with the [Domain population table](#domain) above, this sums only named settlements; the county's full population is slightly higher (~6,100), the small remainder being the same off-the-books peasantry explained under [Population outside named settlements](#populations-outside-named-settlements).

### Town

Total population: **~900-1,500, average ~1,200**.

| P | Caste | Population | Families | Property | Business | Land | Total Tax |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5.5 | Servants | 66 | 13.2 |  |  |  | 18 |
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
| 65 | Farmers | 780 | 156 |  |  |  | 780 |
| 55 | farmer, rural tenant farmer | 660 | 132 | 0 | 0 | 5 | 660 |
| 2.5 | farmer, poor freeholder | 30 | 6 | 0 | 0 | 5 | 30 |
| 5 | farmer, freeholder | 60 | 12 | 0 | 0 | 5 | 60 |
| 2.5 | farmer, wealthy landowner | 30 | 6 | 0 | 0 | 5 | 30 |
| 1.7 | Samurai | 20 | 4 |  |  |  |  |
| 1.7 | samurai, bushi | 20 | 4 |  |  |  |  |
| 100 | Total | 1190 | 238 |  |  |  | 1603.2 |

**Samurai composition note**: a county town holds only ~20 resident samurai, of which ~15 are working (the magistrate and their staff - a full platoon) and only ~5 are non-working.  This is a far higher working share (~75%) than any city, because **county samurai families largely do not live in the remote county seat**; children are sent up-tier to the provincial city or domain capital for schooling, and elders retire to those places, so the dependents who would otherwise pad the count reside in those larger centers (see the [Capital city](#capital-city) note).  The ~10 family members per town who relocate up account for the ~360-per-domain shift that lifts the capital's resident samurai to ~13%.  The town's tax base (~1,603) is unchanged - samurai pay no property taxes on their homes, so their relocation does not move it.

### Village

Total in-village population: **~200-500, average ~350**.

| P | Caste | Population | Families | Property | Business | Land | Total Tax |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 100 | Farmers | 350 | 70 |  |  |  | 350 |
| 80 | farmer, rural tenant farmer | 280 | 56 | 0 | 0 | 5 | 280 |
| 5 | farmer, poor freeholder | 17.5 | 3.5 | 0 | 0 | 5 | 17.5 |
| 10 | farmer, freeholder | 35 | 7 | 0 | 0 | 5 | 35 |
| 5 | farmer, wealthy landowner | 17.5 | 3.5 | 0 | 0 | 5 | 17.5 |
| 100 | Total | 350 | 70 |  |  |  | 350 |

### Hamlet

Total population: **~50-100, average ~75**.

| P | Caste | Population | Families | Property | Business | Land | Total Tax |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 100 | Farmers | 75 | 15 |  |  |  | 75 |
| 80 | farmer, rural tenant farmer | 60 | 12 | 0 | 0 | 5 | 60 |
| 5 | farmer, poor freeholder | 3.75 | 0.75 | 0 | 0 | 5 | 3.75 |
| 10 | farmer, freeholder | 7.5 | 1.5 | 0 | 0 | 5 | 7.5 |
| 5 | farmer, wealthy landowner | 3.75 | 0.75 | 0 | 0 | 5 | 3.75 |
| 100 | Total | 75 | 15 |  |  |  | 75 |

### Populations outside named settlements

**Named-settlement total vs. the full domain**: the sections above count only the *named settlements* (capital, provincial cities, county towns, villages, hamlets), which come to ~246,000.  The domain's full **real** population is **~250,000** (1/400 of the Empire's 100 million); the ~4,000 difference (~1.6% of the domain) is **peasants living outside any named settlement AND outside the magistrate's notice** - households on plots too marginal, too remote, or too newly-cleared to have been entered on the tax rolls at all.  So ~246,000 counted-and-settled inhabitants plus ~4,000 off-the-books peasants reconciles to the ~250,000, and the property 250,000 = 100,000,000 ÷ 400 holds for the domain as a whole.  (The 250,000 is a real headcount, not a registered figure - the off-the-books ~1.6% is included in it; it is simply invisible to the domain's own administration.)

**Why the remainder is peasants and not samurai**: it is purely peasants because of an accounting convention.  A small isolated farm that is *taxed at all* is tallied under whichever village or hamlet district lies nearest, even when the holding is so remote that it is really its own separate thing.  Its output, and the people it supports, are folded into that district's total as a bookkeeping convenience.  Samurai country estates are a separate matter; the ~560 samurai who live on country estates rather than in the cities and towns - the L7R analogue of the rural *gōshi* who remained on the land after the separation of warrior and peasant (*heinō bunri*) concentrated most samurai into castle towns - together with their households and the tenant farmers who work their land, are already inside the ~246,000 (tallied into the surrounding village districts) and already inside the domain's ~5,000 samurai (see [What the samurai counts mean](#what-the-samurai-counts-mean)).  What is left in the ~1.6% is only the genuinely *untaxed* population: peasants the domain administration has never registered.

**Why ~1.6% fits historical norms**: a small off-the-books remainder of this size is well within historical norms, and 1.6% is deliberately at the *low* end of the plausible band because Rokugan is portrayed as an unusually well-administered state.  Two historical patterns set the bounds.  First, **nucleated settlement**: Tokugawa Japan was organized almost entirely around the *mura* (the village as a registered corporate unit), and the wet-rice cores of Ming and Qing China were similar - paddy cultivation rewards clustered labor, so nearly everyone belonged to a named village even when their fields were scattered, and genuinely isolated farmsteads were the exception rather than the rule.  This is why the *taxed* dispersed population is small enough to fold into the district totals rather than forming a population of its own.  Second, **under-registration and non-state space**: every premodern register undercounted.  Tokugawa enumerations ran well below the true population; hidden fields (*kakushida*) concealed from the cadastral surveyors were a chronic problem; Qing baojia coverage in practice could fall far below its nominal 100%; and James C. Scott's "non-state spaces" (uplands, marshes, forests) sheltered people the state could not easily count - though those usually lay *beyond* a polity's effective reach rather than deep inside a well-run core.  A poorly-administered or frontier domain might carry a genuinely uncounted fringe of 5-10% or more; Rokugan, being unusually well-run, sits near the floor at ~1.6%.  That is small enough to be the exception rather than the rule, but nonzero - which is the point: it leaves just enough room for player characters to stumble on a cluster of non-state peasants the local magistrate has never heard of, and for that discovery to register, in-setting, as the genuine irregularity it is.

The capital's ~12,360 is its settled ~12,000 plus the ~360 non-working samurai whose families have relocated there from the domain's county towns (see the [Town](#town) and [Capital city](#capital-city) caste tables); the county towns are correspondingly lighter (~1,190 each, down from ~1,200).  Total domain population and the entire tax base are unchanged - this is a redistribution of samurai *within* the domain, and samurai pay no property taxes on their homes, so no settlement's tax base moves.

### Discretionary budgets

Before diving into the much more detailed budgets below, here is a rough summary of the annual "discretionary" funds available to the people in charge at each of these levels:

| Tier | Per domain | Discretionary funds |
| --- | --- | --- |
| Daimyo | 1 | ~64,000 |
| Provincial governor | 6 | ~11,000 |
| County magistrate | 36 | ~1,100 |

Some notes about these figures:

- **Costs** the discretionary income at each level is what is left over after the cost of samurai compensation, ministry overhead (where applicable), servants, supplies, and miscellaneous operations.  A full breakdown of these costs for each level can be found in the corresponding section below. 
- **Discretionary funds** is the office-holder's income from tax farming, gifts, and (for the daimyo) tariffs, minus costs - slightly above the bare tax-farming cut.  The underlying cut is the figure that defines each post's value: the county magistrate's ~1,000 is a fairly reliable rule of thumb which only varies for counties with poor farmland or a noteworthy local industry; a provincial governor's ~10,000 koku has slightly more variance, especially among provinces with e.g. rich natural resources or a smaller number of counties; and the domain daimyo's ~64,000 is only a rough average, with actual cuts ranging from ~35,000 (poor frontier domains) to ~115,000+ (wealthy domain capitals) and structural factors like ruling-Family-vassal status (~71,000 for the Reiji example documented below) creating additional variation.  A portion of the cut is a **hidden Imperial subsidy to the clans**: because the Empire pays the ~203 of each domain's working samurai who serve in Imperial posts (legions, cross-clan yoriki, central court), the daimyo's stipend outlay is ~7,200 lower than his in-domain headcount alone would imply, and that saving flows to his discretionary cut (documented in the [Imperial legions](#imperial-legions-line-item-detail) section).
- **Kick-ups** are not mentioned here specifically as this table does not include or break down costs, but it is worth mentioning the funds which flow out of the domain to Family, Clan, and Imperial recipients per the structural kick-up chain (see [The Ministry of Revenue](l7r.md#the-ministry-of-revenue) for the rate structure).  In particular, it is important to understand that only the domain tier pays kick-ups directly; counties and provinces pass their tax obligations upward through the cascade rather than paying kick-ups themselves.  The ~114,800 kick-up at the domain tier is composed of ~60,300 (10% of land output, against the ~602,640-koku assessed *kokudaka* per median domain - the obligation base; actual gross output is higher, with the surplus kept by farmers, per the assessed-*kokudaka* note under [Land productivity](#land-productivity)) + ~54,500 (10% of imported-goods trade volume, against ~545,000 koku of median-domain imported-goods sales - itself ~312,000 in provincial-city trade plus ~233,000 at the capital gate), reflecting the standard non-Hida-vassal rates.  Aggregating this kick-up Empire-wide is **mixed-basis**: the land-output and provincial-tariff portions scale × 400, the capital-tariff portion × 284 (see [The two Empire-wide multipliers](#the-two-empire-wide-multipliers)).  Coastal trade-hub domains run substantially higher tariff volumes and pull the true Empire-wide *mean* above this figure, but these per-domain aggregations use the *median* domain throughout (the median is the unit used throughout this document; see [The two Empire-wide multipliers](#the-two-empire-wide-multipliers)).
- **Empire-wide totals**: across the ~284 actual domains, total throughput is ~168 million koku/year, of which ~43 million flows out as kick-ups (~21.6M to the Imperial center and ~21.6M to Family and Clan daimyo) and the remaining ~124 million stays within the domains (operations plus discretionary income at every tier).  Most of this scales × 400 with land and provinces; only the capital-tariff portion of the kick-up scales × 284 (see [The two Empire-wide multipliers](#the-two-empire-wide-multipliers)).

## Samurai concentration by city size

The per-tier caste tables in [`l7r.md` - Demographics](l7r.md#demographics) establish that samurai are ~2% of the Empire's total population (~5,000 per median domain).  But this 2% is not distributed evenly across settlement types, and the way it varies with city size is structurally important both for understanding the Empire and for computing the samurai population of Otosan Uchi.

### The sub-linear scaling principle

**Capital cities of large premodern empires consistently have a *lower* elite percentage than their provincial counterparts, because the absolute size of the administrative cohort scales sub-linearly with city size while the commercial and service population scales roughly linearly.**  A city twice as large does not need twice as many magistrates, ministers, and clerks - administrative need grows more slowly than population - but it does attract roughly twice as many merchants, laborers, servants, and artisans to serve that larger population.  The elite fraction therefore shrinks as the city grows, even as the absolute number of elites rises.

This pattern is robust across analogous premodern capitals:

| Capital | Era | Population | Elite class | Elite % |
| --- | --- | --- | --- | --- |
| Tang Chang'an | ~700 CE | ~1 million | scholar-officials + palace establishment | ~2-3% |
| Northern Song Kaifeng | ~1100 | ~1 million | scholar-officials | ~1-3% |
| Heian-kyo (Kyoto) at peak | ~1000 | ~150,000 | kuge (court nobility) | ~1-3% |
| Ming Beijing | ~1500 | ~700,000 | officials + eunuchs + Imperial Guard | ~5-10% |
| Joseon Hanyang (Seoul) | ~1700 | ~200,000 | yangban (scholar-gentry) | ~5-15% |
| Qing Beijing | ~1750 | ~700,000 | bannermen (hereditary military caste) | ~50% |
| Tokugawa Edo | ~1850 | ~1 million | samurai | ~60% |

Tokugawa Edo is the dramatic outlier, and the reason is instructive: its ~60% samurai concentration is a direct consequence of *sankin kotai* (the alternate-attendance system), which forced every daimyo to maintain a massive permanent Edo establishment - family, retainers, and guards numbering in the thousands - with the daimyo themselves resident half of every year.  Without that extreme forced-residence mechanism, Edo would have looked far more like the ~5-10% range of the other military-aristocratic capitals.  The "natural" range for a million-population East Asian capital with a strong elite-military presence but no *sankin-kotai*-style concentration mechanism is roughly **3-7%**.

Rokugan deliberately does **not** replicate the *sankin kotai* extreme.  Daimyo maintain embassies at Otosan Uchi (hostage family members, business agents, political representatives) and the Imperial Families concentrate there, but daimyo are not required to reside in the capital, and there is no system forcing thousands of retainers per domain into permanent capital residence.  Otosan Uchi therefore lands in the lower part of the natural band.

### The by-size schedule

Combining the sub-linear principle with the caste tables produces the following schedule of samurai concentration by settlement size, using **total resident samurai** as the basis (counting working samurai, pre-gempukku children, and retirees alike, consistent with the ~2% Empire-wide and ~10% median-capital population figures in the caste tables).  The working cohort that actually draws stipends is a subset of these totals - roughly the ~60% domain-wide working ratio, running somewhat higher inside cities where senior officials and their smaller households cluster, per [What the samurai counts mean](#what-the-samurai-counts-mean):

| Settlement | Population | Samurai % | Resident samurai (approx) |
| --- | --- | --- | --- |
| Hamlet | ~75 | 0% | 0 |
| Village | ~350 | 0% | 0 |
| County town | ~1,200 | ~1.7% | ~20 |
| Provincial city | ~3,000 | ~10% | ~300 |
| Median domain capital | ~12,400 | ~13% | ~1,560 |
| Mid-size capital | ~30,000-90,000 | ~8-9% | ~2,500-7,500 |
| Large capital (e.g. Kyuden Daidoji ~200K) | ~200,000 | ~6% | ~12,000 |
| Very large city (e.g. Toshi Ranbo ~300K) | ~300,000 | ~5% | ~15,000 |
| Largest non-capital city (Ryoko Owari ~500K) | ~500,000 | ~4.5% | ~22,500 |
| **Otosan Uchi** | **~1,000,000** | **~4%** | **~40,000** |

The schedule captures the key shape: samurai concentration is near-zero in the countryside, rises to a **peak of ~13% at the median domain capital** - the daimyo's castle-town seat, which concentrates not only the senior administrative cohort but the schooling-and-retirement households of samurai families from across the domain (including the county towns, which run correspondingly light at ~1.7%) - and then **declines steadily** for larger cities as commercial and service populations outgrow the samurai cohort.  Provincial cities sit a step below the capital at ~10% (they are administrative centers but not the family magnet the capital is); larger clan and Family capitals, despite far more samurai in absolute terms, fall back toward ~6-9% as their sheer commercial size dilutes the concentration, all the way down to Otosan Uchi at ~4%.  (This ~13% capital peak is a deliberately restrained echo of the historical castle town, where the daimyo's seat ran 30-60% samurai; Rokugan's capitals are far more commercial.)

### Otosan Uchi: ~40,000 samurai

At 4% of its ~1 million inhabitants, Otosan Uchi has approximately **40,000 resident samurai** - about twice the ~2% samurai share of the Empire's population as a whole.  That the largest, most central city in the Empire concentrates samurai at only twice the baseline rate (rather than 10x or 30x) is a deliberate and revealing feature of the setting: even at the very heart of samurai power, samurai remain a small minority of the people doing the actual work of the city.  (See the thematic discussion in [`l7r.md` - Demographics](l7r.md#demographics) on what this 2%-everywhere reality means for what samurai can and cannot know about their own Empire.)

The ~40,000 break down approximately as follows:

| Otosan Uchi resident samurai cohort | Approx count | Notes |
| --- | --- | --- |
| Imperial Families resident at the capital | ~11,000 | More than half of the Hantei are based at Otosan Uchi, along with substantial fractions of the Seppun, Otomo, and Miya (the remainder administer the Imperial Families' own 9 domains and serve as Imperial appointees scattered across the Empire).  Includes family members, household, and the Imperial-Family officials staffing the inner palace and senior central posts |
| Clan-supplied samurai staffing Imperial central functions | ~13,000 | The resident workforce of the 6 Imperial Ministries' central operations, the Otosan Uchi local government (administering ~1 million inhabitants), the Imperial Household guard, the Emerald Champion's central staff, and the central judicial machinery.  Imperial-paid; drawn from across the clans (part of the ~86,000 clan-supplied Imperial appointee pool discussed below) |
| Daimyo embassies (one establishment per actual domain) | ~13,000 | Each of the ~284 actual domains maintains a permanent Otosan Uchi establishment: hostage family members (a structural feature of Imperial politics), business agents pursuing capital commerce, and political representatives cultivating alliances and Imperial favor.  Scales with domain tier: Clan capitals ~120 each (× 7 = ~840), Family capitals ~90 each (× 25 = ~2,250), vassal houses ~38 each (× 252 = ~9,600).  Clan-paid, not Imperial posts |
| Private samurai | ~3,000 | Independent agents, students attending capital institutions, ronin seeking patronage, and bushi retained by the great merchant houses |
| **Total** | **~40,000** | ~4% of the ~1 million population |

The district-governor system documented in the Otosan Uchi material (in which certain favored houses administer entire city districts) layers additional structure onto the clan-supplied and embassy cohorts, but does not change the aggregate ~40,000 figure and does not affect the median domain, so it is set aside here.

### What this means for the median domain

Running the Otosan Uchi population back through the median domain: if ~40,000 of the Empire's ~2,000,000 total samurai (2% of ~100 million inhabitants) reside at Otosan Uchi, then **~2% of all samurai live in the capital at any given time**.  Applied to a median domain's ~5,000 total samurai, that predicts **~100 of a median domain's samurai are at Otosan Uchi** at any moment.

For the Reiji-style vassal-house domain, this ~100 breaks down as:

| Reiji samurai at Otosan Uchi | Approx count | Status |
| --- | --- | --- |
| Reiji's permanent embassy (hostage family + business/political agents) | ~40 | Clan-paid representation, NOT an Imperial post |
| Reiji samurai in clan-supplied Imperial central posts | ~50 | Imperial-paid; a subset of Reiji's ~203 outgoing Imperial appointees (see [Total Imperial appointee samurai](#total-imperial-appointee-samurai-empire-wide-synthesis)) |
| Private Reiji samurai (agents, students, etc.) | ~10 | Private; not on any payroll |
| **Total Reiji samurai in Otosan Uchi** | **~100** | ~2% of Reiji's ~5,000 total samurai |

This is a small but politically consequential cohort.  Note that vassal houses like Reiji sit slightly *below* the per-clan average for Otosan Uchi presence: the Great Clan and Family capitals maintain far larger embassies (~120 and ~90 vs Reiji's ~40) and supply more senior central officials, so they pull the per-clan fraction up above 2% while vassal houses sit a touch below it.  Domains geographically closer to the capital also tend to maintain larger and more active Otosan Uchi establishments than distant frontier domains, though the hostage-politics floor applies to every domain regardless of distance.

## Ministry budgets

**Note on the term "tax farming"**: This document uses "tax farming" in its loose modern English sense - the structural pattern of officials keeping a share of taxes they collect as their compensation.  Strictly, tax farming refers to the Roman *publicani* model where collection rights were auctioned to private contractors who paid the state a fixed sum upfront and pocketed whatever they could extract above it.  The Rokugan system isn't that: Rokugani officials are appointed through the civil-service examination and chancellery selection process, not auctioned, and the size of each office's cut is fixed by tradition and centralized land assessments rather than competitive bidding.  Structurally, the Rokugan arrangement is closer to the Tokugawa *chigyō* (fief grant) or the medieval European prebend (office-attached income), where the official is a state official whose compensation is an attached tax allocation.  "Tax farming" is used here because it conveys the right intuition (the office-holder profits from extraction efficiency) and is the established casual English usage for this broader pattern, including in modern descriptions of the Mughal *jagir* and Ottoman *timar* systems which were similarly appointment-based rather than auctioned.

The tax-farming cuts (typically ~58,000 for the daimyo, ~10,000 per provincial governor, and ~1,000 per county magistrate) are **the office-holder's discretionary income** - what remains after all mandatory expenses (tax obligations up to the next tier, kick-ups to Clan/Family/Imperial, samurai stipends, ministry overhead budgets, manor and office operations, etc).

The breakdowns below show the typical allocation at each tier.  Numbers are approximate and vary by domain, province, and the personalities and politics of the office-holders.  The **informal income** column shows the office-holder's effective personal take above their formal stipend, calculated as a ~10% skim on the ministry budget they administer ("a tithe", a customary rate built into many Rokugani fiscal formalities and occasionally formalized, e.g. the 10-koku Imperial registration fee on a 100-koku bounty).  Strictly speaking, this is not built into the budget, and in fact office holders are expected to pay all expenses related to their duties even if those expenses exceed their income.  As with tax farming, the presumption is that forward-thinking appointees will save their money in years of plenty so that they can spend their savings and/or make use of lineage reserves as needed in lean years.  The 10% figure is thus only a loose average, and corrupt officials may extract more, while scrupulous samurai might consistently draw on family connections to make up chronic shortfalls without ever personally enriching themselves.

### Domain ministry budgets

A typical domain generates ~256,000 koku/year in tax throughput at the daimyo's tier, from the six provincial governors' tax obligations passed up, the capital city's direct tax base and import tariffs, and domain-level revenue from mining royalties, large cross-province sake export licenses, craft monopolies, and special assessments.  Of this:
* ~60,300 koku flows up to the Clan daimyo, Family daimyo, and Imperial superiors as the 10% land-output kick-ups (see [The Imperial budget](#the-imperial-budget) below)
* ~54,500 flows up to those same superiors as the 10% tariff kick-ups on the domain's typical ~545,000 koku of imported-goods sales volume (per the "Yasuki Taka" rate structure documented in [l7r.md - The Ministry of Revenue](l7r.md#the-ministry-of-revenue))
* ~32,000 funds the ~800 working capital samurai the daimyo pays (stipends + food + equipment - the other ~203 of the domain's working samurai serve in Empire-paid posts elsewhere)
* ~50,000 funds the six domain ministries' **overhead budgets** (materials, contracts, ministry-specific staff, ministers' formal stipends and customary skims)
* ~1,400 covers minor domain servants, supplies, and the daimyo's direct administrative staff.
* The remaining ~58,000 koku is the **daimyo's discretionary funds** - the daimyo's "tax-farming cut," significantly higher than a provincial governor's ~10,000 and a county magistrate's ~1,000 but not by a fixed ratio.

**Note**: as at the provincial tier, the ministry budgets shown here are **overhead only** - they do NOT include capital samurai stipends, which are funded as a separate ~32,000-koku line from the daimyo's overall budget.  The Ministry of Retainers *administers* stipend disbursement (rice/coin denomination decisions, rank-squared calculations, payment-day logistics) but the funds themselves flow from the daimyo's tax-farming allocation, not from the Retainers ministry's ~3,000-koku overhead budget.  Only working samurai past their gempukku and not yet retired receive stipends.

Unlike the magistrate's ~1,000 and governor's ~10,000 cuts, the daimyo's discretionary cut varies widely with domain wealth and structural factors.  Wealthy maritime trade domains or large Clan-capital domains can run substantially higher (large trade volume, lower per-domain kick-up rates if structurally consolidated); frontier or war-recovering domains run lower (smaller trade base, additional military pressure on the budget).  Hida vassal houses like the Reiji stop levying the absorbed 2% Family layer on both land and tariffs.  On land the daimyo keeps it outright (~12,000 koku/year), which lands the cut above the typical median; on tariffs the absorbed 2% (~10,900 koku/year) can be kept too; most ruling-Family vassal houses hold their gate tariff at the standard ~15% and pocket the extra 2%, but a domain facing competitive pressure from low-tariff neighbors (as the Reiji do from three nearby Minor Clans) instead passes that 2% to merchants as a lower rate, taking higher throughput rather than a bigger cut.  The ~58,000-koku figure for a typical domain represents a rough median, not a fixed expectation - and specifically it is the median *non-ruling-Family* vassal house, which pays the full 10% kick-up.  That is the modal domain, because each Great Clan has only one ruling Family but several non-ruling ones (the Matsu, Ikoma, and Kitsu of the Lion; the Hiruma, Kaiu, Kuni, and Yasuki of the Crab; etc), so most vassal houses sit under a non-ruling Family and pay the full rate; the ruling-Family vassal houses that absorb the 2% layer (like the Reiji) are the higher-cut minority.  Actual daimyo discretionary across the empire ranges from ~35,000 (poor frontier domains) to ~115,000+ (wealthy Clan capitals).

The ~50,000-koku ministry overhead allocation breaks down across the six ministries, with effective income for each Rank 10 minister:

| Ministry | Budget | Minister's stipend | Informal income (~10% skim + throughput where applicable) | Gifts | Minister's effective income |
| --- | --- | --- | --- | --- | --- |
| Works | ~30,000 | 100 | ~3,000 | ~0 | **~3,100** |
| War | ~7,000 | 100 | ~700 | ~1,500 | **~2,300** |
| Rites | ~6,000 | 100 | ~600 | ~200 | **~900** |
| Justice | ~3,000 | 100 | ~300 (formal) | ~200 (virtuous) to ~2,700+ (corrupt, incl. fines) | **~600 to ~3,000+** |
| Retainers | ~3,000 | 100 | ~300 (formal) + ~1,600 (rice/coin arbitrage on capital stipend throughput of ~28,000) | ~400 | **~2,400** |
| Revenue | ~1,000 | 100 | ~100 (formal) + ~2,000 (tax-collection fees on throughput) | ~100 | **~2,300** |
| **Total** | **~50,000** |  |  |  |  |

Notice the **structural floor for the Minister of Justice is the lowest** of the six (~600 koku effective income at the modest end), but the **ceiling is uncapped**.  Ministers of Justice in wealthy domains can accept significant "gifts" from those under their judicial authority and assess fines whose amounts they set within wide precedential limits.  A virtuous Minister of Justice lives modestly on ~600 (the formal income plus the modest, customary gifts even an honest official accepts in this gift-centered society); a corrupt one in a wealthy domain can exceed even the Minister of Works; both extremes are well-attested in Rokugan.

The Minister of War is the other gift-sensitive post.  Its overhead budget is small, but it draws substantial gifts - from underlings angling for promotion and from outsiders seeking the appointments the ministry hands out beyond the chancellery's reach - which lift its effective income (~2,300) well above what its ~7,000-koku budget alone would yield.  Works, Rites, and Revenue sit closer to their budget-determined income: gifts to Works or Revenue in particular are structurally discouraged, because favoring a gift-giver (a padded contract, a soft assessment) comes out of the minister's own overhead budget or out of the daimyo's revenue rather than being a free favor to grant - the same dynamic that holds magistrate and governor gift income down.

### Provincial ministry budgets

Each typical province generates ~44,000 koku/year in tax throughput from county tax kick-ups, the provincial city's direct tax base, and city-gate tariffs.  Of this:
* ~24,500 koku flows up to the daimyo as the province's tax obligation (composed of ~16,200 land-tax kick-up + ~7,800 tariff passthrough; the tariff kick-up distribution to Family/Clan/Imperial is handled at the daimyo's tier, not the governor's)
    * Note that in the provinces of the example Reiji domain below (such as our example Nagahara province) collect slightly less in gross tariffs (~6,800 vs ~7,800) because the Reiji hold their gate tariff near ~13% rather than the ~15% standard - competitive pressure from three bordering low-tariff Minor Clans, passing their absorbed Family layer to merchants rather than pocketing it - with correspondingly lower throughput (~43,000) and tax obligation (~23,500).
* ~5,000 funds the six provincial ministries' **overhead budgets** (materials, contracts, ministry-specific staff, the minister's formal stipend and customary skim)
* ~4,500 funds the broader cohort of ~225 working provincial samurai the governor pays (stipends + food + equipment, averaging ~20 koku each; the other ~25 of the province's ~250-strong working cohort serve in Empire-paid posts elsewhere)
* The remaining ~10,000 koku is the **governor's discretionary funds** - the "tax-farming cut" that defines the post's value, parallel to a county magistrate's ~1,000-koku cut.

**Note on what ministry budgets cover**: The provincial ministry budgets shown here (and the domain ministry budgets shown later) are **overhead budgets only** - they do NOT include samurai stipends for the broader provincial samurai cohort.  Stipends are funded as a separate line item from the governor's overall budget.  The Ministry of Retainers *administers* stipend disbursement as throughput (handling rice/coin denomination decisions, calculating per-samurai allocations under the rank-squared rule, and physically disbursing on payment days), but the actual stipend funds flow from the governor's tax-farming allocation rather than from the Retainers ministry's own ~250-koku overhead budget.  Only working samurai past their gempukku and not yet retired receive stipends; children and retired samurai consume from their family households' resources rather than from a separate state allocation (matching the convention documented in [What the samurai counts mean](#what-the-samurai-counts-mean) above).

**Note on tariff-collection staff at the provincial city gate**: of the ~225 working provincial samurai counted above, typically ~15-30 are deployed to the provincial city gate as "the Yasuki Taka system" inspectors and licensors who handle physical tariff collection from arriving caravans.  Their stipends come out of the ~4,500-koku provincial samurai compensation line rather than the Ministry of Revenue's ~150-koku overhead budget; the Revenue ministry's overhead budget covers materials (the publicly posted tariff-rate boards, manifest paper, stamps, courier dispatch to Otosan Uchi with sealed records) but not the personnel themselves.  This is in addition to the small cohort of Imperial yoriki (~7-8 per provincial city) attached to the Imperial Magistrate's office who audit the operation for the Emperor's 5% cut - those yoriki are funded from the Imperial Magistrate line in the Imperial Budget rather than from any provincial or domain budget.

The 5,000-koku provincial ministry overhead allocation breaks down across the six ministries, with effective income for each Rank 7 provincial minister:

| Ministry | Budget per province | Minister's stipend | Informal income | Gifts | Minister's effective income |
| --- | --- | --- | --- | --- | --- |
| Works | ~3,000 | 49 | ~300 | ~0 | **~350** |
| War | ~700 | 49 | ~70 | ~150 | **~270** |
| Rites | ~600 | 49 | ~60 | ~20 | **~130** |
| Justice | ~300 | 49 | ~30 (formal) | ~20 (virtuous) to ~420+ (corrupt, incl. fines) | **~100 to ~500+** |
| Retainers | ~250 | 49 | ~25 (formal) + ~180 (rice/coin arbitrage on ~3,375-koku provincial stipend throughput) | ~40 | **~295** |
| Revenue | ~150 | 49 | ~15 (formal) + ~450 (collection fees on ~44,000-koku province revenue throughput, ~1%) | ~15 | **~530** |
| **Total** | **~5,000** |  |  |  |  |

A few things to notice:

- The **provincial governor** at ~10,000 koku discretionary income is the wealthiest provincial-tier official by an enormous margin - almost 20x the next-highest provincial minister (Revenue).
- The **county magistrate** at ~1,000 koku discretionary (~955 from tax surplus + ~150 from gifts in Hikai's case, ~1,105 total) is actually wealthier than every provincial minister, despite holding a lower rank (Rank 5 vs Rank 7).  This is well-known in Rokugan and explains why ambitious junior samurai often prefer a county magistrate appointment to a provincial ministry appointment.
- The **provincial Minister of Justice** at the virtuous floor (~100 koku) is genuinely poor for a Rank 7 official, comparable to a Tokugawa-era ordinary hizamurai.  The ceiling for a corrupt one in a wealthy province can exceed the Minister of Works.
- The **provincial Minister of War**, like its domain counterpart, draws more in gifts (from promotion-seeking underlings and appointment-seeking outsiders) than its tiny ~700-koku budget implies - ~270 effective, above Rites and a virtuous Justice but far below a corrupt one.

### Cross-cutting project negotiation

For projects that span multiple tiers (a new canal across the domain, maintenance of a road that crosses several provinces, mobilization for clan warfare), the question of who pays which share is a major source of domain politics.  The general pattern:

- **Routine maintenance** stays at the tier responsible for that scope (county roads = magistrate; provincial roads = governor; capital infrastructure = daimyo)
- **Capital projects** are negotiated, often with the daimyo expecting affected governors to contribute from their provincial Works budgets, and governors arguing that domain-spanning projects should come from the domain Works budget alone
- **Emergencies** (war, famine relief) involve the daimyo drawing from their contingency reserves and demanding "emergency contributions" from governors above their normal budgets

A ~10,000-koku canal project, for example, might be funded purely from domain Works (using ~33% of that year's domain Works budget), or split as ~6,000 from domain Works + ~600-700 from each of 6 affected provinces' Works budgets.  Which solution prevails depends on the daimyo's bargaining position, the governors' political weight, and the lineage chancellors' opinions in the chancellery.

Canals are in every case a domain-and-clan matter, never a standing Imperial line.  A domain has them only where its geography offers a sizable inland river worth canalizing - the Lion's link from Toshi Ranbo to the Drowned Merchant River is the type case - while coastal clans like the Crane, who move goods by sea and cart only the last few miles, have little need of them.  Unlike imperial China, Rokugan maintains no centrally-managed canal network: the force that made China's Grand Canal an Imperial concern was the need to haul tax grain across the empire to an inland or grain-poor northern capital, and that imperative was designed out of the Rokugani model.  Most tax grain stays in local domain granaries rather than converging on the center, and Otosan Uchi itself sits on the eastern coast and is provisioned by sea - in the manner of Rome, Alexandria, or Constantinople - rather than fed down an inland grain artery.  Any Imperial hand in canals is therefore incidental: an occasional Crown-funded major waterwork falls under the Imperial Ministry of Works' central-operations line, and any audit presence where a canal meets a city is already covered by the city-gate tariff apparatus.

## Example office-holder budgets

### Magistrate Hida no Reiji Hikai of Seitoyama County

Seitoyama is a county in Nagahara province of the Reiji domain (Crab Clan).  Hida no Reiji Hikai is its current magistrate, a moderately conscientious official well-regarded by peasants and respected by their retainers.  The breakdowns below show Hikai's specific allocation choices; other magistrates with the same ~1,000-koku discretionary allocation but different personalities, lineage politics, or local circumstances allocate very differently.

#### Income

| Source | Households | Tax type | Total |
| --- | --- | --- | --- |
| Town farmers (1 town × ~156 households) | ~156 | Land tax (~5 koku/household) | ~780 |
| Village farmers (6 villages × ~70 households each) | ~420 | Land tax (~5 koku/household) | ~2,100 |
| Hamlet farmers (36 hamlets × ~15 households each) | ~540 | Land tax (~5 koku/household) | ~2,700 |
| Town merchants (very rich, rich, poor, and ordinary) | ~24 | Property + business | ~700 |
| Town laborers, servants, and burakumin | ~55 | Property + business | ~125 |
| **Total county tax revenue** |  |  | **~6,400** |

Math note: each farming household has ~5 members and pays ~5 koku per year in land tax (following the [Rice and arable-land math](#rice-and-arable-land-math)).  The ~1,116 farm families in the county contribute ~5,580 koku in farm taxes.  The remaining ~825 koku is property and business tax from town residents, dominated by the wealthy merchants - the very-rich merchant families pay ~235 koku each in combined property + business tax, while the ordinary "merchants, other" households pay ~5 koku each.  Per-household rates by caste sub-category are detailed in the [Town](#town) caste table earlier in this document.

Seitoyama is a heavily agrarian county, so Magistrate Hikai's tax revenue comes almost entirely from land tax and ordinary town property/business taxes.  Local specialized industries do exist, e.g. the local clothier, sake brewer, etc, but their licenses are captured in the business tax column above and do not constitute a separate revenue stream.  Counties with major specialized industries (coastal counties with substantial fishing or salt-making operations, mountain counties with mining, river-junction counties with major brewing or paper-making) collect additional "small assessments" (in the Tokugawa *komononari* sense) beyond what is shown here, sometimes amounting to several hundred koku per year, occasionally more for an exceptional county.

#### Mandatory expenses

| Category | Annual koku | Notes |
| --- | --- | --- |
| Tax obligation to Governor Hida no Reiji Asuka | ~5,000 | The county's share of provincial revenue, passed up the chain |
| Samurai stipends (~15 useful samurai × ~10 koku avg) | ~150 | Rank-squared rule, avg rank ~3 |
| Samurai food allowance (~15 × ~3 koku) | ~45 |  |
| Samurai equipment allowance (~15 × ~2 koku) | ~30 |  |
| Ashigaru stipends | ~190 |  |
| Office servants | ~20 |  |
| Office supplies | ~10 |  |
| **Total mandatory** |  | **~5,445** |

#### Gift income (in addition to tax revenue)

Beyond tax revenue, Magistrate Hikai receives approximately **~150 koku per year in seasonal gifts** from local notables - primarily merchant landlords (the largest single category, since they hold most rural rentable land in the county), wealthy artisans and tradesmen (the sake brewer, the master smith, the dye-house owner), and ceremonial visitors from the magistrate's own lineage.

Unlike gifts to a Minister of Justice (which can shade into transactional bribery, since a Minister of Justice can directly grant rulings whose value far exceeds the gift), gifts to a county magistrate are predominantly **relational rather than transactional**.  The structural reason is that the magistrate's discretionary income depends on meeting their tax obligation to the governor: forgiving ~1,000 koku of land tax owed by a merchant landlord in exchange for a ~100-koku gift would be forgiving the county magistrate's own income, since the magistrate must make up any shortfall in their tax obligation to the provincial governor.  The most effective way for a landlord to keep a magistrate happy is therefore not large gifts but rather **efficient rent collection and avoidance of tenant disputes** that would otherwise require the magistrate's costly intervention.

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
| Lineage patronage donation to the Reiji chancellor | ~110 | Expected (~10%) | "Voluntary" but socially-pressured; the customary tithe on total discretionary income |
| **Subtotal: expected donations** | **~690** |  | ~62% of the allocation, consumed by never-required-but-always-expected obligations |
| Lean-year savings (forward-thinking reserve) | ~250 | Personal | ~23% put away against bad harvests; well above the irresponsible ~5-10% range that many magistrates of lesser foresight accept |
| Personal household and lifestyle (clothing, sword maintenance, family expenses) | ~105 | Personal | Gift income particularly helps here; many of the gifts received (silk, sake, fine goods) are themselves household-quality items that reduce out-of-pocket personal spending |
| Truly free (small luxuries, gifts to others, personal indulgences) | ~60 | Personal | About 1 koku per week of unconstrained spending |
| **Subtotal: personal/discretionary** | **~415** |  | ~38% of allocation, of which ~60 koku is truly unconstrained |
| **Total** | **~1,105** |  |  |

#### Summary

Magistrate Hida no Reiji Hikai is responsible for collecting ~6,400 koku in taxes annually from Seitoyama county, of which ~5,000 goes up to Governor Hida no Reiji Asuka and ~445 covers stipends and office expenses.  The remaining ~955 koku is Hikai's tax-derived discretionary income, supplemented by ~150 koku in seasonal gifts from local notables, for a total of ~1,105 koku per year.  After festivals, almsgiving, county operations, retainer hospitality, and the customary lineage tithe, ~415 koku is truly personal - of which Hikai is forward-thinking enough to save ~250 against future lean years.  Hikai's truly-unconstrained spending is around ~60 koku per year, comfortable but not lavish.

By all accounts Hikai is a virtuous magistrate.  One in their position who skimped on festivals or pocketed the lineage donation might keep two to three times that amount for themselves, at the cost of their standing in the lineage and the community.

### Governor Hida no Reiji Asuka of Nagahara Province

Nagahara is a province in the Reiji domain (Crab Clan), containing Seitoyama county (administered by Magistrate Hikai, above) among its six counties.  Hida no Reiji Asuka is its current governor, a moderately accomplished official well-regarded within the Reiji Chancellery though not particularly distinguished in the broader Crab political landscape.  The breakdowns below show Asuka's specific allocation choices; other governors with the same ~10,000-koku discretionary allocation distribute very differently depending on the wealth of their province and their personal temperament.

#### Income

| Source | Annual koku | Notes |
| --- | --- | --- |
| Tax obligation from 6 county magistrates (~5,000 each) | ~30,000 | Standard provincial-tier share of county tax revenue; Hikai's ~5,000 obligation is one of these six |
| Provincial city direct tax base (property + business; dominated by very-rich and rich merchant households) | ~6,200 | Per the Provincial City caste table above |
| Provincial city import tariffs ("the Yasuki Taka system" at the city gates; 13% effective rate × ~52,000 koku of imported goods sold annually) | ~6,800 | Varies by trade volume; Nagahara is a typical inland Crab province with steady but moderate caravan traffic through its provincial city, primarily from neighboring Scorpion lands.  The 13% effective rate reflects the Reiji's Hida-vassal status: the 2% Family-daimyo layer is absorbed into the clan-daimyo layer (since both are Hida Kisada), giving an 8% kick-up layer instead of the standard 10%, plus the ~5% average daimyo cut (out of the ≤10% legal maximum the daimyo can charge).  All of this tariff revenue passes up the chain - 100% of it is either kick-ups or daimyo's portion, with none retained at the provincial level |
| **Total provincial throughput** |  | **~43,000** |

#### Mandatory expenses

| Category | Annual koku | Notes |
| --- | --- | --- |
| Tax obligation to Daimyo Hida no Reiji Isao (includes the full ~6,800 of tariff passthrough plus ~16,200 of land-tax kick-up, plus the ~500 saved on samurai now in Imperial service and passed up - the kick-up structure on tariffs is handled at Isao's tier, not Asuka's) | ~23,500 | The province's share of domain revenue, passed up the chain |
| Provincial samurai stipends (~225 working samurai × ~15 koku average; the other ~25 of the province's working cohort serve in Empire-paid posts elsewhere; only working samurai past their gempukku and not yet retired receive stipends) | ~3,375 | Distributed across the six ministries and the governor's personal household roles; the Ministry of Retainers administers disbursement, but the funds flow from the governor's allocation rather than from the Retainers ministry's ~250-koku overhead budget |
| Provincial samurai food allowance (~225 × ~3 koku) | ~675 |  |
| Provincial samurai equipment allowance (~225 × ~2 koku) | ~450 |  |
| Provincial ministry overhead budgets (sum across the six ministries; materials, contracts, ministry-specific staff, ministers' formal stipends and customary skims) | ~5,000 | Per the [Provincial ministry budgets](#provincial-ministry-budgets) table above; overhead only, NOT including the samurai stipends shown separately above |
| Provincial servants and supplies | ~30 |  |
| **Total mandatory** |  | **~33,030** |

Math note: the 6 county magistrates pass up ~30,000 koku, the provincial city's own tax base contributes ~6,200, and tariffs at the provincial city gates contribute ~6,800 (Hida-vassal 13% effective rate × ~52,000 koku of imported goods) - bringing total throughput to ~43,000.  Of this, ~23,500 goes up to Daimyo Isao (composed of ~16,200 land-tax kick-up plus the full ~6,800 tariff passthrough plus ~500 in samurai-stipend savings passed up; the kick-up structure on tariffs is handled at Isao's tier, not Asuka's, since the Family/Clan/Imperial layers are paid out at the domain level rather than retained at any provincial level); ~4,500 funds the broader samurai cohort's compensation (stipends + food + equipment for ~225 working samurai serving in-province); ~5,000 funds the six provincial ministries' overhead budgets; ~30 covers minor servants and supplies.  Asuka is left with **~10,000 koku of discretionary income** - the "tax-farming cut" that defines the post's value, parallel to a county magistrate's ~1,000-koku cut.  All of Asuka's personal household operations, manor, retinue hospitality, festival and almsgiving obligations, lineage tithe, savings, and truly-personal spending come out of this ~10,000 plus her gift income, broken down further below.

A structural note: the ~23,500 tax obligation is meaningfully less than the ~30,000 sum of the 6 county magistrates' tributes.  The governor receives ALL provincial revenue (county tribute, the provincial city's direct tax base, and the city-gate tariffs) and decides what funds provincial operations, what they keep, and what flows up.  Of the ~13,000 the governor effectively retains from county money beyond the daimyo's share, most goes to funding the provincial samurai cohort (~4,500 in stipends and allowances) and the six provincial ministries' overhead budgets (~5,000) - both of which have no equivalent at the county tier, where the magistrate IS the institution.

#### Gift income

Beyond tax revenue, Governor Asuka receives approximately **~1,000 koku per year in seasonal gifts** from notables across Nagahara.  The major categories:

- **The 6 county magistrates under her authority** each give ceremonial gifts on New Year and the major festivals (~8 koku per occasion per magistrate, following the rank-scaled gift convention for the Rank 8 provincial governor; ~200 koku/year total)
- **Very-rich and rich merchant families in the provincial city** (~30 households between them; gifts scale by household wealth, totaling ~400 koku/year)
- **Wealthy merchant landlords from outlying counties** whose holdings span multiple counties and who therefore have province-wide rather than purely county-level concerns (~6 counties × 2-3 such families × ~5 koku/year ≈ ~80 koku)
- **Major sake brewers** in the province (a handful of large operations whose annual licenses approach 100 koku; gifts of ~15-20 koku/year each, totaling ~75 koku)
- **The six provincial ministers serving under Asuka** (~30 koku/year each; partially reciprocated since Asuka also gifts subordinates downward, so the net inflow is closer to ~100 koku)
- **Lineage chancellor and senior lineage members** (~75-100 koku, exchanged in both directions with substantial net symmetry)
- **Peer governors and visiting daimyo representatives** (variable, ~50 koku net inflow in a typical year)

This totals roughly 6-7x Magistrate Hikai's ~150-koku gift income.  The increase reflects the broader jurisdiction and richer pool of potential gifters - and the larger denominational increments scaled to the governor's higher rank - but NOT a qualitatively different scale that would mark transactional bribery.  A governor reporting 10x or more in gift income relative to a county magistrate is generally operating somewhere on the corrupt end of the spectrum.

Like gifts to a county magistrate, gifts to a provincial governor are predominantly **relational rather than transactional** for the same fiscal reasons: forgiving merchant tax obligations in exchange for gifts would forgive Asuka's own income, since she must meet her ~23,500-koku tax obligation to Daimyo Isao regardless.  The governor's structural temptation toward transactional gifts comes not from tax forgiveness but from **policy discretion** - provincial-level decisions about tariff rates on specific goods, road maintenance priorities between counties, market regulations at the provincial city, and recommendations to the daimyo about appointments can favor or harm specific merchant houses by amounts far exceeding any individual gift.  A virtuous governor declines gifts that arrive too close to such decisions; a corrupt governor in a wealthy province can extract substantially more than the ~1,000-koku baseline, with the ceiling set by the same factors that limit the Minister of Justice (visibility within the lineage, the daimyo's attention, the Imperial magistrate stationed in the domain capital).

#### Discretionary residual

Of the ~43,000-koku provincial throughput, ~33,000 goes to mandatory expenses, leaving Asuka with **~10,000-koku tax-derived discretionary allocation** (her "tax-farming cut").  Combined with the ~1,000-koku gift income, Asuka's effective total discretionary income is **~11,000 koku per year**.

#### Asuka's discretionary breakdown

This is specifically how Governor Asuka chooses to allocate her ~11,000-koku total discretionary income (~10,000 from tax surplus + ~1,000 from gifts), separated between expected obligations and personal/discretionary spending.  Other governors with the same allocation distribute very differently.

| Category | Annual koku | Type | Notes |
| --- | --- | --- | --- |
| Provincial festival hosting and almsgiving (combined) | ~2,300 | Expected | Provincial festivals are more elaborate than county festivals; almsgiving at provincial scale is more visible and politically important |
| Retainer hospitality (food, sake, occasional lodging for the personal household samurai and the ~6 visiting county magistrates and ~6 provincial ministers Asuka entertains regularly) | ~1,500 | Expected | Notionally retainers' stipends cover their day-to-day; in practice failure to host generously erodes loyalty across the entire provincial command |
| Visitor hospitality (lineage chancellor visits, Daimyo Isao's representatives, the Imperial magistrate, peer governors, Crab Clan officials) | ~700 | Expected |  |
| Religious patronage (donations to the provincial abbot's temples and minor village shrines beyond the formal Rites budget) | ~500 | Expected |  |
| Lineage patronage donation to the Reiji chancellor | ~1,100 | Expected (~10%) | Customary tithe on total discretionary income |
| **Subtotal: expected donations** | **~6,100** |  | ~55% of allocation, consumed by the same never-required-but-always-expected obligations that consume the majority of a county magistrate's discretionary income |
| Governor's manor and household operations (servants, food, fuel, maintenance, stable, security supplies, garden and grounds upkeep, office supplies, courier service) | ~1,500 | Personal | The governor's personal household infrastructure; analogous to Hikai's "personal household and lifestyle" line but larger because of the scale of a governor's residence |
| Lean-year savings (forward-thinking reserve) | ~2,000 | Personal | ~18% put away against bad harvests, blight years, military levies, or unexpected provincial obligations |
| Personal household and lifestyle (clothing, sword maintenance, family expenses, political wardrobe for chancellery appearances) | ~900 | Personal | Higher than Hikai's because the governor's household includes a wider family circle plus visible political wardrobe expectations at the chancellery |
| Truly free (small luxuries, gifts to subordinates above the customary, personal indulgences) | ~500 | Personal | Around ~40 koku per month of unconstrained spending |
| **Subtotal: personal/discretionary** | **~4,900** |  | ~45% of allocation, of which ~500 koku is truly unconstrained |
| **Total** | **~11,000** |  |  |

#### Summary

Governor Hida no Reiji Asuka is responsible for collecting ~43,000 koku in tax revenue annually from Nagahara province, of which ~23,500 goes up to Daimyo Hida no Reiji Isao (composed of ~16,200 in land-tax kick-up plus the full ~6,800 in tariff passthrough plus ~500 in passed-up samurai-stipend savings), ~4,500 funds the broader cohort of ~225 working provincial samurai serving in-province (stipends + food + equipment), and ~5,000 funds the six provincial ministries' overhead budgets.  This leaves Asuka with a ~10,000-koku tax-derived discretionary allocation (the governor's "tax-farming cut"), supplemented by ~1,000 koku in seasonal gifts from the province's notables, for a total of ~11,000 koku per year.  After festivals, almsgiving, retainer and visitor hospitality, religious patronage, and the customary lineage tithe (~6,100 in expected obligations), and after manor operations and personal household expenses (~2,400), ~2,500 koku remains for savings and truly-unconstrained spending - of which Asuka is forward-thinking enough to save ~2,000 against future lean years.  Her truly-unconstrained spending is around ~500 koku per year, roughly 8x Magistrate Hikai's truly-unconstrained ~60 koku.

This reflects Asuka's higher tier and broader responsibilities, but it is NOT a fundamentally different lifestyle - the governor of a typical province lives perhaps as a wealthier-than-average mounted samurai might, not as a minor daimyo.  By all accounts Asuka is a virtuous-but-not-exceptional governor: she meets her obligations to the daimyo on time, refuses transactional gifts on contested policy decisions, hosts the expected festivals, and is well-regarded if not actively beloved within her lineage.  A more politically ambitious governor would cultivate the chancellery more aggressively (and pay for the cultivation out of personal savings); a less scrupulous one in the same role could extract two to three times Asuka's discretionary income through transactional policy gifts, at the cost of standing within the Reiji Chancellery and the Crab Clan more broadly.

### Daimyo Hida no Reiji Isao of the Reiji Domain

The Reiji are a fairly typical inland Crab domain: agricultural-base economy, modest mining operations in the hill country, steady caravan trade through the domain capital from neighboring Scorpion lands, and the standard Crab obligation to contribute manpower and material to the Kaiu Wall through the clan-level allocation rather than direct frontier defense.  Hida no Reiji Isao is the current Reiji house daimyo, an experienced administrator who succeeded his father about a decade ago, well-regarded within the Hida Family but not particularly distinguished in broader Crab Clan politics.  The breakdowns below show Isao's specific allocation choices; other daimyo with similar inland domains allocate very differently depending on the local economy, military pressures, and the daimyo's temperament.

#### Income

| Source | Annual koku | Notes |
| --- | --- | --- |
| Tax obligation from 6 provincial governors (~23,500 each) | ~141,000 | Standard domain-tier share of provincial revenue; Asuka's ~23,500 obligation is one of these six.  Each governor's obligation decomposes as ~16,200 land-tax kick-up plus ~6,800 of provincial-city tariff passthrough plus ~500 in samurai-stipend savings passed up (the governors' samurai who left for Imperial service); the kick-ups on tariffs are distributed at the daimyo's tier, not at the provincial tier |
| Capital city direct tax base (property + business; dominated by the capital's larger and wealthier merchant population than provincial cities) | ~25,000 | Per the Capital City caste table above |
| Capital city import tariffs (taken at the capital city gates; 13% effective rate × ~233,000 koku of imported goods sold annually) | ~30,000 | Substantial because the capital is the largest urban center in the domain (~12,000 inhabitants) and the principal caravan junction for trade through the Reiji domain; the 13% effective rate reflects the Reiji's Hida-vassal status (Family-Clan layer consolidated).  Like provincial tariffs, the full ~30,000 passes up to kick-ups (Family/Clan/Imperial) and the daimyo's own portion, not retained gross |
| Domain mining royalties (iron and minor metal works from the hill country) | ~20,000 | A characteristic feature of Crab domains; the Reiji's inland hill country supports modest iron, tin, and copper works whose extracted value flows partly to the daimyo as a royalty |
| Other domain-level revenue (large cross-province sake export licenses, craft monopolies such as silk and fine paper, special assessments / *komononari* on specific industries) | ~30,000 | The aggregated revenue from licenses and assessments that the daimyo collects directly rather than passing through the provincial tier |
| **Total domain throughput** |  | **~246,000** |

#### Mandatory expenses

| Category | Annual koku | Notes |
| --- | --- | --- |
| Land-output kick-ups to Hida Kisada (as both Hida Family daimyo and Crab Clan daimyo) and the Imperial center (8% of land output) | ~48,200 | Calculated against the domain's assessed land output (the *kokudaka*, ~602,640 koku), not against actual harvest.  The standard split is 2% family + 3% clan + 5% Imperial = 10%, but the Reiji are a Hida vassal house and Hida Kisada holds BOTH the Hida Family daimyo title AND the Crab Clan daimyo title - so the family-level 2% layer is not levied separately and the Reiji keeps it (the "family services" it notionally funds are already covered by the clan's operations when the same person heads both); on land tax, which is captive, that ~12,000 koku/year goes straight to the daimyo's cut.  Other domains where the Family and Clan daimyo are distinct people pay the full 10% per the split documented in [l7r.md - The Ministry of Revenue](l7r.md#the-ministry-of-revenue); the ~12,000-koku/year savings is one of the structural advantages of being a Hida vassal house |
| Tariff kick-ups to Hida Kisada and the Imperial center (8% of declared sales value at every provincial and capital city gate within the Reiji domain) | ~43,600 | Calculated against the domain's total imported-goods sales volume (~545,000 koku/year across 6 provincial cities + the capital).  Composed of ~16,350 to Kisada (3% combined Family+Clan, with the Family-daimyo 2% layer absorbed per the Hida-vassal note above) plus ~27,250 to the Imperial center (5% of trade volume, per the rate structure documented in [l7r.md - The Ministry of Revenue](l7r.md#the-ministry-of-revenue)).  Other domains where the Family-daimyo layer is not absorbed pay the full 10% tariff kick-up rate |
| Capital samurai stipends (~800 working samurai × ~35 koku average; the other ~150 of the capital's working cohort serve in Empire-paid Imperial posts; only working samurai past their gempukku and not yet retired receive stipends) | ~28,000 | Distributed across the six domain ministries and the daimyo's personal household roles; the Ministry of Retainers administers disbursement, but the funds flow from the daimyo's allocation rather than from the Retainers ministry's ~3,000-koku overhead budget |
| Capital samurai food allowance (~800 × ~3 koku) | ~2,400 |  |
| Capital samurai equipment allowance (~800 × ~2 koku) | ~1,600 |  |
| Domain ministry overhead budgets (sum across the six ministries; materials, contracts, ministry-specific staff, ministers' formal stipends and customary skims) | ~50,000 | Per the [Domain ministry budgets](#domain-ministry-budgets) table above; overhead only, NOT including capital samurai stipends shown separately above |
| Domain servants, supplies, and the daimyo's direct administrative staff (outside the ministry budgets) | ~1,400 |  |
| **Total mandatory** |  | **~175,200** |

Math note: the 6 provincial governors pass up ~141,000 koku, the capital city's own tax base contributes ~25,000, the tariff system at the capital city gates contributes ~30,000, mining royalties contribute ~20,000, and other domain-level revenue contributes ~30,000 - bringing total throughput to ~246,000.  Of this, ~48,200 flows up to Hida Kisada and the Imperial center as the Reiji's 8% land-output kick-ups (reduced from the standard 10% per the Hida-vassal note above); ~43,600 flows up to Hida Kisada and the Imperial center as the Reiji's 8% tariff kick-ups on the domain's ~545,000 koku of imported-goods sales volume; ~32,000 funds the ~800 working capital samurai the daimyo pays (stipends + food + equipment); ~50,000 funds the six domain ministries' overhead budgets; ~1,400 covers minor domain administrative overhead.  Daimyo Isao is left with **~71,000 koku of discretionary income** - the daimyo's "tax-farming cut," substantially higher than a provincial governor's ~10,000 and a county magistrate's ~1,000.  This figure varies widely across domains depending on trade volume, tariff structure (Hida-vassal vs standard), domain wealth, and military pressures: wealthy maritime trade or large Clan-capital domains run substantially higher; frontier or war-recovering domains run substantially lower.  The Reiji's ~71,000 sits *above* the ~58,000 typical median because of its Hida-vassal status, which lets it stop levying the 2% Family-daimyo kick-up layer (Hida Kisada holds both the Hida Family and Crab Clan daimyo titles, so there is no separate Family daimyo to pay).  The two halves of that layer behave very differently, because land tax is captive and tariffs are not.  On **land** - peasants cannot relocate to a cheaper jurisdiction - the Reiji simply keep the 2% (~12,000 koku/year), and *that* is what lifts the cut to ~71,000, above the ~58,000 typical median.  On **tariffs** they cannot: the Reiji border three Minor Clans, whose domains carry neither Family nor Clan kick-ups and therefore far lower gate tariffs, and the resulting competition forces the Reiji to hold their own gate tariff near ~13% rather than the ~15% standard - so the absorbed tariff 2% (~10,900 koku/year) is handed to merchants as a lower rate rather than pocketed, showing up as ~10,900 of *lower throughput* instead of a bigger cut.  Most ruling-Family vassal houses face no such neighbor and simply keep their tariff at ~15%, pocketing that ~10,900 - so a typical one runs nearer ~81,000, and the Reiji's tariff restraint is a locally-compelled choice to sit below its ruling-Family peers.  (Separately, the ~203 working samurai the Empire pays while they serve in Imperial posts also free up stipend money for the daimyo's cut, but that applies to *every* domain and is already built into the ~58,000 median.)

#### Gift income

Beyond tax revenue, Daimyo Isao receives approximately **~6,000 koku per year in seasonal gifts** from notables throughout the Reiji domain and the broader Crab Clan.  The major categories:

- **The 6 provincial governors under his authority** each give ceremonial gifts on New Year and the major festivals (~12 koku per occasion per governor, following the rank-scaled gift convention for the Rank 12 daimyo; ~288 koku/year total)
- **The 6 domain ministers serving under Isao** (~12 koku/occasion each × 4 occasions; partially reciprocated since Isao gifts downward too, so the net inflow is closer to ~150 koku)
- **Wealthy merchant families in the capital city** (~48 very-rich and rich merchant households between them; gifts scale by household wealth, totaling ~2,000 koku/year)
- **Major sake brewers, mining concerns, and large industrial operators across the domain** (~800-1,200 koku/year combined)
- **Wealthy lineage notables and vassal-lineage leaders within the Reiji domain** (~800-1,200 koku/year, with substantial reciprocal flow as Isao gifts down to maintain political relationships)
- **County magistrates throughout the domain (~36 of them) and minor officials at various tiers** (~36 × small ceremonial gifts ≈ ~400 koku/year aggregate)
- **Visiting peers and dignitaries** (other Clan daimyo, Imperial Court representatives, foreign envoys; ~variable, mostly reciprocated, ~200 koku net inflow in a typical year)
- **Miscellaneous minor gifts** (artisan and merchant guild offerings, temple and shrine reciprocations, smaller vassal-lineage tokens, and one-off ceremonial occasions across the year) (~700-1,000 koku/year aggregate)

This totals roughly 6x Governor Asuka's ~1,000-koku gift income, consistent with the per-tier scaling between magistrate (~150), governor (~1,000), and daimyo (~6,000).  The daimyo's gift income would scale higher in a wealthier maritime or capital-clan domain, where the merchant gift pool is much larger and the political weight of the daimyo's decisions draws bigger transactional pressure.

As at the lower tiers, gifts to a daimyo are predominantly **relational rather than transactional** - Isao must meet his ~91,800-koku combined kick-up obligations (land output ~48,200 + tariffs ~43,600) regardless of any gift income, and the bulk of his political authority comes from honoring the well-understood structural obligations of his position.  The structural temptation toward transactional gifts at the daimyo tier comes from **domain-shaping decisions**: appointment of governors and ministers, allocation of provincial Works budgets, recognition or denial of vassal-lineage land claims, tariff rate adjustments that favor specific merchant houses, and the daimyo's voice within the Crab Clan chancellery on matters that affect lineages beyond their own domain.  A virtuous daimyo declines gifts that arrive too close to such decisions; a corrupt one in a wealthy domain can extract substantially more than the ~6,000-koku baseline, with the ceiling set by the visibility of the daimyo's actions to the Clan daimyo (Hida Kisada) and the Imperial Court.

#### Discretionary residual

Of the ~246,000-koku domain throughput, ~175,200 goes to mandatory expenses, leaving Daimyo Isao with **~71,000-koku tax-derived discretionary allocation** (his domain's "tax-farming cut").  Combined with the ~6,000-koku gift income, Isao's effective total discretionary income is **~77,000 koku per year**.

#### Isao's discretionary breakdown

This is specifically how Daimyo Isao chooses to allocate his ~77,000-koku total discretionary income (~71,000 from tax surplus + ~6,000 from gifts), separated between expected obligations and personal/discretionary spending.  Other daimyo with comparable allocations distribute very differently.

| Category | Annual koku | Type | Notes |
| --- | --- | --- | --- |
| Domain festival hosting and almsgiving (combined; includes capital-scale ceremonies attended by Imperial representatives in major years, almsgiving distributions across the domain during festivals and famine relief) | ~12,000 | Expected | Capital festivals are several orders of magnitude larger and more elaborate than provincial festivals; almsgiving at domain scale is a major political-religious obligation |
| Retainer hospitality (food, sake, lodging for the daimyo's extended household + the ~6 provincial governors entertained quarterly + the ~6 domain ministers + senior visiting yoriki and family members) | ~6,000 | Expected |  |
| Visitor hospitality (Crab Clan daimyo's representatives, Imperial Court emissaries, peer daimyo, foreign envoys, lineage chancellor visits, occasional sankin-kotai-style attendance costs) | ~3,600 | Expected |  |
| Religious patronage (donations to capital temples, Crab Clan obligation toward Kaiu Wall temple support, major shrine patronage, contributions to Fortunist orders that operate within the domain) | ~3,000 | Expected | Substantially higher than provincial-level because of the Kaiu Wall obligation that all Crab domains share regardless of direct frontier exposure |
| Inter-domain political maintenance (gifts to other Clan daimyo for alliance maintenance, sponsorships of Crab Clan tournaments and ceremonies, political donations to clan chancellery initiatives) | ~3,600 | Expected | A category that does not meaningfully exist at lower tiers; the daimyo operates at a political scale where ongoing inter-domain relationships require costly cultivation |
| Lineage patronage donation to the Reiji chancellor | ~7,700 | Expected (~10%) | Customary tithe on total discretionary income; the Reiji chancellor administers the lineage's voluntary contributions fund per the standard pattern |
| **Subtotal: expected donations** | **~35,900** |  | ~47% of allocation, consumed by the never-required-but-always-expected obligations of the daimyo's office |
| Daimyo's manor and household operations (the capital castle, servants for the daimyo's extended family, food and fuel and maintenance for a structure that may house hundreds of household personnel, stable for a large warhorse contingent, security supplies, garden and grounds upkeep, courier service across the domain) | ~7,200 | Personal | The daimyo's castle is the political and administrative center of the domain; its operations dwarf any provincial governor's manor |
| Lean-year savings (forward-thinking reserve, supplemented by the kind of long-horizon planning expected of a daimyo) | ~25,000 | Personal | ~32% put away against bad harvests, military emergencies, succession disputes, or unexpected Imperial obligations; the daimyo is expected to maintain reserves several times what a virtuous governor would |
| Personal household and lifestyle (extensive seasonal wardrobe for political appearances, daimyo-tier sword maintenance, expenses of an extended noble family including children's tutors and gempukku ceremonies, jewelry and other status goods) | ~6,000 | Personal |  |
| Truly free (small luxuries, personal indulgences, gifts to subordinates above the customary, patronage of artists and poets, occasional impulsive purchases) | ~2,900 | Personal | Around ~240 koku per month of unconstrained spending |
| **Subtotal: personal/discretionary** | **~41,100** |  | ~53% of allocation, of which ~2,900 koku is truly unconstrained |
| **Total** | **~77,000** |  |  |

#### Summary

Daimyo Hida no Reiji Isao is responsible for the financial operation of the Reiji domain, which generates ~246,000 koku in annual tax revenue at the daimyo's tier.  Of this, ~48,200 flows up to Hida Kisada (in his combined role as Hida Family daimyo and Crab Clan daimyo) and the Imperial center as the Reiji's 8% land-output kick-ups (a reduced rate from the standard 10%, reflecting the Reiji's Hida-vassal status); ~43,600 flows up as the Reiji's 8% tariff kick-ups on the domain's ~545,000 koku of imported-goods sales volume; ~32,000 funds the ~800 working capital samurai the daimyo pays (stipends + food + equipment); ~50,000 funds the six domain ministries' overhead budgets; ~1,400 covers minor domain administrative overhead.  This leaves Isao with a ~71,000-koku tax-derived discretionary allocation, supplemented by ~6,000 koku in seasonal gifts from across the domain and clan, for a total of ~77,000 koku per year.  After festivals, almsgiving, retainer and visitor hospitality, religious patronage (including the Kaiu Wall contribution), inter-domain political maintenance, and the customary lineage tithe (~35,900 in expected obligations), and after manor operations and personal household expenses (~13,200), ~27,900 koku remains for savings and truly-unconstrained spending - of which Isao saves ~25,000 against future obligations.  His truly-unconstrained spending is around ~2,900 koku per year, roughly 5.8x Governor Asuka's ~500 and ~48x Magistrate Hikai's ~60.

This is a substantial lifestyle by any standard, but it is the lifestyle of a serious working official, not a leisure-class noble.  The daimyo's discretionary income is dominated by obligations of the office rather than freely-spent wealth.  Even the ~2,900 koku of truly-free spending represents only ~4% of total discretionary income - the same proportion as Asuka's ~4-5% and Hikai's ~5%, scaled by tier.  By all accounts Isao is a steady, virtuous-but-not-exceptional daimyo: he meets his clan and Imperial obligations on time, manages the Reiji ministries competently, contributes the expected manpower and material to the Wall, and has cultivated his lineage chancellor and his fellow Crab daimyo well enough to maintain political stability for his household.  A more politically ambitious daimyo would invest more heavily in clan-level relationships and Imperial Court visibility (paid from personal savings, often dramatically reducing the lean-year reserve); a less scrupulous one could divert substantially more to personal use through reduced almsgiving, reduced Kaiu Wall contributions, or transactional appointments - any of which would quickly invite scrutiny from Hida Kisada or the Imperial magistrate stationed in the Reiji capital.

## The Imperial budget

The per-domain budget breakdowns documented in the sections above describe the financial operation of a single domain.  Above and parallel to those is the Imperial budget, by which the Emperor funds the structures and services that bind the Empire together as a whole.

### Imperial revenue (~34-36 million koku per year at baseline)

| Source | Annual koku |
| --- | --- |
| Land-output kick-ups (5% of land output Empire-wide; land output scales with farmland, so this aggregates on the ~400 basis) | ~12 million |
| Otosan Uchi tax base (property + business taxes from the capital's ~1 million urban inhabitants - merchants, artisans, administrators, soldiers, servants) | ~7-8 million |
| Otosan Uchi import tariffs (taken at the city gates and harbors at the 5% baseline rate) | ~1.5-2 million |
| Imperial-Family direct domain taxes (only the Hantei's own ~2 median-domain personal holdings outside Otosan Uchi, taxed at the full daimyo tier; the Seppun/Otomo/Miya 5% kick-up is already inside the land-output line above, so it is not re-counted here) | ~0.5 million |
| Imperial tariff cut on cross-domain commerce (5% of declared sales value at every provincial-city and capital-city gate Empire-wide, per the standard rate structure; the ~2,400 provincial-city gates aggregate × 400 and the ~284 capital gates × 284, against ~312,000 provincial + ~233,000 capital koku of median-domain trade volume) | ~9-10 million |
| Imperial salt monopoly cuts | ~3 million |
| Minor Imperial revenue (specific mining royalties, miscellaneous) | ~1 million |
| **Total** | **~34-36 million** |

**Note on the Otosan Uchi tax base**: The residence (property) component of this line is not, strictly, a tax.  Samurai pay no property tax - levying the warrior caste's residences would be unthinkable - so residence assessments in the capital are collected by the governors of the city districts as customary **gifts** rather than taxes.  There is no legal mechanism to compel a gift, but withholding one is socially unthinkable, and these residence "taxes" on Otosan Uchi real estate barely move from year to year; the line's variance comes almost entirely from the business component, which rises and falls with the capital's commerce.

The **Imperial-Family direct domain taxes** line is small, and counts only the Hantei's own land.  The Seppun, Otomo, and Miya hold and administer their own domains and run their own household budgets exactly as clan Families do - they are wealthy in part because they pay no clan-level kick-up, and only the Seppun are large enough to have vassal houses paying them a Family kick-up - but the Emperor's *direct* take from them is just the standard 5% Imperial land-output kick-up, which is **already inside the ~12M land-output line above** (that line is 5% of *all* Empire land output, the Imperial Families' 9 domains included).  Counting their lands again here would double-count them.  What remains is the Hantei's own personal holdings outside Otosan Uchi - about 2 median domains' worth of land - feeding the treasury at the full daimyo tier, ~0.5M.

This is a tiny fraction of Imperial income, yet ~0.5M is disproportionately large for only ~2 median domains of land, for two reasons.  First, the land is **unusually fertile** - the capital sits where it does precisely because of it - so each domain yields well above the median.  Second, the Hantei command an **unusually large labor pool to work it**: fallow-land reclamation is far easier beside a million-person city, where surplus urban laborers can be relocated onto newly opened fields around the capital in numbers no median domain could supply from its comparably small capital town.  (The Hantei's own 5% layer is technically inside the ~12M line too, but that small overlap is deliberately left in - the fertility-and-labor premium more than absorbs it.)

**Note on year-to-year variance**: The ranges above are decade-scale bands, not the swing in a typical year, and they overstate that swing in two ways.  First, a large fixed core does not move with the harvest: the land-output kick-ups (~12M) and the Hantei direct domain taxes are assessed against the *kokudaka*, which does not fall in a bad year (the burden lands on the peasantry, not the assessment), and urban property tax is similarly stable.  Second, the variable trade lines do not trough in the same year, so summing each line's low (or each line's high) double-counts uncorrelated variation that never lands in a single year.  In normal years total revenue therefore clusters near the middle of the band (~35M); the extremes are reached only by once-in-a-generation shocks like the Lion/Crane War, which suppressed capital trade and several tariff lines at once, in addition to the corresponding increase in expenses caused by such unrest.

**Note on the Otosan Uchi tariff rate**: the 5% Imperial floor is the rate the Emperor *always* collects at Otosan Uchi gates (it is the Imperial cut from the standard rate structure that applies Empire-wide).  Above this floor, the Emperor has discretion to increase Otosan Uchi tariffs, raising the effective rate at the Imperial capital above the 5% baseline.  Such elevations are rare and politically sensitive (OU merchant houses lobby vigorously against them, and excessive rates would discourage commerce into the capital), but they have occurred.  At the time of the current campaign, sustained fiscal pressure has forced the Emperor to raise Otosan Uchi tariffs incrementally to approximately 15% (10 points above the floor), adding roughly ~2-3 million koku/year above the baseline figure shown in the table.  Even this elevation has not been sufficient to fully offset the recent multi-year drawdown of Imperial reserves; see the Imperial Savings section below for the campaign-current fiscal context.

Note that the 5% from each domain is calculated against the domain's assessed land output (the *kokudaka*), not against the much smaller figure of taxes actually collected.  Since the daimyo collects 1/3 of that assessed output as land tax, the 5% Imperial cut works out to ~15% of the daimyo's land-tax revenue.  This is documented per the Wakashi example in [l7r.md - The Ministry of Revenue](l7r.md#the-ministry-of-revenue).

The Imperial **salt monopoly** is regional rather than universal: the Crown takes a direct cut from salt production in coastal salt-pan regions (most prominently along Earthquake Bay in Crab lands, the Daikoku Strait, and the Phoenix coast) and from inland brine-well operations in certain Lion and Dragon provinces.  Other salt production - household salt-boiling for local use, small-scale rock-salt mining in mountain regions, the smaller coastal salt operations - is taxed at the domain level through the normal business license system rather than reserved to the Crown.  At its Tang peak an imperial Chinese salt monopoly could account for around half of central revenue, rising to as much as two-thirds under the Song; Rokugan's lighter-touch implementation at roughly 8-9% of Imperial revenue reflects both the Empire's general preference for distributed rather than centralized monopolies (consistent with the tax-farming pattern documented throughout these notes) and the practical difficulty of suppressing illicit production in such a large and varied geography.  The Imperial Treasurer's office maintains a standing investigative unit dedicated to salt-smuggling cases, which has historically been one of the more dramatic-but-modest profit centers within the broader Imperial Ministry of Revenue operation.

The Emperor does **not** collect road tolls anywhere in the Empire.  All tolls on the Imperial road network were outlawed by Hantei the Tenth, with consequences explained below.

### Imperial spending (~30-31 million koku per year)

| Category | Annual koku | Notes |
| --- | --- | --- |
| Imperial household and Imperial Family | ~1.5 million | Emperor's personal household + Imperial Consorts and their establishments + Imperial Princes and Princesses + Empresses Dowager + retired Emperors + the chamberlain/eunuch staff that runs the inner palace.  Distinct from the Imperial Ministries below; this is the Emperor's personal/dynastic establishment, not the central bureaucracy |
| Otosan Uchi local government and administration | ~1.5 million | The mayoral-equivalent functions for the capital's ~1 million inhabitants: magistrates, policing, local market regulation, local public works above what corvee and the Imperial Ministry of Works handle directly, the local granary infrastructure (see the Imperial Ministry of Justice line below for the standard per-domain granary model; OU's granaries are vastly larger because of population concentration) |
| Imperial Ministry of Works | ~15-17 million | The Imperial Ministry of Works oversees all Imperial public works at scale, including two enormous strategic programs that account for the bulk of its budget.  Breakdown: **Imperial roads and waystations ~10-11 million** (the ~50,000-mile road network plus ~5,000 waystations; detailed breakdown in its own section below); **Kaiu Wall direct contributions ~4 million** (Imperial-funded Wall maintenance and supplies above and beyond what the Crab Clan funds autonomously; detailed breakdown in its own section below); **central operations ~1.5 million** (Imperial palace maintenance and construction, granary infrastructure design and supervision, sacred construction at major Imperial shrines, local aqueducts and harbors, Imperial public-works engineering and capital projects) |
| Imperial Ministry of War | ~3 million | The Imperial Ministry of War oversees the Empire's central standing army and the supporting strategic functions.  Breakdown: **Imperial legions ~2 million** (the standing 25 legions of ~1,000 legionnaires each, the great majority Wall-stationed at ~75K with a handful on border, ceremonial, or emergency duty; this is the stable peacetime figure - a major war both field-deploys legions and raises additional ones, driving the War line toward ~6-7M, see the detailed breakdown in its own section below); **central operations ~1 million** (Imperial-level war command, weapon manufacture oversight, war horse breeding programs, strategic intelligence on clan military capacity, mobilization planning, and strategic-reserve readiness) |
| Imperial Ministry of Rites | ~2 million | State ceremonies, sacred construction, mourning observances, Empire-wide religious infrastructure, festival distributions.  The Imperial-level state religion: major Imperial shrines (especially Amaterasu's), Imperial-rank shugenja stipends, ceremonial costs for major Imperial events, Empire-wide festival coordination, supervision of major mourning periods (see Imperial Savings below for the fiscal mechanics of large mourning-period distributions) |
| Imperial Ministry of Justice | ~4 million | The Imperial Ministry of Justice oversees the Empire's central judicial functions plus the field-level Imperial Magistrate cohort.  Breakdown: **Imperial Magistrates and their staff ~3.6 million** (one Imperial Magistrate per domain per the Emerald Charter, plus "the Yasuki Taka system" tariff-audit yoriki cohort and the local Imperial granary oversight role; detailed breakdown in its own section below); **central operations ~0.5 million** (Otosan Uchi resident judicial machinery, Emerald Champion's central staff, central judicial review, prisoner transport at the Imperial level) |
| Imperial Ministry of Retainers | ~1.5 million | Imperial-rank samurai stipends and the central retainer-administration apparatus.  Stipends for Imperial-rank samurai serving in Imperial posts (Imperial princes who hold formal offices, Imperial-Family officials, ceremonial-court samurai, samurai seconded to Imperial duty from clan Families *outside* of the Imperial legions structure - the legions are funded under the Imperial Ministry of War line above); rank-squared stipend calculations and payment-day logistics; the Imperial-level civil service examination administration |
| Imperial Ministry of Revenue | ~1 million | Empire-wide tax collection oversight, salt monopoly administration, commercial regulation, Imperial Court financial administration (the Imperial Treasurer's office), liaison with the 284 Imperial Magistrates' tax-related functions |
| **Total operating spending** | **~30-31 million** | The Imperial Chancellery (a deliberative body that advises the Emperor and ratifies major decisions; see [l7r.md - The Ministry of Justice](l7r.md#the-ministry-of-justice) for its political role) is not a separate line because its operating cost is minimal and is folded into the Imperial Ministry of Retainers and Imperial household lines |

In a normal year this operating spending runs against revenue of ~34-36M, leaving **~4-5M koku that flows into Imperial savings**.  That surplus is the system's shock absorber and the engine of the Empire's reserve-building: larger in a good year, smaller in a lean one, and reversing outright in a war or mourning year, when the Emperor draws down the accumulated reserves instead of adding to them.

**Note on year-to-year variance**: As on the revenue side, these are normal-decade operating figures, not a measure of annual swing.  Imperial operating costs are overwhelmingly fixed - salaries, garrisons, standing offices, and infrastructure upkeep barely move year to year - so the spending side is steady and the savings line absorbs almost all the variance.  The table deliberately **excludes the once-in-a-generation shocks** behind the current crisis: a war year pushes the legions alone toward ~6-7M and piles on magistrate interventions, supply disruption, and famine relief, while an extended Imperial mourning can add millions in grain distributions.  It was many of these arriving together that drained the reserves, i.e. the long mourning for Hantei the XXXVIII's mother followed by a massive harbor rennovation project in Otosan Uchi prior to preventing a Crab/Scorpion war before the actual Lion/Crane and Lion/Unicorn wars.  In a normal decade the books balance with the surplus above, with famine relief and tax forgiveness happening at a local scale spending down these numbers on an irregular basis as needed.  (The per-program detail sections below carry the fuller picture - the legions climbing from their ~3M peacetime baseline toward ~6-7M in a major war, ~3-4M for the magistrates, etc - while the table shows the normal-decade operating figure.)

### Imperial budget scale: historical context

The Imperial Budget figures above warrant explicit historical grounding, because the scale of Imperial fiscal extraction varies enormously across premodern empires and the Rokugani case is structurally important to understand.  Comparing per-capita central revenue across major historical examples:

| State | Population | Central revenue (grain-equivalent) | Per capita |
| --- | --- | --- | --- |
| Han China at its census peak (2 CE) | ~60 million | ~40-50 million *shi* | ~0.7-0.8 *shi*/person |
| Tang China at Xuanzong's peak (~750 CE) | ~50-60 million | ~60-80 million *shi* | ~1.0-1.4 *shi*/person |
| Northern Song China (~1100) | ~100 million | ~60-100 million *shi* | ~0.6-1.0 *shi*/person |
| Ming China at peak (~1500-1600) | ~150-200 million | ~50-70 million *shi* | ~0.3-0.4 *shi*/person |
| Qing China Yongzheng/Qianlong era (~1730-1790) | ~300-400 million | ~70-100 million *shi*-equivalent | ~0.2-0.3 *shi*/person |
| Tokugawa Japan at peak (*bakufu* central revenue only) | ~30 million | ~4 million koku (*tenryo* only) | ~0.13 koku/person |
| **Rokugan under this framework** | **~100 million** | **~30 million koku** | **~0.30 koku/person** |

These per-capita figures are deliberately rough, order-of-magnitude estimates.  Premodern central-revenue totals are contested and hard to compare, because different regimes collected in grain, cloth, cash, and labor service in different proportions, and surviving figures often blur the line between grain tax alone and total multi-form state revenue.  The Han and especially the Tang entries here sit toward the high end of the plausible range (the Tang total in particular is sensitive to that grain-versus-total ambiguity), so the table is meant to fix the *relative ordering* of central fiscal capacity rather than precise values.  That ordering is robust regardless of where the true numbers fall within these ranges: Rokugan sits near Ming at face value (and a touch above it once the smaller Chinese *shi* is converted to koku), below the Tang/Song peak, and well above Tokugawa.

**Why the *shi*/koku mix still works**: the table reports each state in its own grain unit, and those units differ in size - the koku (~180 litres) is roughly two to three times a Chinese *shi*/*dan* (~59 litres in the Tang, ~100 in the late dynasties, and never a fixed quantity; see [Historical units](#historical-units) below).  Read as raw magnitudes the *shi* rows would overstate Chinese revenue against the koku rows.  What makes the comparison hold is that per-capita grain revenue stands in for *the share of one person's annual food the central state commands*, and a person's yearly grain is about 3.33 *shi* or, equivalently, ~1.5 koku - so once the figures are read as consumption-shares rather than bare numbers, the units reconcile and the ordering is sound.  Tokugawa Japan is the one line already in koku, a clean like-for-like anchor against Rokugan.  The residual bias is conservative toward Rokugan: expressing the Chinese rows in koku would shrink them, raising Rokugan's relative standing rather than lowering it.

Rokugan's Imperial center extracts roughly as much per capita as the Ming dynasty did - a touch more, once the Chinese figures are converted from *shi* into koku - significantly less than the Tang/Song peak (when the Chinese central state was at its strongest fiscal capacity), significantly more than the Tokugawa shogunate (which was historically a weak central state by deliberate structural design - the daimyo system delegated most fiscal capacity to clan domains rather than centralizing it).

This is a deliberate worldbuilding match.  Rokugan is structurally more like Ming China than like Tang/Song China: the 7 Great Clans absorb fiscal capacity that in the strongly-centralized Tang/Song models would have flowed to the central treasury.  Substantial portions of what would otherwise be central revenue stay at the clan tier - clan-level kick-ups from Family/house revenue, clan-level military formations like the Crab Wall force, clan-level Magistrates running internal disputes, clan-level commerce regulation through the Family chancelleries - rather than flowing to Otosan Uchi.  Aggregating across all clans, the 7 Great Clans' combined fiscal capacity (sum of daimyo discretionary across ~284 domains + lower-tier kept money + clan-level treasury operations) probably runs ~50-80 million koku/year, exceeding the Imperial Court's ~30 million by a significant margin.  The Empire is thus a **fiscal duopoly** between Imperial Court and clan aggregate, with the central state being smaller than the regional aggregate.

This is structurally similar to late Heian / early Kamakura Japan in shape, though at a vastly larger scale and with the Imperial Court retaining substantially more actual fiscal capacity than the Heian-period emperor did.  It also matches the broader L7R framing of Rokugan as "samurai culture on a Chinese scale" - the bureaucratic structures and physical infrastructure are Sino-imperial in scope, but the political-fiscal structure preserves substantial regional autonomy in the clan system, which is more feudal than Sinic.

The total tax extraction rate observable to a Rokugani peasant - the 1/3 land tax to the daimyo, plus the kick-up cascade that follows - is moderate to high by historical premodern standards, similar to mid-Tokugawa Japan and somewhat higher than the Tang/Song Chinese norm.  But the proportion of this extraction that reaches the Imperial center (~15% of land tax revenue under the 5% land-output kick-up structure) is much lower than equivalent Tang/Song-era Chinese central extraction (often 25-50% of regional tax revenue at peak).  This is essentially the structural cost of running samurai feudalism across a China-sized land area: the multi-tier extraction cascade (peasant -> magistrate -> governor -> daimyo -> Family + Clan + Imperial) means that more total extraction is required to deliver the same revenue to the central treasury than would be true under a more centralized Tang/Song-style two-tier model (peasant -> provincial governor -> Imperial center).  The clan-feudal layers absorb a disproportionate share of what gets extracted, leaving the Imperial center fiscally weaker than a comparably-sized centralized empire would expect to be.

The practical implication for campaign play: significant Imperial policy questions can be re-litigated when an Emperor weakens or a clan strengthens.  The relationship between Imperial Court and the 7 clans is a live, evolving fiscal-political balance, not a settled hierarchy.  Hard fiscal pressure on the Imperial Court (a depleted treasury, an unusually expensive Wall campaign, a succession crisis with large discretionary outlays) is something the clans can sometimes exploit; conversely, a strong Emperor with full reserves can push back against clan autonomy in ways that a fiscally stressed Emperor cannot.

### Imperial roads and waystations: line-item detail

The ~10-11 million koku/year for the Imperial road network breaks down roughly as follows:

- **Road surface maintenance** (~4 million): Cash costs for materials, specialized labor (stone-cutting, bridge work, mountain-pass engineering), supervision, and emergency repairs after floods or landslides.  Average cash spend is ~80 koku/mile/year, reflecting the network's deliberately heavy maintenance standard.  The bulk of actual repair labor is provided through **corvee obligations** on counties adjacent to the road network (per [l7r.md - The Ministry of Works](l7r.md#the-ministry-of-works)), which is why the cash component is far smaller than the engineering scope would otherwise suggest.

- **corvee laborer rations and household stipends** (~1-2 million): The bulk of the unskilled repair labor is corvee (above), but the Crown - unusually for a premodern state - feeds those laborers throughout their term of service and pays a deliberately generous grain stipend, drawn from the Imperial granaries in each domain rather than in cash.  The stipend is pitched above the bare value of the laborer's own time, on the principle that conscription pulls a farmer away from the fields that feed not just the worker but the worker's whole household; it is meant to keep that household whole during the absence, not merely to pay for the labor.  It runs toward the high end in lean years, when the household relief matters most.  The Crown bears it directly rather than leaving it to the domains, for the reasons given in [Imperial roads: a special case](#imperial-roads-a-special-case) below.

- **Waystation operations** (~3.7 million): Approximately ~5,000 waystations across the ~50,000-mile network, spaced at irregular but worthwhile intervals averaging ~10 miles apart but varying substantially by route conditions.  On the most important and well-traveled stretches (the main trunks connecting Otosan Uchi to the Great Clan capitals, the heavily-populated route through central Crane lands, dangerous segments where bandit incidents have been historically frequent) waystations are spaced as close as every ~5 miles.  In remote frontier regions (parts of Unicorn lands well west of Shiro Iuchi, sections of the Kuni Wastelands road network, far northern Phoenix routes through the cold mountains) the spacing stretches to ~20-30 miles - these are routes where it is a full day's journey between waystations, and travel preparations are correspondingly more serious.  Each waystation costs the Imperial budget ~560-1,400 koku/year to operate (typical ~700; see the Per-Waystation detail below), plus a small clan-paid stipend burden (~50 koku/year, for the locally-detailed clan samurai) borne by the host domain rather than the Crown.  Each supports a permanent staff of ~10-30 people: relay-master, courier-postmaster, mounted patrol detachment, stable hands, road-maintenance crew billeted there, kitchen and provisioning staff, and waystation-attached Imperial yoriki assigned to "the Yasuki Taka system" transit-stamp verification (distinct from the city-gate yoriki cohort attached to the Imperial Magistrate offices).

- **Specialized engineering infrastructure** (~850K): Bridges across major rivers, tunnel-pass maintenance, mountain-pass shelter facilities, ferry stations.  Roughly 50-100 major engineered structures Empire-wide.

- **Mounted Imperial courier service** (~450K): The ~500-1,000 trained mounted couriers themselves, above and beyond the waystation base operations.  Significant horse-replacement and tack-equipment costs.

**Why waystations exist at all (since Rokugan does not collect tolls)**: the network supports six distinct functions apart from toll collection (which Rokugan rejects).  Without tolls, waystations still support: (1) Imperial courier relay, the central government's nervous system, allowing orders from Otosan Uchi to reach distant frontier domains in days rather than weeks; (2) mounted anti-banditry patrols on the road segments between stations; (3) military logistics for Imperial legions in transit; (4) civilian hospitality and overnight safety for commoner travelers; (5) billeting for road-maintenance crews; (6) transit-stamp verification, the audit-side companion to the no-transit-tariffs policy (see [l7r.md - The Ministry of Revenue](l7r.md#the-ministry-of-revenue) for the tariff-audit detail).

**Historical justification**: The Tang Chinese *yi* (驛) post system spaced stations every ~10 miles for these same functions, with no toll collection, at a cost of roughly 8-12% of Tang central revenue at peak.  Rokugan at ~30% of Imperial revenue is HIGH by Tang standards, but this is the deliberate worldbuilding choice that the [Imperial roads: a special case](#imperial-roads-a-special-case) subsection below explains - Hantei the Tenth committed to an unusually intense road investment, and the figures reflect that commitment rather than the historical average expenditure.

The same institution recurs across the premodern world, and the waystation here borrows from all of it.  Japan took the Chinese model directly: the *ritsuryō*-era *eki* (駅) relay stations, spaced along the highways with state relay-horses and a station-master, and later the Edo *shukuba* (宿場) post-towns that added lodging, porters, and service to travelers and daimyo alike, with *sekisho* (関所) barrier checkpoints performing the travel-permit function the transit-stamp verification mirrors.  The closest structural analog is the Roman *cursus publicus*: its *mutationes* (horse-change posts every ~12-18 km) map onto the typical waystations and its *mansiones* (day's-travel rest stops) onto the busy trunk ones; it was permit-gated by an imperial warrant - the *diploma* or *evectio*, the very model of the transit stamp - it ran on a provisioning burden laid on the communities along the route (the *angareia*, the direct parallel to the corvee-and-clan-provisioning arrangement here), and it collected no tolls on the road itself, taking its customs (*portoria*) at boundaries and ports the way Rokugan takes its tariffs at city gates.  The one element more generous than the historical norm is the open hospitality to commoner travelers: the *yi* and the *cursus publicus* were official-use-only, and even the *shukuba* served travelers as paid inns rather than free Imperial shelter - so that function is the rosy, well-run-Rokugan end of the comparison rather than the historical norm.

#### Per-waystation staffing breakdown

A typical waystation supports ~15-20 permanent staff.  Most positions are locally sourced - hard oversight (transit-stamp verification, station command) requires Imperial appointees from elsewhere, but the broader administrative and physical work is done by locals.  Composition and stipend breakdown, with funding source noted:

| Role | Count | Status / Rank | Stipend (koku/yr) | Total (koku/yr) | Paid by |
| --- | --- | --- | --- | --- | --- |
| Relay-master (senior samurai who manages the station; Imperial appointee from elsewhere, rotates periodically) | 1 | Rank 5 samurai | 25 | 25 | Imperial budget |
| Waystation Imperial yoriki (transit-stamp verification, Imperial appointee from elsewhere, attached to the Imperial Magistrate of the domain the station sits in) | 1 | Rank 4 samurai | 16 | 16 | Imperial budget |
| Foot-patrol and station-guard ashigaru (locally recruited) | ~4 | Ashigaru (peasant light infantry) | 2 each | ~8 | Imperial budget |
| Stable hands (locally recruited) | ~3 | Peasants (housed + fed + small stipend) | ~1 | ~3 | Imperial budget |
| Kitchen and provisioning staff (locally recruited) | ~2 | Peasants (housed + fed + small stipend) | ~1 | ~2 | Imperial budget |
| Road-maintenance crew specialists (locally recruited; supervise corvee labor and do specialized stonework) | ~2 | Peasants with skilled-craft status | ~2 | ~4 | Imperial budget |
| Courier-postmaster (handles incoming/outgoing couriers and mail; clan samurai detailed by the local daimyo to assist Imperial functions) | 1 | Rank 4 samurai | 16 | 16 | Local clan budget |
| Mounted patrol leader (clan samurai detailed by the local daimyo) | 1 | Rank 4 samurai | 16 | 16 | Local clan budget |
| Manifest clerk / scribe (clan samurai detailed by the local daimyo) | 1 | Rank 3 samurai | 9 | 9 | Local clan budget |
| **Total** | **~16** | | | **~99** | |

**Note on ashigaru**: in Rokugan, ashigaru are peasants, not samurai - the original L5R usage, which departs from historical Japan, where ashigaru formed the lowest stratum of the samurai class.  As peasant light infantry they serve on foot: a waystation's ashigaru patrol the immediate road and guard the station, while its mounted element - the samurai patrol leader and the trained mounted couriers - carries the longer-range anti-banditry patrols.  Conscripted farmers neither owned horses nor trained to fight mounted, so the cavalry role falls to the warrior caste throughout these notes.

The local/Imperial split is due to oversight requirements, i.e. the yoriki function specifically cannot be entrusted to locals because of the structural conflict of interest - the daimyo's own samurai cannot be trusted to audit imports flowing into the daimyo's own city.  However, the broader administrative apparatus (couriers, mounted patrols, manifest record-keeping) can be done by local clan samurai working under the Imperial relay-master's command, which is cheaper and uses local knowledge while preserving Imperial oversight where it matters.

Funding split:
- Imperial-paid personnel (relay-master + yoriki + all ashigaru/peasants): ~58 koku in stipends + ~10 koku in allowances = ~68 koku/year per waystation
- Clan-paid personnel (3 local samurai detailed by the daimyo): ~41 koku in stipends + ~9 koku in allowances = ~50 koku/year per waystation, borne by the host domain's clan budget

#### Single waystation budget reference

A typical waystation's annual Imperial budget breaks down as follows (clan-paid samurai stipends are NOT included here - they appear in the host domain's clan budget):

| Category | Annual koku | Notes |
| --- | --- | --- |
| Imperial-paid personnel stipends and allowances | ~70 | Relay-master + waystation yoriki + locally-recruited ashigaru and peasants.  See the staffing breakdown table above |
| Horses and stable operations | ~60 | ~8-10 horses average, scaling with the station's courier traffic (mostly relay mounts for couriers swapping tired horses for fresh, plus officer and patrol mounts for the station's samurai); includes fodder, tack, replacement |
| Building maintenance and repairs | ~150 | Structural upkeep of the waystation complex (main hall, barracks, stables, gates, courtyard walls) |
| Road repair materials for the adjacent ~10 miles of road | ~200 | Stone, lumber, specialized tools, materials for bridge and culvert maintenance.  The bulk of actual road-repair LABOR comes from corvee obligations on adjacent counties; this budget line covers materials and the wages of the skilled-craft specialists who supervise the corvee crews and do specialized stonework |
| Daily consumables | ~100 | Lamp oil, firewood, food preservation, kitchen consumables, daily operations of housing and feeding ~16 staff plus transient travelers (couriers passing through, the occasional inspecting magistrate, civilian travelers overnighting) |
| Manifest paper, sealing wax, courier equipment, transit-stamp supplies | ~50 | For courier-relay record-keeping and transit-stamp verification work |
| Medical supplies, religious offerings, ad-hoc costs | ~70 | Basic medical supplies, small altar maintenance, irregular operational costs |
| **Total per typical waystation (Imperial budget)** | **~700** | |

The local daimyo additionally pays ~50 koku/year per waystation in stipends for the 3 clan samurai detailed as courier-postmaster, mounted patrol leader, and manifest clerk.  Across all the waystations within a typical Reiji-style domain (see the per-domain synthesis below), this comes to a few hundred koku of clan budget burden - a trivial obligation in absolute terms but a continuing structural reminder that the domain participates in supporting Imperial infrastructure.

Variation by waystation type (Imperial budget figures, excluding clan-paid samurai stipends):

- **Remote frontier waystations** (~560 koku/year): Fewer staff (~10), fewer horses, less road traffic, lower building-maintenance needs.  Found in places like deep Unicorn lands well west of Shiro Iuchi, northern Phoenix mountain routes, parts of the Kuni Wastelands road network, etc.
- **Typical mid-route waystations** (~700 koku/year): The standard model documented above.  Represent the majority of stations.
- **Busy trunk-route or junction waystations** (~1,400 koku/year): Larger staff (~25-30) including a smith for shoeing horses and weapon maintenance, additional clerks for heavier manifest volume, more horses, dual-function as relay points where major routes intersect, occasional hosting of ceremonial Imperial travelers.  Found on the main Otosan Uchi trunks, the central Crane corridor, and major route junctions throughout the Empire.

Empire-wide aggregation across ~5,000 waystations:

- ~1,000 remote × ~560 koku = ~560K
- ~3,500 typical × ~700 koku = ~2.45M
- ~500 busy × ~1,400 koku = ~700K
- **Total Imperial-paid: ~3.7 million koku/year**

This produces the ~3.7M waystation operations figure shown in the Imperial Roads and Waystations top-level breakdown above.  Plus an additional ~250K koku/year of clan-paid stipends for the ~15,000 locally-detailed clan samurai serving across all ~5,000 waystations (3 per waystation), spread across the 284 actual domains as a routine support-of-Imperial-infrastructure obligation.

### Imperial roads: a special case

The Empire's ~50,000-mile Imperial road network is an extraordinary investment for a premodern state.  Heavy maintenance, ~5,000 waystations staffed at irregular but worthwhile intervals (averaging ~10 miles apart on the major trunk routes, more sparsely on minor branches and frontier extensions), no tolls collected anywhere along the system - by historical standards this is dramatic over-investment, and most premodern road networks of comparable ambition either decayed for lack of maintenance funding (Imperial Rome's roads were essentially gone within a generation of the Western collapse) or fragmented into a patchwork of local tolls extracted by individual lords, towns, and barrier stations (medieval European roads, Sengoku Japanese *sekisho*, the various transit-tax stations of the late dynasties of imperial China).

The no-tolls policy itself is actually well-grounded in imperial Chinese fiscal best practice: Tang and Song administrators understood and explicitly argued the deadweight-loss principle, that tolls on a unified empire's main road network suppressed trade more than they generated revenue, and that any state with the central fiscal capacity to fund roads through general taxation should do so.  What is unusual about Rokugan is not the no-tolls choice itself - which any Tang or Song scholar-official would have endorsed - but the consistent multi-century maintenance of the underlying road investment that makes the no-tolls policy economically viable.  Most empires that initially banned tolls eventually drifted back toward toll systems when central fiscal capacity weakened (this was the trajectory of late Yuan and late Ming, and of the late Qing under the *likin* internal-customs system).  Rokugan's distinction is that the Imperial road investment has been sustained, not that the Imperial road tolls have been absent.

That sustained investment is what calls for explanation, and there are two of them.

First, the Empire has been blessed in certain reigns with Emperors who counted prophets of Daikoku, the Fortune of Wealth, among their close advisors.  Such prophets do not understand modern economic principles or supply-and-demand curves, but their attunement to Daikoku grants them direct insight into the consequences of fiscal decisions across spans of time no ordinary planner could reason about.  Hantei the Tenth, in particular, was advised by such a prophet when he made the foundational decisions: the elimination of all tolls anywhere on the Imperial road network, and (more critically) the establishment of a permanent Imperial commitment to ongoing road maintenance funded from the central treasury.  The no-tolls choice was within the realm of normal Imperial bureaucratic reasoning - several previous Emperors had reduced toll systems, citing the same trade-suppression arguments familiar from Tang and Song administrative practice - but the commitment to *permanent and substantial* central funding for maintenance was the harder choice, and the one ordinary planners would have been reluctant to make in any given fiscal year.  The prophet's vision was that this investment would pay for itself many times over in the centuries that followed, through commerce that would not otherwise have been possible, regional integration that would prevent or end wars, and stability that would let the Empire prosper in ways otherwise unreachable.

A specific and historically unusual feature of the Hantei commitment is that the Crown takes direct responsibility for **feeding and compensating the corvee laborers** who do the bulk of the actual repair work.  In most premodern systems conscripted labor was uncompensated and self-provisioned - it was simply incumbent on a peasant household to keep its conscripted members alive, which in lean years was a serious and sometimes fatal hardship that bred resentment.  Earlier in Rokugan's history this was the system too, and it produced exactly that result: in hard years local governments, not sharing the Emperor's (correct) appraisal of the roads' long-term value, were tempted both to let maintenance lapse and to raise corvee laborers with no offered provisions, and the resulting unrest was a recurring problem.  The Hantei response was to centralize it - the Crown now feeds corvee laborers throughout their service and provides a modest grain stipend, drawn from the Imperial granaries distributed across the domains rather than paid in cash, to support the households they leave behind.  The domains are *not* compensated for the use of their peasants - that labor is part of the domain's standing obligation to the Emperor - but the laborers themselves are provisioned by the Crown, which both removes the lean-year hardship and removes the local temptation to neglect the roads.  This is more considerate of the peasantry than most historical premodern states managed, but it is not without precedent: well-run Chinese dynasties at their height moved toward provisioning or outright paying their labor levies rather than relying on unprovisioned conscription - most notably the Song, whose *muyi* (募役, "hired service") reforms replaced unpaid corvee with state-funded paid labor on public works.  It is of a piece with Rokugan's portrayal as an unusually just and well-administered society.

This brings us to the second explanation for this system, which is a Doyalist reason which the in-fiction characters do not articulate but the worldbuilding consciously enacts: **Rokugan is the kind of world that real historical premodern populations believed themselves to be living in**, even when their actual governments fell short.  Thus, Rokugan is portrayed as enacting the historical ideals of rule of law and the justice of heaven to a degree that real-world historical equivalents rarely achieved.  When PCs pass by a farming village, they are not participating in a system that is literally starving those inhabitants - they are taking part in a society that, by premodern standards, governs unusually well.  The well-maintained road network with forward-thinking policies to prevent peasant unrest through fair compensation is an example of this working in practice.

The Yasuki Taka import tariff system (see [l7r.md - The Ministry of Revenue](l7r.md#the-ministry-of-revenue)) provides the necessary fiscal counterbalance: city gates collect tariffs that generate substantial revenue from commerce, while roads themselves remain free for any traveler, preserving the conditions for the commerce to occur in the first place.

### Imperial legions: line-item detail

The Imperial legions are the Empire's central standing army.  In peacetime the Empire maintains a fixed, stable **25 legions** of ~1,000 legionnaires each (~25,000 active combat troops), supported by a substantially larger cohort of non-combatant peasant support staff.  This count is deliberately written as **25, not ~25**: unlike most figures in this document it is a real and stable number, held constant by long Imperial practice rather than estimated, and it does not drift from year to year.  Additional legions are raised only under exceptional circumstances (e.g. a period of intense Shadowlands activity or a major clan war) and are stood down again once the emergency passes (see the Lion/Crane War context below).  The standing 25 cost the Imperial treasury ~3M koku/year (the cost breakdown follows).

**Every legionnaire is a samurai** - the ~1,000 combat troops in a legion are samurai drawn from the clans (with senior command from the Imperial Families, especially the Seppun), carrying the rank-squared stipends shown below.  The much larger support tail (cooks, smiths, porters, animal handlers, etc) is entirely peasant, per the tooth-to-tail discussion further down.  Most legions are stationed on the Kaiu Wall assisting the Crab Clan, with a small handful stationed at other posts (most famously: the 1st Imperial legion at the Gateway to the Land of the Burning Sands, and the 2nd Imperial legion at Beiden pass).

#### Legion organization and rank structure

Each Imperial Legion is organized into a hierarchy that maps directly onto the rank-squared stipend system:

| Unit | Composition | Commander | Commander's Rank | Stipend (koku/yr) |
| --- | --- | --- | --- | --- |
| Platoon | ~15-20 legionnaires | Platoon lieutenant | Rank 6 | 36 |
| Company | ~3 platoons (~50 legionnaires) | Company captain | Rank 7 | 49 |
| Battalion | ~4-5 companies (~200-250 legionnaires) | Battalion commander | Rank 8 | 64 |
| Legion | ~5 battalions (~1,000 legionnaires) | Legion general | Rank 9 | 81 |
| Army | Multiple legions in a theater section (e.g. all legions along one stretch of the Kaiu Wall) | Army general | Rank 10 | 100 |
| Theater | Multiple armies (e.g. all legions along the entire Kaiu Wall) | "General of the X Armies of the Y" | Rank 11 | 121 |

The Imperial appointee in charge of all legions along the Kaiu Wall holds the title **General of the Border Armies of the Emperor** (Rank 11).  Theater commanders for other strategic groupings carry analogous titles.

Within each platoon, the standard composition is: 1 platoon lieutenant (Rank 6, 36 koku), ~3 squad sergeants (Rank 5, 25 koku each), ~3 corporals (Rank 4, 16 koku each), and ~9-13 rank-and-file legionnaires (Rank 3 by default, 9 koku each).  Rank-and-file legionnaires can be demoted to Rank 2 (4 koku) for misconduct, but no Imperial legionnaire is ever demoted to Rank 1 - that lowest rank is incompatible with the prestige of Imperial service, and no samurai who has earned a place in the legions could be reduced to it without an extraordinary act of dishonor which would likely result in expulsion from the legion and possibly execution or seppuku.

#### The rank uplift principle

Imperial Legion postings are administratively reckoned **one rank higher** than equivalent posts in clan armies.  A squad sergeant in a clan army would normally be a Rank 4 posting; in the Imperial Legions, it is Rank 5.  This applies systematically up and down the structure: a platoon lieutenant who would be Rank 5 in clan service is Rank 6 in Imperial service; a legion general is Rank 9 rather than the Rank 8 they would be at a comparable clan-army post.

The rank uplift is a structural feature of Imperial Legion service, not a discretionary honor.  It reflects the prestige of serving the Emperor directly, and it has two important consequences:

1. **The stipend bump while serving**: under the rank-squared stipend rule, the uplift increases compensation meaningfully.  A squad sergeant goes from 16 koku (Rank 4) to 25 koku (Rank 5), a 56% increase.  A legion general goes from 64 koku (Rank 8) to 81 koku (Rank 9), a 27% increase.  Across an entire legion, the rank uplift is a substantial cost borne by the Imperial Treasury.

2. **The retention of rank after Imperial service**: when a samurai's Imperial Legion assignment ends and they return to their clan, **they keep the higher rank**.  A sergeant who served at Rank 5 in the Imperial Legions returns to their clan as a Rank 5 samurai; their daimyo cannot retroactively demote them to Rank 4 without explicitly insulting them.  The logic is straightforward: to give a returning Imperial veteran a lower-ranking post would be to say they were good enough to serve the Emperor at their elevated rank but not good enough to serve their daimyo at the same rank, which is unacceptable to both the returning veteran and to the Imperial system that elevated them in the first place.  Demotion is only possible if the samurai is deemed to have personally and individually embarrassed themselves to a degree that warrants explicit punishment - and such embarrassments are public, well-documented, and rare, not silent reversions to clan-army ranks.

This rank-retention rule creates a sustained incentive for daimyo to second their samurai to Imperial Legion duty: the Empire pays the elevated stipend during service, and when the samurai returns, the daimyo has a higher-ranking retainer at no additional clan cost (the daimyo now pays the higher stipend in clan service, but receives a more experienced and Imperially-vetted official in exchange).  This is the structural reason why daimyo happily fulfill their obligation to contribute manpower to the Imperial Legions despite the temporary loss of their retainers' service, and are not inclined to lobby against or otherwise resist this part of the Imperial system.

#### Per-legion stipend breakdown

A typical Imperial Legion of ~1,000 legionnaires has the following annual stipend cost, broken down by rank:

| Rank | Position | Count | Stipend (koku/yr) | Total (koku/yr) |
| --- | --- | --- | --- | --- |
| Rank 9 | Legion general | 1 | 81 | 81 |
| Rank 8 | Battalion commander | ~5 | 64 | ~320 |
| Rank 7 | Company captain | ~20 | 49 | ~980 |
| Rank 6 | Platoon lieutenant | ~60 | 36 | ~2,160 |
| Rank 5 | Squad sergeant | ~180 | 25 | ~4,500 |
| Rank 4 | Corporal | ~180 | 16 | ~2,880 |
| Rank 3 | Rank-and-file legionnaire | ~570 | 9 | ~5,130 |
| Rank 2 | Demoted rank-and-file (~5% misconduct) | ~30 | 4 | ~120 |
| **Total** | | **~1,046** | | **~16,170** |

Stipends alone come to ~16,000 koku/year per legion.  Empire-wide across the standing 25 legions, total samurai stipend cost is ~400K koku/year.

#### Tooth-to-tail ratio and non-combatant support

A legion's combat strength is supported by a substantial cohort of non-combatant peasant staff - cooks, cleaners, carpenters, smiths, latrine-diggers, tailors, porters, animal handlers, supply clerks, and other support personnel without whom the legion could not function.  The ratio of combat troops to support staff varies dramatically with deployment posture, which is the single biggest variable in legion cost.

| Deployment Posture | Combat-to-Support Ratio | Total Personnel per Legion | Notes |
| --- | --- | --- | --- |
| Long-term permanent encampment (e.g. Kaiu Wall garrison) | 1:2 | ~3,000 (1,000 combat + ~2,000 support) | The larger support tail includes specialized roles that would not exist in the field: brewers, entertainers, performers, and luxury providers who keep morale up during long deployments; pavers, stonemasons, and construction specialists who maintain and extend the encampment infrastructure; shopkeepers, kitchen specialists, scribes, and clerical staff who run the day-to-day operations of what is effectively a small permanent town |
| Field operations (legion on the move, deployed away from permanent base) | 1:1 | ~2,000 (1,000 combat + ~1,000 support) | A legion in the field sheds most of its luxury-and-construction tail (no need for pavers when the legion is moving every few days) but ironically becomes **more expensive per active soldier** because of supply-chain costs.  The non-combatant tail is smaller in raw count, but every meal, every weapon repair, every horse fodder ration must be carried in by porter or wagon rather than being produced on-site at the permanent encampment |

The 2:1 Wall-encampment ratio reflects the heavy logistical and construction tail of a *permanent* fortress garrison - far larger than a marching field army's lean support echelon (a legion in the field is nearly all combatants) - together with the suppliers and camp-followers a standing garrison accretes.  The 1:1 field ratio matches the lighter "marching legion" structure that Roman and Tang armies used when deploying away from permanent bases.

A breakdown of typical non-combatant roles at a Wall-stationed legion of ~2,000 support staff:

| Role Category | Count | Annual cost (~5 koku/person incl. food) | Notes |
| --- | --- | --- | --- |
| Cooks, kitchen staff, food preservation | ~300 | ~1,500 | Feeding 3,000 people in a permanent encampment requires substantial daily operations |
| Animal handlers, stable hands, fodder management | ~250 | ~1,250 | ~400 horses per legion require constant care |
| Smiths, weapon and armor maintenance | ~150 | ~750 | Daily wear maintenance plus replacement |
| Carpenters, masons, pavers, construction maintenance | ~200 | ~1,000 | Wall fortification and encampment infrastructure |
| Porters, supply clerks, quartermaster staff | ~250 | ~1,250 | Receiving and distributing supplies; record-keeping |
| Tailors, leather-workers, equipment fabricators | ~100 | ~500 | Uniforms and personal equipment |
| Latrine-diggers, water carriers, sanitation | ~150 | ~750 | Critical for preventing camp disease |
| Brewers, entertainers, performers, masseurs | ~150 | ~750 | Morale maintenance during long deployments |
| Scribes, clerical staff, message couriers | ~100 | ~500 | Administrative support for the officer cohort |
| Shopkeepers, market vendors, civilian camp followers | ~200 | ~1,000 | Camp-town economy serving the legion's domestic needs |
| Recovery orderlies, litter-bearers, and priest-healer attendants | ~100 | ~500 | Nursing the Wall's sick-and-wounded load and supporting the legion's priest-healers |
| Shrine priests and keepers | ~50 | ~250 | Builds up across tiers: one full-time priest for each company's shrines (~20 companies) and each battalion's (~5), plus the legion's own larger shrine, the personal and family shrines maintained by wealthier and more powerful officers, and the extra hands that especially pious or superstitious companies take on |
| **Total** | **~2,000** | **~10,000** | |

#### Single legion budget - Wall-stationed reference

A typical Wall-stationed Imperial Legion's annual budget breaks down as follows:

| Category | Annual koku | Notes |
| --- | --- | --- |
| Combat-troop stipends | ~16,000 | Per the rank-squared breakdown table above |
| Combat-troop food and basic equipment allowance | ~7,000 | ~7 koku/legionnaire above stipend (food + basic kit + housing in barracks) |
| Officer expense allowances | ~3,000 | General, battalion commanders, company captains: ceremonial functions, command-tent maintenance, personal household at the encampment |
| Non-combatant peasant support staff | ~12,000 | Per the non-combatant support breakdown table above |
| Horses and stable operations | ~4,000 | ~400 horses per legion: cavalry mounts, supply-train horses, officer mounts, replacement and fodder |
| Equipment maintenance: weapons, armor, fortification supplies, siege material | ~10,000 | Annual replacement and maintenance, plus encampment construction supplies |
| Fortification work specific to this legion's stretch of Wall | ~10,000 | Stonework, watchtower repair, gate maintenance, structural work |
| Medical and priest-healer infrastructure | ~2,000 | Medical posts, recovery facilities, priest-healer stipends, casualty pensions |
| Camp operating supplies | ~8,000 | Firewood, food preservation, daily-life supplies at the permanent encampment |
| Other (intelligence operations, religious ceremonies, ad-hoc costs) | ~3,000 | Scout teams, monastery donations, daily-life expenses not otherwise itemized |
| **Total per Wall-stationed legion** | **~75,000** | |

Field-deployed legions cost roughly **1.5x** the per-legion baseline due to supply-chain inefficiency, even though their non-combatant tail is smaller in count.  A field-deployed legion costs ~100-115K koku/year, vs. ~75K for a Wall-stationed legion.

In peacetime the standing **25 legions** are the great majority Wall-stationed, with a handful on border, ceremonial, or emergency-response duty at field rates.  This gives a stable peacetime baseline:

- The 25 legions themselves (mostly Wall-stationed at ~75K, a few at field rates): ~2M
- Plus Imperial-level War Ministry coordination, central logistics, weapon and war-horse programs, and strategic-reserve readiness: ~1M
- **Peacetime total: ~3M**, the figure shown on the main spending table.

This baseline is steady across a normal decade.  It rises sharply only under the exceptional circumstances described below, when the Emperor both field-deploys standing legions (at ~1.5x cost) *and* raises additional ones; in such years the War line can reach ~6-7M.  The high cost of those exceptional years - not the steady peacetime ~3M - is what made the recent wars so damaging to the Imperial reserves (see Imperial Savings below).

#### Campaign context: the Lion/Crane war

For most of recent Imperial history, the great majority of Imperial Legions have been stationed on the Kaiu Wall, where they remain.  This is the stable peacetime baseline.

During the **6-year Lion/Crane War**, the Emperor first redeployed several standing legions away from the Wall.  Officially these deployments were framed as quelling peasant unrest in war-affected provinces and ensuring civilian safety along the frontiers; in actual practice they were also meant to prevent opportunistic raids into territories unaffiliated with the war - notably Imperial-Family holdings, whose own forces were not built for sustained defense against clan-aligned raiders - a rationale too politically delicate to state aloud.  But pulling legions off the Wall was only ever a **stopgap**, sustainable until additional legions could be raised.  Once they were, the redeployed legions mostly returned to the Wall, and the newly-raised legions took over the watch in Imperial lands and in the domains bordering the conflict - standing as what a modern military historian would call **tripwire forces**, present in enough strength to make any incursion into the non-Lion, non-Crane domains deemed off-limits to the war an unacceptable provocation rather than an opportunity.

This made the war far more expensive than simple relocation would suggest.  A legion operating from a non-permanent base already costs ~1.5x its Wall-stationed rate; on top of that, the Emperor was now paying for **additional legions** raised specifically for the duration.  Strictly, the Crown is not even *required* to fund the stipends of legionnaires in Imperial service - but to have declined, or to have economized visibly, would have signaled that the Imperial treasury was in distress, and a dynasty that projects weakness invites exactly the instability the legions were deployed to prevent.  Paying in full was therefore treated as non-optional.

In other circumstances the Hantei do have a cheaper instrument: they can require extra military service while demanding that the daimyo supplying the troops bear the cost.  This is permissible, is frequently used for shorter or more distant deployments, and doubles as a test of whether a domain will meet its Imperial obligations out of loyalty and the understanding that such sacrifices are repaid over time in Imperial favor.  The Emperor used exactly this instrument for the **Lion/Unicorn War** - a shorter but still large-scale conflict that broke out in the final 3 years of the Lion/Crane War and was negotiated to a settlement at the same time - which was far enough from the capital for the demand to read as routine.  But the Lion/Crane fighting was too close to Otosan Uchi for the same approach: there, "the Emperor asks you to sacrifice" might have been heard as "the Emperor is so desperate he has no choice but to ask," accomplishing the opposite of its intent.  Near the capital the only safe posture was business as usual, whatever the added expense.

Over six years these costs - field-rate deployments, freshly raised legions, and full Imperial funding throughout - drew the treasury down considerably and were a major contributor to the current fiscal crisis (see Imperial Savings below).  With both wars settled, the raised legions have been stood down and the rest have returned to the Wall, so the War line has dropped back to its steady ~3M peacetime baseline - but the cumulative drawdown of the war years has not been recovered.

#### Historical justification

Han Dynasty military spending was 15-30% of central revenue at peak.  Tang under Xuanzong: ~20-30% of revenue on military (frontier garrisons plus central army).  Ming Dynasty at peak Wall-defense intensity: ~25-35% (most of which was border garrison troops).  Rokugan at ~15% on legions is at the low end of historical norms for an empire facing significant frontier military pressure - understated relative to Ming peak, but defensible because Crab Clan carries significant additional military costs from their own treasury that don't appear in this line, and the other clans' standing armies are similarly Crown-independent rather than Imperial.

In scale terms, Rokugan's standing army of ~25,000 active combat legionnaires in peacetime (~75,000 total Imperial military personnel including non-combatant support) - rising toward ~40,000 combat (~120,000 total) at the height of a major war - is, in absolute terms, in the broad range of mid-Tang central armies (~100K-200K), though markedly smaller relative to Rokugan's far larger population, and significantly smaller than Han or Ming peak central forces (~600K-1M).  The Rokugani Imperial standing army is moderate-to-small for an empire of ~100 million inhabitants, but the broader Empire-wide military capacity (Imperial legions + clan standing armies + clan-bushi reserves) is much larger and adequate to the threats the Empire faces.

**Why the central army can be small: the Emperor does not rule by direct force.**  The modest size of the Imperial legions is not the vulnerability it might first appear, because the legions are not the instrument by which the Hantei actually hold power.  The Emperor is, by and large, reluctant to deploy them against even a single small vassal house of the 7 Great Clans.  The throne can, and on rare occasions does deploy troops in this manner, but it treats this as a tool of last resort rather than the foundation of its authority.  The reluctance is specifically about turning the legions *against* a Great Clan; deploying them *among* the clans as a neutral force - damping inter-clan border friction, suppressing unrest in a distant province, or steadying the situation once a conflict like the Lion/Crane War is already underway - is routine and carries none of the same risk.

The foundation of the Empire's stability is instead an equilibrium between the Clans and the Hantei dynasty that continues to benefit every major stakeholder, and the central political project of the Hantei across the centuries has been to keep that alignment of interests intact.  Asserting raw military dominance might resolve particular disputes faster and more directly, but the dynasty has been extraordinarily careful *not* to let the Celestial Order come to rest on the Clans' fear of the Imperial army: such an order would be only as durable as the throne's ability to maintain permanent military superiority over the combined Clans, which would be difficult, ruinously expensive, and carry its own risk of provoking the very coalition it was meant to deter.

What actually prevents, say, the daimyo of the Matsu Family from seizing control of the whole Lion Clan - or the 7 Clans, collectively, from overthrowing the Hantei - is structural rather than military.  Set aside even the Lion-specific custom by which every Lion samurai swears *dual* blood oaths of fealty, one to their own daimyo and one directly to the Emperor (a practice unique to the Lion).  Rokugan's feudal system of vassal houses gives each vassal daimyo their own standing army, loyal personally to them.  A Matsu daimyo bent on usurpation would therefore need to secure durable commitments from dozens of such vassals - each of whom benefits enormously from the current order, and each of whom is strongly incentivized to expose and oppose the treachery rather than gamble on it.  Indeed, were such an attempt ever made, one of the daimyo who helped thwart it would almost certainly be installed as the new sovereign daimyo of the Matsu Family, which makes loyalty not merely safe but positively rewarding.  No widespread military coup against the Hantei has ever been attempted, in large part because the dynasty has so exhaustively maintained the structural constraints that make rebellion by any major subset of the Clans nearly impossible to coordinate.

The Imperial legions, in this light, need not be strong enough to conquer a Great Clan outright.  They need only be strong enough to reinforce the loyalist forces that already exist *within* any fracturing Clan, so that any plausible internal fracture can be reliably expected to resolve in the Emperor's favor.  A force sized to tip a balance is far cheaper than a force sized to win a war of conquest, which is precisely why a standing 25 legions (with additional legions raised in a crisis) suffice to secure the throne of a 100-million-population Empire.

This pattern of consolidating power through engineered interdependence rather than standing force is not unique to Rokugan; it is a recognizable feature of stable feudal systems generally.  But, as with so much of its governance, Rokugan is unusually well-run for a premodern society, and the Hantei have sustained the arrangement more successfully, and for longer, than any real-world dynasty managed while still wielding real power.  The real dynasties that endured even longer (the Imperial House of Japan foremost among them) generally did so by allowing themselves to be reduced to ceremonial figureheads while actual governance passed to shoguns, regents, or ministers.  That is arguably true of the Hantei to some extent (the Emperor rarely takes a significant action not "recommended" by the Imperial Chancellery), but only to a degree: across a thousand-year span, Rokugan's Imperial monarchy has retained far more wealth, direct control of governance, and real power than the throne of any comparable real-world empire.

### Kaiu Wall direct contributions: line-item detail

The ~3-5 million koku/year for direct Imperial Wall contributions covers:

- **Imperial-funded wall maintenance** (~1-2 million): Stonework, watchtower repair, gate maintenance, and structural work above and beyond what the Crab Clan funds directly from clan-level revenue.

- **Supply caravans to the Wall** (~500-750K): Rice, equipment, materials shipped from non-Crab regions of the Empire via the Imperial road network and the Imperial logistics corps.

- **Magical-ward materials** (~500-750K): Jade for jade-strike weapons, ritual components for ward refresh, scroll-paper and ink for ward-renewal ceremonies, supplies handled and consumed by Imperial shugenja (often Kuni shugenja seconded to Imperial postings).

- **Supernatural-threat response infrastructure** (~500-750K): Emergency Shadowlands-incursion response forces, specialized anti-oni equipment, dedicated shugenja units rotating through Wall postings, intelligence operations probing into the Shadowlands.

- **Material aid to the Crab Clan beyond legion contributions** (~500-750K): Imperial-funded supplies, equipment, and emergency aid that go directly to Crab Clan operations rather than to the legions stationed there.

**Critical context**: this Imperial-direct line covers ONLY the Imperial Court's strategic contribution.  Most of the Wall's total operating cost is borne by the Crab Clan from their own domain-level budgets - Crab Clan bushi, Crab-clan-funded fortification crews, Crab Clan magistrates running Wall logistics, Crab-clan-produced iron and stone from their domains.  Total Wall operations probably consume an additional ~5-10 million koku/year of Crab Clan revenue ABOVE the Imperial line shown here.

**Historical justification**: Ming Wall+frontier spending was 25-35% of central revenue at sustained peak.  Most of that was border garrison troops (which in Rokugan we account for under the legions line above).  The "Imperial Wall direct" category corresponds to the Ming "frontier supply and fortification capital" budget category, which in Ming China was an additional ~5-10% of central revenue beyond garrison troop costs.  Rokugan's ~3-5 million is ~10-15% of Imperial revenue, comparable to the Ming case.  Combined Wall+legions Imperial spending lands at ~22-33% of revenue, squarely within Ming-peak frontier-defense norms.

**Length and intensity comparison**: The Great Wall of Ming was ~5,500 miles total length; the Kaiu Wall is shorter (estimates range from ~500 to ~1,500 miles depending on how the canonical L5R descriptions are interpreted, and we assume ~1,000 miles) but more fortification-intensive per mile because of the ongoing supernatural threat profile.  Thus, we assume a per-mile cost approximately similar to Ming Great Wall maintenance.

### Imperial magistrates and their staff: line-item detail

The ~3-4 million koku/year for the Imperial Magistrate cohort breaks down as follows:

- **The ~284 standing Imperial Magistrate main offices at domain capitals** (~1.5 million): One Imperial Magistrate stationed in every domain (per the Emerald Charter), located at the domain capital.  This covers the Magistrate's personal stipend (Rank 10 for vassal-house domains, Rank 11 for non-ruling Family domains, Rank 12 for Clan-ruling Family capitals - see the Rank by Domain Tier table below), retinue, manor and office operations, the office's standing yoriki force (handling general judicial work, dispute investigation, cross-clan-issue mediation, and the *capital-city* tariff audit work), and the supervision of **the Emperor's local granaries within the domain**.
    - The granary function is structurally important: most of what is collected in Imperial taxes does not physically travel to Otosan Uchi (Rokugan is ~1,000 by ~1,500 miles, and physically transporting grain over those distances would be prohibitively expensive) but is instead stored in the Imperial granaries in each domain capital and used locally - for paying yoriki and other Imperial-staff stipends, funding road and waystation operations, supporting the local Imperial Magistrate's office, and being released into the local market in lean years (the "ever-normal granary" function familiar from Tang/Song Chinese administration).  The Imperial Magistrate's role in overseeing these granaries is one of the most economically consequential functions of the office.  Per-IM cost varies dramatically with the size of the domain capital (see the Per-Magistrate Office Staffing and Budget detail below).  (Otosan Uchi's Imperial granary infrastructure is exceptional: because the capital concentrates ~1 million inhabitants, its granaries are vastly larger than any per-domain installation, and Otosan Uchi's local market is tightly monitored and controlled by Imperial regulators.  This is partly handled through the Otosan Uchi local government line in the spending table and partly through the Imperial Ministry of Rites' Empire-wide ceremonial-distribution coordination.)

- **~2,400 provincial-city Imperial yoriki sub-stations** (~400K): One small Imperial yoriki sub-station in each of the Empire's ~2,400 provincial cities, auditing tariff collection at the provincial city's gates.  These sub-stations report up to the Imperial Magistrate at their domain capital and are administratively part of the Imperial magistrate cohort, but they are budgeted and counted separately because the empire-wide multiplier is different (~2,400 provincial cities, using the 400-MD × 6-provinces aggregation, rather than the ~284 actual domain capitals).  See the Provincial-City Imperial Yoriki Sub-Station Budget detail below.

- **Emerald Champion central operations** (~500-700K): The Imperial Minister of Justice's office in Otosan Uchi, supporting the Emerald Champion's institutional functions (administration of the Test of the Emerald Champion, coordination of Imperial Magistrate appointments and rotations, central judicial review).

- **Traveling Imperial Magistrate force** (~300-500K): Imperial Magistrates not assigned to specific domains but moving between assignments, often handling cross-clan disputes or specialized investigations that exceed a single domain's scope.

- **Imperial-court judicial infrastructure at Otosan Uchi** (~300-500K): The Imperial Court's own judicial machinery, including court materials, prisoner transport across the Empire, ceremonial execution costs at the capital, and the Imperial archives that track precedential rulings.

- **Standing investigative units** (~200-400K): Including the salt-smuggling investigative unit documented under the Imperial Revenue salt-monopoly discussion above, plus other specialized Imperial investigation units (counterfeit-currency squad, false-Imperial-credential investigators, etc.).

**Note on the tariff-audit infrastructure**: the Imperial yoriki performing tariff audit at provincial city and capital city gates throughout the Empire are part of the Imperial Magistrate cohort, but distributed across two budget categories: the 284 Imperial magistrate main offices at domain capitals each include ~25 yoriki handling general judicial work AND the capital-city tariff audit, while the ~2,400 provincial-city sub-stations each include ~4-5 yoriki specifically for provincial-city tariff audit.  Total Imperial yoriki Empire-wide across both categories: approximately 14,000-15,000.  This is distinct from the separate waystation-yoriki cohort budgeted in the Imperial Roads line above; those waystation yoriki perform transit-stamp verification at intermediate points along the roads between cities, not point-of-sale tariff audit at city gates.  The two cohorts (Imperial Magistrate-attached city-gate yoriki and Imperial Roads-attached waystation yoriki) are functionally and budgetarily separate.

#### Imperial magistrate rank by domain tier

The Imperial Magistrate's personal rank is determined by the political tier of the domain they are posted to, not by the size of the domain's capital city:

| Domain Tier | IM Rank | IM Stipend (koku/yr) | Approximate Empire-wide Count | Examples |
| --- | --- | --- | --- | --- |
| Vassal-house domain | Rank 10 | 100 | ~252 | Reiji (Hida vassal house), Wakashi (Ikoma vassal house), Damasu (Akodo vassal house), Michio (Shosuro vassal house controlling Ryoko Owari) |
| Non-ruling Family domain | Rank 11 | 121 | ~25 | Matsu (non-ruling Lion Family), Yasuki (non-ruling Crab Family), Shosuro (non-ruling Scorpion Family) |
| Clan-ruling Family domain (Clan capital) | Rank 12 | 144 | 7 (one per Great Clan) | The Akodo capital for the Lion, the Hida capital for the Crab, etc. |

The rank is a function of political importance, not commercial scale.  Ryoko Owari is one of the most economically consequential cities in the Empire (500,000 inhabitants, second only to Otosan Uchi) but its Imperial magistrate is Rank 10 because the Michio are a vassal house under the Shosuro Family.  Conversely, a Rank 12 Imperial magistrate at a relatively small Clan-ruling Family capital still carries the prestige and authority of the clan-tier posting even if the city itself is smaller than several Rank 10 vassal-house capitals.

#### Per-magistrate office staffing and budget (median domain capital, Rank 10 IM)

A typical Imperial Magistrate office at a median-sized vassal-house domain capital (~12,000 population, Imperial magistrate at Rank 10) supports the following permanent staffing.  The "Paid by" column distinguishes Imperial appointees and Imperial-paid local staff from samurai whom the local daimyo provides to the office as part of the domain's standing obligation to support Imperial functions:

| Role | Count | Status / Rank | Stipend (koku/yr) | Total (koku/yr) | Paid by |
| --- | --- | --- | --- | --- | --- |
| Imperial Magistrate themselves | 1 | Rank 10 samurai (Imperial appointee) | 100 | 100 | Imperial budget |
| Karo (chief steward / secretary to the IM) | 1 | Rank 6 samurai (Imperial appointee, traveling with the IM) | 36 | 36 | Imperial budget |
| Personal household samurai | ~5 | Rank 4-5 samurai (Imperial appointees, sourced from either Imperial or Clan families) | ~20 avg | ~100 | Imperial budget |
| Yoriki for general judicial work + capital-city tariff audit | ~25 | Rank 3 samurai (Imperial appointees - oversight cannot be local) | 9 each | ~225 | Imperial budget |
| Ashigaru (manor security, prisoner escort, court enforcement) | ~8 | Ashigaru (locally recruited) | 2 each | ~16 | Imperial budget |
| Manor servants and clerical peasants | ~13 | Peasants (locally recruited, housed + fed + small stipend) | ~1 each | ~13 | Imperial budget |
| Manifest clerks and scribes (locally-detailed support samurai) | ~3 | Rank 3 samurai (clan samurai detailed by the local daimyo to assist) | 9 each | ~27 | Local clan budget |
| **Total staff** | **~56** | | | **~517** | |

Plus food and equipment allowances for the Imperial-paid samurai cohort (~3 koku/samurai × ~32 samurai + ~1 koku × 8 ashigaru): ~104 koku, bringing total Imperial-paid personnel cost to ~594 koku/year.  The clan-paid manifest clerks cost an additional ~36 koku/year from the local daimyo's budget.

Single median Imperial magistrate office budget (Imperial portion only):

| Category | Annual koku | Notes |
| --- | --- | --- |
| Personnel stipends and allowances (Imperial-paid only) | ~600 | Per the staffing breakdown above |
| Manor maintenance, grounds, stable | ~700 | The Imperial magistrate is a senior Imperial official whose residence and office must reflect their rank.  Manor maintenance, gardens, stable, fortified walls, ceremonial halls |
| Office operations | ~250 | Court materials, paper, ink, document storage, archive maintenance |
| Travel and ceremonial allowances | ~450 | Official duties require regular travel within the domain; ceremonial entertainment of visiting Imperial officials, the daimyo, and other domain elites |
| Local Imperial granary supervision and oversight | ~450 | The Imperial magistrate oversees the Emperor's local granaries (see the granary discussion above).  Separate granary staff, materials, and operations costs |
| Religious offerings, gifts, ceremonial expenses | ~250 | Donations to local temples, gifts to local notables maintaining court relations, ceremonial expenses at festivals |
| Imperial Court correspondence and courier dispatch | ~150 | Regular reports back to Otosan Uchi, dispatches to/from the Emerald Champion's office, communication with the traveling force when relevant |
| Other (ad-hoc, miscellaneous) | ~150 | Reserve for unexpected costs (special investigations, dispute mediation expenses, prisoner transport beyond normal volume) |
| **Total per median office (Imperial budget)** | **~3,000** | |

#### Imperial magistrate office scaling by capital size

The ~3,000-koku figure is for a typical median (Rank 10 Imperial magistrate, vassal-house) capital.  Larger domain capitals carry substantially larger Imperial magistrate offices because both the judicial workload and the capital-city tariff-audit workload scale with the city's commercial volume.  The Empire's largest domain capitals roughly follow **Zipf's law** (the Nth-largest city is approximately 1/N the size of Otosan Uchi at 1,000,000), per the list in [l7r.md - Large Cities](l7r.md#large-cities).

Note that the **Imperial magistrate rank** (10/11/12) and the **Imperial magistrate office budget** (which scales with city size) are independent variables: a Rank 10 Imperial magistrate at Ryoko Owari (500,000 inhabitants, the 2nd-largest city in the Empire) runs a ~75,000 koku/year office, while a Rank 12 Imperial magistrate at a Clan-ruling Family capital may have a smaller office in absolute terms but carries the political prestige of the clan-tier posting.  Per-Imperial-magistrate cost still scales sub-linearly with population because the magistrate themselves and personal-household components are fixed costs that don't grow with city size - it is primarily the yoriki cohort and the granary-oversight infrastructure that scale.

Scaling categories used for the Empire-wide office aggregation:

| Tier | Population Range | Number of Capitals | Typical Rank Distribution | Per-Office Cost | Subtotal |
| --- | --- | --- | --- | --- | --- |
| Very large Clan-capital / major-trade-hub (rank 2-5 cities) | 200K-500K | 4 (Ryoko Owari [Rank 10 Imperial magistrate, Shosuro's Michio vassal house], Toshi Ranbo [Rank 10, Akodo's Damasu vassal house], Yasuki Estates [Rank 11, Yasuki Family], Kyuden Daidoji [Rank 11, Daidoji Family]) | 2 Rank 10 + 2 Rank 11 | ~60K avg | ~240K |
| Large Clan-capital (rank 6-11 cities) | 90K-200K | 6 (Shiro Otaku, Kyuden Shinjo, Kyuden Matsu, Kyuden Doji, Kyuden Mirumoto, Kyuden Ikoma) | Mix of Rank 11 (Family capitals) and Rank 12 (Clan-ruling Family capitals) | ~25K avg | ~150K |
| Medium-large capitals | 30K-90K | ~20 | Mostly Rank 11, some Rank 10 vassal-house seats, a few Rank 12 Clan capitals | ~10K avg | ~200K |
| Medium capitals | 15K-30K | ~70 | Mostly Rank 10 vassal-house seats, some Rank 11 Family seats | ~5K avg | ~350K |
| Median/small capitals (largest tier of count) | 5K-15K | ~184 | Almost entirely Rank 10 vassal-house seats | ~3K avg | ~552K |
| **Total main offices** | | **~284** | **~7 Rank 12 + ~25 Rank 11 + ~252 Rank 10** | | **~1.5 million** |

Notes:
- The Imperial magistrate rank split (~7 Rank 12 + ~25 Rank 11 + ~252 Rank 10) follows the domain tiers in [l7r.md - Clan Populations](l7r.md#clan-populations): **7 Clan-ruling Family capitals** (one per Great Clan) get a Rank 12 IM; the **~25 non-ruling Family capitals** (the Matsu, Ikoma, and Kitsu of the Lion; the Yasuki, Kaiu, Kuni, and Hiruma of the Crab; and so on, plus the three non-ruling Imperial Families) get a Rank 11 IM; and the **~252 remaining vassal-house domains** get a Rank 10 IM.  The counts are approximate at the margins (minor-clan single-domain holdings and Imperial-Family domains are edge cases), but the three-tier structure is firm.
- The Empire's largest 10-15 cities follow Zipf's law fairly closely.  Below that the long tail flattens - the median-tier domain capitals are mostly smaller cities clustered in the 5K-15K range, with the median of 12K matching the Reiji-style domain in the worked-example section above.
- Otosan Uchi at 1,000,000 inhabitants is not a domain capital - it is the Imperial direct domain and its judicial functions are handled through the Otosan Uchi local government budget line and the central judicial machinery (Emerald Champion central operations, Imperial-court judicial infrastructure) rather than through an office attached to a domain capital.

#### Provincial-city Imperial yoriki sub-station budget

Each of the ~2,400 provincial cities in the Empire (400 median domains × 6 provinces per MD) houses a small Imperial yoriki sub-station that audits tariff collection at the city's gates.  This uses the ~400 MD × 6 multiplier rather than the ~284 actual-domain multiplier because larger actual domains have proportionally more provincial cities than the median (see [The two Empire-wide multipliers](#the-two-empire-wide-multipliers) for the dual-multiplier discussion).

Staffing breakdown for a typical provincial-city sub-station:

| Role | Count | Status / Rank | Stipend (koku/yr) | Total (koku/yr) |
| --- | --- | --- | --- | --- |
| Senior yoriki overseer (reports to the Imperial Magistrate's office at the domain capital) | 1 | Rank 5 samurai | 25 | 25 |
| Sub-yoriki / assistants | ~2 | Rank 4 samurai | 16 each | ~32 |
| Sub-yoriki / assistants | ~2 | Rank 3 samurai | 9 each | ~18 |
| **Total** | **~5** | | | **~75** |

Plus food and equipment allowances (~3 koku × ~5 samurai = ~15 koku), bringing personnel costs to ~90 koku/year.

The senior overseer sits at Rank 5 by design: under the [Doctrine of Three Steps](l7r.md#the-doctrine-of-three-steps), an official is dismissible as "beyond the reach" of anyone more than three ranks above them, so a Rank 4 overseer could press an audit finding only as far as the Rank 7 Provincial Minister of Revenue whose collectors they oversee, whereas Rank 5 keeps them within reach of the provincial governor above as well.  The assistants sit at Ranks 3-4 (two of each).

Single sub-station budget:

| Category | Annual koku | Notes |
| --- | --- | --- |
| Personnel stipends and allowances | ~90 | Per the staffing breakdown above |
| Operational supplies | ~50 | Manifest paper, sealing wax, audit-record materials |
| Quartering / workspace | ~30 | Small office near the provincial city gate, or rented space in the provincial governor's administrative annex |
| Travel and communication with the domain capital Imperial magistrate | ~30 | Regular reports and dispatches between the sub-station and the senior office |
| Medical, religious offerings, ad-hoc | ~20 | Basic supplies and miscellaneous |
| **Total per provincial-city sub-station** | **~220** | |

Empire-wide aggregation: **~2,400 × ~220 = ~528,000 koku/year**.

The sub-station's primary function is to *audit* "the Yasuki Taka system" inspectors and licensors (who are part of the provincial Revenue ministry, not the Imperial magistrate cohort), verify that the Emperor's 5% cut is correctly collected on all imported goods sold at the provincial city, and report any discrepancies up to the Imperial Magistrate at the domain capital.  Sub-station yoriki do not collect taxes themselves; they monitor the collection.  This architectural separation between domain-level tax collection (provincial ministries) and Imperial oversight (Imperial Magistrate cohort) is the audit-side counterpart to the inspector/licensor split in the original Yasuki Taka system: just as the inspector who assesses goods is institutionally separate from the licensor who collects payment, the licensor who collects is institutionally separate from the Imperial yoriki who audits the records.

#### Imperial appointees vs. locally-sourced staff (per-domain view)

The Imperial infrastructure within any domain is staffed by a mix of three groups, distinguished by funding source and origin:

1. **Imperial appointees** - personnel sent by the Emperor from elsewhere, paid from the Imperial budget, rotating periodically.  Required for any position involving oversight of local activities (all yoriki, regardless of where they're posted) or strategic command (the Imperial Magistrate and karo at the capital, relay-masters at waystations).  Oversight cannot be local because the daimyo's own samurai cannot be trusted to audit the daimyo's own imports, granaries, or judicial proceedings - the structural conflict of interest is too direct.

2. **Locally-detailed clan samurai** - samurai of the host domain assigned by the local daimyo to support Imperial functions in non-oversight roles (couriers, mounted patrol leaders, manifest clerks, office scribes).  Paid from the local clan budget as part of the domain's standing obligation to support Imperial infrastructure.  These postings are prestigious - working alongside Imperial appointees, often with promotion potential and visibility to the Emerald Champion's office - but are explicitly **not** oversight positions.  The phrasing inside the domain is that these samurai are detailed *to assist* the Imperial Magistrate (or the waystation relay-master), not *to oversee* on behalf of the Emperor.

3. **Locally-recruited ashigaru and peasants** - hired from the host domain's population, paid from the Imperial budget.  Handle physical, security, and unskilled labor (mounted patrol ashigaru, stable hands, kitchen staff, manor servants, road-maintenance specialists, ashigaru security at the Imperial magistrate's manor).

For a median (vassal-house) Reiji-style domain - ~12 waystations within the domain (per the geographic divisor: ~5,000 waystations Empire-wide / ~400 median domains of Empire land area = ~12.5 waystations per MD of land), 6 provincial cities each with a yoriki sub-station, 1 Imperial Magistrate at the domain capital - the breakdown looks like:

| Imperial Infrastructure Location | Imperial Appointees | Locally-Detailed Clan Samurai (clan-paid) | Local Ashigaru + Peasants (Imperial-paid) | Total Staff |
| --- | --- | --- | --- | --- |
| ~12 waystations within the domain (per station: 1 relay-master + 1 yoriki + 3 detailed clan samurai + ~11 ashigaru/peasants) | 24 (12 relay-masters + 12 waystation yoriki) | 36 (3 per station: courier-postmaster, mounted patrol leader, manifest clerk) | ~132 (~4 mounted patrol ashigaru + ~7 peasants per station) | ~192 |
| 6 provincial-city Imperial yoriki sub-stations (~5 yoriki per station, all Imperial appointees) | 30 | 0 | 0 | 30 |
| 1 Imperial Magistrate main office at the domain capital | 32 (1 Imperial magistrate + 1 karo + ~5 personal household + ~25 yoriki) | 3 (manifest clerks) | ~21 (~8 manor-security ashigaru + ~13 manor servants/clerical peasants) | ~56 |
| **Total per Reiji-style vassal-house domain** | **~86** | **~39** | **~153** | **~278** |

So within the Reiji domain, approximately **86 Imperial appointees** are working on Imperial business at any given time - the Imperial Magistrate themselves, their traveling retinue and yoriki force, the yoriki manning the 6 provincial-city sub-stations, and the 24 relay-masters and waystation yoriki scattered across the ~12 waystations within the domain.

Conversely, the Reiji domain commits approximately **39 of its own samurai** to locally-detailed Imperial-adjacent service: 3 at the Imperial magistrate's office in the capital (as manifest clerks) and ~36 across the waystations (as couriers, patrol leaders, and clerks).  At average ~Rank 3-4 (12 koku stipend), the clan budget burden for these detailed samurai is ~470 koku/year - a tiny fraction of Daimyo Hida no Reiji Isao's discretionary budget, but a continuing structural reminder of the domain's obligation to support Imperial infrastructure operating within its borders.  These postings are well-regarded among Reiji's samurai because working alongside Imperial appointees confers prestige, access to the Imperial Magistrate's court, and a documented record of competent service that can be cited in promotion considerations.

**Note on the multipliers used in this breakdown**: per [The two Empire-wide multipliers](#the-two-empire-wide-multipliers) above, this section uses **~400 MD** for waystations (geographic distribution by land area) and provincial-city sub-stations (sub-unit count), but **~284 actual domains** for the Imperial magistrate main office (one per the Emerald Charter) and for the samurai-pool quantities (outflow count, clan budget burden) discussed below.

Empire-wide totals (rough):
- The ~86 appointees per median domain are NOT all aggregated with the same multiplier - each component uses the divisor appropriate to it (per [The two Empire-wide multipliers](#the-two-empire-wide-multipliers)): the **24 waystation appointees** and **30 sub-station appointees** are geographic/sub-unit counts, so × ~400 MD = ~9,600 + ~12,000; the **32 Imperial-magistrate-main-office appointees** are a per-actual-domain count, so × ~284 = ~9,100 at the median, rising to ~13,000 once larger capitals' bigger offices are included (per the scaling table above).  Total: ~9,600 + ~12,000 + ~13,000 = **~34,600 Imperial appointees** working in main offices, provincial sub-stations, and waystations Empire-wide.  (Multiplying the full 86 by 400 would happen to land near the same total only by coincidence - the correct method keeps the office component on the ×284 divisor.)  Plus ~5,000-7,000 additional Imperial appointees in central roles (Emerald Champion's office, traveling Imperial magistrate force, Otosan Uchi's judicial infrastructure, investigative units, and the much larger Imperial Legion cohort separately budgeted).
- ~39 locally-detailed clan samurai per MD × 400 = ~15,600 clan samurai Empire-wide in Imperial-adjacent support roles (clan-paid, distributed across all 7 Great Clans in proportion to their land area).
- ~153 ashigaru and peasants per MD × 400 = ~61,200 ashigaru and peasants Empire-wide working at Imperial facilities (Imperial-paid, locally recruited).

For larger domains (the Lion, Crab, and Crane have substantially more land area per clan than the smaller clans; Clan-capital and Family-capital domains have larger offices), these per-domain figures scale up proportionally.  The clan-budget burden for locally-detailed samurai also scales: a Crane province with multiple Family capitals and many vassal houses may have ~150-250 detailed clan samurai serving Imperial functions across the province's waystations and Imperial magistrate offices.

#### Imperial magistrate cohort total aggregation

Bringing together the Empire-wide totals for the Imperial Magistrate cohort:

| Component | Empire-wide Annual Cost |
| --- | --- |
| 284 Imperial Magistrate main offices at domain capitals (per the scaling table above) | ~1.5 million |
| ~2,400 provincial-city Imperial yoriki sub-stations (per the breakdown above) | ~0.53 million |
| Emerald Champion central operations | ~0.5-0.7 million |
| Traveling Imperial Magistrate force | ~0.3-0.5 million |
| Imperial-court judicial infrastructure at Otosan Uchi | ~0.3-0.5 million |
| Standing investigative units | ~0.2-0.4 million |
| **Total Imperial Magistrate cohort** | **~3.3-4.1 million** |

This matches the ~3-4M Imperial Magistrate line shown under the Imperial Ministry of Justice in the Imperial Spending table above.

**Historical justification**: Tang and Song central administration including the judiciary, central court bureaucracy, and Imperial inspector forces was probably ~15-20% of central revenue at peak.  Ming and Qing were closer to ~5-10% (their central administrations were structurally smaller).  Rokugan at ~9-11% sits between Ming/Qing norms and Tang/Song norms, which is consistent with the Empire's overall positioning as moderately more centralized than Ming/Qing but less centralized than Tang/Song.

### Total Imperial appointee samurai: Empire-wide synthesis

The various Imperial appointee positions discussed across the line-item sections above sum to a substantial standing samurai population.  This section consolidates the count, traces how those positions are sourced (Imperial Families vs Great Clans), and computes the per-domain "outflow" - how many of a typical Reiji-style domain's own samurai are themselves currently serving in Imperial posts elsewhere in the Empire.

#### Empire-wide tally of Imperial appointee samurai positions

| Source / Function | Approximate Count | Budgeted Under |
| --- | --- | --- |
| Imperial Legions (rank-and-file + officers + senior command, the standing 25 legions × ~1,000 each) | ~25,000 | Imperial Ministry of War |
| Imperial magistrate main offices at the 284 domain capitals (scaling with capital size: median ~32 each, very large ~250+) | ~13,000 | Imperial Ministry of Justice |
| ~2,400 provincial-city Imperial yoriki sub-stations (5 yoriki per station) | ~12,000 | Imperial Ministry of Justice |
| Waystation Imperial appointees across ~5,000 stations (relay-master + waystation yoriki per station) | ~10,000 | Imperial Ministry of Works (Roads) |
| Central Imperial magistrate cohort (Emerald Champion central + traveling magistrates + Otosan Uchi judicial machinery + investigative units) | ~6,000 | Imperial Ministry of Justice |
| Other Imperial Ministry of Works (Wall direct contributions, central public works engineering, granary infrastructure) | ~4,000 | Imperial Ministry of Works (central) |
| Imperial Ministry of Rites (shugenja and ceremonial officials at Imperial shrines, mourning-period coordinators) | ~2,500 | Imperial Ministry of Rites |
| Imperial Ministry of Retainers (Imperial princes in formal offices, central court samurai, ceremonial-court samurai) | ~4,000 | Imperial Ministry of Retainers |
| Imperial Ministry of Revenue (The Imperial Treasurer's central office, salt-monopoly administration, commercial regulators) | ~1,500 | Imperial Ministry of Revenue |
| Imperial Household (Emperor's personal staff, inner-palace samurai, palace guards) | ~2,500 | Imperial household |
| Otosan Uchi local government (administering the ~1 million inhabitants of the Imperial capital) | ~6,000 | local government |
| **Total** | **~86,500** | (round: **~85,000 Imperial appointee samurai positions Empire-wide**, with substantial uncertainty - the realistic range is ~75,000-95,000) |

For scale: ~85,000 Imperial appointee samurai is approximately the size of a mid-tier Great Clan's working samurai population.  Phoenix and Dragon are in this range; Lion, Crab, and Crane each substantially exceed it.  The Imperial appointee cohort is structurally a "shadow clan" without territorial domains, drawn from across the actual clans plus the four Imperial Families' supply.

#### Source distribution: Imperial Families vs Great Clans

The ~85,000 positions are not sourced evenly across the Empire's samurai population.  Senior posts concentrate heavily in the Imperial Families (Hantei, Seppun, Otomo, Miya); mid-tier and rank-and-file posts are overwhelmingly clan-drawn.  The structural reason is that the Imperial Families' combined samurai population (~15,000-25,000 active) is too small to fill more than a sliver of the lower tiers even at high utilization.

| Tier | Empire-wide Count | Imperial Family Share | Clan Share | Notes |
| --- | --- | --- | --- | --- |
| Senior Imperial magistrate cohort + senior Legion command (Imperial Magistrates themselves, karos, theater commanders, army generals, senior central judicial) | ~700 | ~75% (~525) | ~25% (~175) | Seppun supplies the largest fraction of magistrate and karo posts (the user's hypothesis that "the Seppun Family makes up the bulk of the Imperial magistrates and legion generals" sits here).  Hantei holds a small handful of the most prestigious assignments (the bulk of the Hantei Family runs Otosan Uchi's local government and the inner palace, with high-level help from the other Imperial Families; relatively few Hantei take field postings).  Otomo and Miya supply some senior court roles.  Cross-clan placements - a senior samurai from one clan posted as Imperial magistrate in another - cover the residual ~25% |
| Mid-tier Imperial posts (IM-office personal household, mid-Legion officers, waystation relay-masters, mid-tier central roles) | ~10,000 | ~8% (~800) | ~92% (~9,200) | Imperial Families concentrate their mid-tier share in posts that touch high-prestige central work (IM personal household for senior IMs, top Legion staff officers, Otosan Uchi government leadership).  Most mid-tier posts come from the clans |
| Yoriki and rank-and-file (sub-station yoriki, office yoriki, waystation yoriki, Legion rank-and-file, central Imperial rank-and-file) | ~75,800 | ~5% (~4,000) | ~95% (~71,800) | Almost entirely clan-supplied.  Yoriki postings are the single most numerous Imperial appointment type and the dominant cross-clan "tour of duty" experience for clan samurai |
| **Total** | **~86,500** | **~5,300 (~6%)** | **~81,200 (~94%)** | Imperial Families supply ~6% of all Imperial appointee positions Empire-wide; the system is structurally clan-dependent at scale |

The Imperial Families are small (~75,000 samurai total across all four, per [l7r.md - Clan Populations](l7r.md#clan-populations)), and most of their samurai administer the Imperial Families' own 9 domains rather than serving as Imperial appointees elsewhere - which is why they supply only ~6% (~5,300) of all Imperial appointee positions despite dominating the senior tier.  Seppun is the default supplier for any senior Imperial post, but the family is small enough that it cannot fill every senior post even at high utilization - hence the ~25% cross-clan placements at the senior tier.

#### Per-domain outflow: how many of a daimyo's samurai are serving elsewhere

For a typical Reiji-style vassal-house domain, the **~2,900 working samurai** (~58% of the ~5,000 total) are distributed as follows.  Every one is counted **once, at Reiji** - including those serving the Empire elsewhere, who are *part of* the 3,000, not additional to it (this is what keeps the Empire-wide samurai share at exactly 2%):

| Reiji Samurai Location | Count | Status |
| --- | --- | --- |
| Reiji capital, serving Daimyo Isao's court and administering the capital city | ~800 | In-domain, daimyo-paid |
| Reiji's 6 provincial cities, serving the provincial governors | 6 × ~225 = ~1,350 | In-domain, governor-paid |
| Reiji's 36 county-seat towns, serving the county magistrates | 36 × ~15 = ~540 | In-domain, magistrate-paid |
| In Imperial posts elsewhere in the Empire | ~203 | Empire-paid, serving outside Reiji's borders |
| **Total Reiji working samurai** | **~2,900** | (the rest of the 5,000 are pre-gempukku children and retirees) |

Of the ~2,690 working *inside* Reiji, ~39 are clan samurai the daimyo details to support Imperial functions within the domain itself (waystation couriers and clerks, office assistants) - they are drawn from the cohorts above, not an additional headcount.  The ~203 outgoing figure follows from samurai-supply scaling with each domain's working-samurai pool, which is the **× 400** basis: total clan-supplied Imperial positions Empire-wide (~81,200) divided across the ~400 median domains = ~203 per median Reiji (equivalently ~286 per *average* actual domain × 284, since the average domain is ~1.41 MD).  Of the ~203 Reiji samurai in Imperial posts elsewhere, the breakdown approximates:

| Post Type | Approximate Count | Notes |
| --- | --- | --- |
| Imperial Legions | ~70 | Mix of all ranks; the Crab Clan provides especially large numbers to Wall-end legions because of geographic logic and the Hida-vassal political alignment, with Reiji contributing more than the all-clan average of those Wall-stationed Crab samurai (its inland-vassal status keeps the figure from spiking even higher) |
| As Imperial yoriki and household samurai at other domains' main offices | ~27 | Cross-clan tours in office yoriki roles, working under senior IMs (mostly Seppun or cross-clan senior placements); at the senior tier, Reiji's contribution is reduced (~25% of senior IM/karo posts are clan-supplied, with the bulk going to Seppun and the other Imperial Families) |
| As Imperial yoriki at provincial sub-stations in other domains | ~27 | Cross-clan rotating tours; a Reiji samurai might serve 3-5 years auditing tariff collection in (say) a Lion province before returning home |
| As Imperial appointees at waystations in other domains (mix of relay-masters and waystation yoriki) | ~26 | Spread across waystation roles in non-Reiji parts of the Empire |
| In central Imperial roles in Otosan Uchi (OU local government, central court samurai, central judicial machinery, central ministries other than the Imperial magistrate cohort field roles) | ~50 | Imperial-paid central posts physically located at the capital.  These ~50 are the Imperial-post component of Reiji's ~100-strong total Otosan Uchi presence (the rest being the ~38 clan-paid embassy and ~12 private samurai - see [Samurai concentration by city size and the capital](#samurai-concentration-by-city-size)).  Central roles favor the Imperial Families more heavily, but the absolute clan share is still substantial |
| In other Imperial ministries' field operations (Works engineering, Rites ceremonial, Revenue inspection) | ~3 | Specialized assignments matched to a samurai's particular skills (e.g. an unusually skilled stonemason posted to Wall-construction supervision under Min of Works) |
| **Total Reiji samurai in Imperial service elsewhere** | **~203** | |

**Do their families go with them?**  Whether the ~203 take their households abroad depends on the posting, and this determines how many *non-working* Reiji samurai (children, retirees, non-serving spouses) are physically outside the domain at any time:

- **Imperial Legions and remote road-waystation postings (~96): almost never.**  These are hardship or fast-rotating postings; the samurai's family stays resident in Reiji.
- **Otosan Uchi central posts (~50): usually yes.**  The capital is desirable (good schools, society, opportunity), so spouses and young children accompany - though school-age children are often left with kin in Reiji and elders retire at home.
- **Cross-clan Imperial magistrate office, sub-station, and other field tours (~57): partial.**  Spouse and infants typically come; school-age children and retired parents usually remain in Reiji with the lineage.

Netting this out, **~45-50 non-working Reiji samurai accompany the ~203 abroad**, skewing strongly **young** - babies and toddlers travelling with their parents, plus some pregnant spouses (who may or may not draw a stipend, as this varies by locality with no Imperial decree on the matter).  **Retirees almost never leave**, since samurai retire at home among their lineage.

Separate from the ~203 in Imperial posts, a further **~45 of Reiji's working samurai are abroad at any given moment as traveling samurai without a fixed post** - retainers the daimyo has not assigned to a standing in-domain office, away on *musha shugyo*, open-ended missions, pilgrimage, or their lineage's business.  This is the wandering-samurai life that many player characters lead.  They are *not* Imperial appointees and are *not* part of the ~203 above (which underpins the Empire-wide Imperial-appointee count): they remain Reiji's own retainers, drawing the daimyo's stipend and counted within Reiji's in-domain working cohort, simply physically elsewhere at the moment.  They skew young and travel light, so their families almost never accompany them.

Putting both groups together, **~405-415 Reiji samurai (working and non-working) are physically outside the domain at any moment** - all still counted in Reiji's ~5,000 lineage allocation - while the other **~4,590 reside within Reiji's borders** (a hair under 2% of its 250,000 inhabitants, the slight net-export dip that Otosan Uchi's 4% concentration and the Wall-massed legions balance out Empire-wide).

Reiji's *incoming* Imperial appointees (from elsewhere): ~86, per the Per-Domain View synthesis above.

**Net Imperial flow for Reiji**: ~203 going out minus ~86 coming in = ~117 net samurai "lent" to the Imperial system at any given moment.  Combined with the ~39 Reiji samurai detailed to Imperial functions *within* Reiji, the full Imperial-engagement footprint is ~242 of the ~2,900 working cohort = **~8% of Reiji's working samurai are in Imperial-attached roles at any given time** (whether serving within Reiji's borders or elsewhere in the Empire).

This ~8% engagement figure is the structural cost (or, depending on perspective, structural benefit) of supporting the Imperial system from the daimyo's point of view.  The cost: ~7% of Reiji's working samurai are unavailable for direct domain service at any moment.  The offsetting benefits: the Empire pays the stipends of the ~203 samurai serving elsewhere (so the daimyo loses the labor but not the cost - indeed he keeps their would-be stipends as discretionary income, which is why his cut runs ~7,200 above what his in-domain headcount alone would fund); the rank-uplift principle for Imperial Legion service returns those samurai to Reiji at +1 rank from where they left (a hidden Imperial subsidy to Reiji's manpower pool over the long term, per the Rank Uplift Principle discussion in the Legion section above); the prestige of Reiji samurai serving in Imperial roles strengthens Reiji's standing within the broader Crab Clan and at the Imperial Court; and the rotating cross-clan experience returns experienced samurai to Reiji's service with knowledge of how other clans actually operate at the administrative level.

**Empire-wide cross-check**: ~203 outgoing per median domain × ~400 median domains = ~81,200 clan-supplied Imperial appointee positions (equivalently ~286 per average actual domain × 284).  Plus ~5,300 supplied by the Imperial Families = ~86,500 Empire-wide total.  The structural balance is: each median domain contributes ~203 samurai to Empire-wide Imperial functions and hosts ~86 incoming Imperial appointees, with the Imperial Families supplying the residual ~6% that closes the Empire-wide accounting.  Larger actual domains (Clan capitals, Family seats) contribute proportionally more outgoing samurai AND host proportionally more incoming Imperial appointees; the balance still holds in aggregate.

### Imperial savings: the "wealth in favors owed" model

The Emperor typically maintains "savings" equivalent to roughly 70-110 million koku - two to three years of Imperial revenue in reserve.  This is in line with well-run premodern East Asian Imperial norms: Tang China at its fiscal peak held similar 2-3 year reserves; Song China sometimes accumulated many years' worth of central revenue in its Wealth Treasuries during particularly prosperous reigns; Qing China under the Yongzheng and Qianlong emperors held silver reserves equivalent to roughly two years of central revenue.  Maintaining substantial reserves was the historical default for any well-administered premodern empire, because commodity-money economies could not easily borrow at scale and faced periodic massive obligations (military campaigns, river-control works, famine relief) that ordinary annual revenue could not cover.

However, in addition to these literal reserves, the Emperor commands an even larger pool of de facto wealth in the form of **obligations owed** by those throughout the Empire who have received Imperial generosity at one time or another.

A gift of 10,000 koku from the Emperor to a noteworthy retainer (a wedding gift, a battlefield reward, a contribution to a new construction, a donation to a temple) creates an implicit obligation that the Emperor may later call upon.  When the Emperor later asks that retainer to undertake something costly on the Empire's behalf - to host a foreign embassy, to outfit a campaign, to contribute to a relief effort during a famine - the prior gift is the credit being drawn down.  The retainer does not refuse, because to refuse would be to acknowledge that the prior gift had been unearned.

This treatment of Imperial wealth is structurally important.  Premodern states never achieved the liquid-treasury model that would later characterize early-modern fiscal-military states; their actual operational wealth was always partly in obligation networks.  Rokugan's Emperor has access to a far greater pool of practical resources than the nominal vault-savings figure would suggest, because so many of those resources are pre-committed in the form of favors that can be called.

Reserves at this scale serve several specific structural functions beyond ordinary fiscal smoothing.  The largest is **Imperial succession**: each new Emperor's coronation and the preceding Emperor's funeral collectively consume the equivalent of 3-6 months of central revenue concentrated in a single year.  Imperial mourning periods are smaller events but still substantial: when the Emperor's wife or mother dies, a public mourning period is observed across the entire Empire (during which "people" - samurai - may not marry, though peasants conduct their own observances independently); the Empire-wide ceremonies center on the **opening of the Imperial granaries at every domain capital**, where peasants from surrounding counties travel to the domain capital to receive sacks of grain that both make the journey worth their while and serve as a public celebration of the figure who passed.  These distributions are funded from accumulated Imperial reserves and consume roughly ~5-15 million koku across the Empire-wide observance period (varying with the length of the mourning period, which scales with the depth of the Emperor's grief and the rank of the deceased).  Other reserves draws include major military campaigns, river-control works after catastrophic floods, and famine-relief operations during multi-domain crop failures.

The Empire's current state (per the campaign-current understanding) is that recent years have been very hard on Imperial finances, and the practical pool of total Imperial reserves (vault savings and callable obligations combined) is down to roughly 10 million koku - under a third of one year's revenue, and roughly an order of magnitude below the well-run-empire norm of 2-3 years.  By the standards of any well-administered premodern empire this is a genuine fiscal crisis, and the Imperial Treasurer is under considerable pressure to rebuild reserves.  This number can shift with the campaign's events.

The proximate cause of the current crisis is well-known in the Imperial Court.  The passing of Hantei the XXXVIII's mother brought an unusually long mourning period with especially generous Empire-wide grain distributions, reflecting the depth of the Emperor's feeling for her; at the time of her death the reserves were only slightly below normal, but the extended observances consumed several years' worth of accumulated savings.  This drawdown was followed almost immediately by the **Lion/Crane War**, and then by the **Lion/Unicorn War** that broke out in its final 3 years and was settled alongside it - between them imposing years of the elevated military costs described in the legions section above (field-rate deployments, freshly raised legions, full Imperial funding throughout), on top of magistrate interventions, supply disruption to the Wall, and emergency famine relief in war-affected counties.  Between the mourning and the wars the reserves fell from near-normal to the current crisis level, and the Emperor has been raising Otosan Uchi tariffs incrementally (now ~15% rather than the 5% baseline) to halt the bleeding - so far without enough success to begin rebuilding.

The ongoing cost of those deployments is also what made it *rational* for the Emperor to fund many of the peace terms personally, out of the Imperial treasury.  The largest single such expenditure was a personal pledge of **5 million koku to Moto Gaheris** - extraordinary not only in size but in being paid in coin, gems, silk, and other valuables rather than grain, which makes its true cost far higher than the raw figure suggests - but it was far from the only one; the Hantei quietly absorbed a long list of lesser treaty provisions as well, though by no means all of them.  The striking thing is that the Emperor paid from a position of *strength*, not weakness.  His goal was to end both wars without taking a military side - which would have alienated a Great Clan and upset the thousand-year balance - and without letting the fighting grind on at ruinous expense.  Much of his work at the negotiating table was the patient demonstration that, to reach a settlement, he could if he chose impose far less favorable terms on every party, and that each of them stood to lose a great deal if he did.

That leverage was concrete.  The **Crane** carried the original fault: it was the Doji vassal house of the **Tsume** that set the disorder in motion by invading Damasu lands and seizing Toshi Ranbo, and both the Tsume and the Crane at large could have been punished far more harshly for it.  The **Lion** finished the wars as nominal victors, holding more land than they began with - and because every Lion samurai swears *two* blood oaths, one to their daimyo and one to the Emperor, the Emperor could have required the Lion to pay for Imperial recognition of those gains, compelling even low-ranking Lion samurai to help enforce the demand on pain of breaking the very oath their daimyo's own authority depends upon.  The **Unicorn** were militarily ascendant but politically brittle: Shinjo Yokatsu had been deposed for religious heresy, and his successor Shinjo Hanari had held the Championship only a few years before the Lion invasion - and owed his survival to Moto Gaheris rather than to his own forces - so the Emperor could have demanded a far larger Unicorn contribution toward appeasing Gaheris and settling with the Lion, under the implicit threat of recognizing some other lineage, house, or Family as the clan's rightful rulers.

In the event, the Emperor and his advisors did extract genuine concessions from each party, and pressed on every signatory some small, pointed term so the lesson could not be missed - but the Hantei nonetheless paid for far more of the settlement than they were strictly obliged to.  That was the deliberate strategy, not weak bargaining: a measured show of strength (an unwelcome condition or two for everyone, proof the throne could compel) wrapped in conspicuous generosity (the throne quietly absorbing the costs), so that each clan came away both reminded of Imperial power and glad to keep participating in the Imperial system as it stands.  The price has been steep - the treasury is now lower than it has been in centuries, low enough to drive the Emperor to the loans and bargains described below on terms he would never otherwise entertain - but it is an understandable trade, and entirely of a piece with the strategy and ethos by which the Hantei have held the center of the Empire for over a thousand years.

Properly understood, then, the depleted treasury is the result of **prudence and long-term thinking, not financial mismanagement**.  In a normal year the Empire runs a healthy surplus - ~4-5M against ~34-36M of revenue - and builds its reserves steadily; the current shortfall is the mark of a dynasty that chose to absorb a generational run of shocks in full rather than appear weak or take sides.  There were, to be fair, some avoidable outlays in the years before the crises, which had already drawn the treasury down to perhaps 60-80% of its usual reserve level - but with no warning of the hard years ahead, that was a reasonable posture rather than a careless one.  (Astute readers may infer, correctly, that the current generation of prophets in the Order of Amaterasu includes no servant of Daikoku, the Fortune of Wealth, of the kind who once let Hantei the Tenth foresee the long-run consequences of fiscal decisions; had one been at court, the Emperor might have been counseled to husband the reserves against the coming years.)  Even a healthy surplus, however, cannot refill a hole this deep in any reasonable span - rebuilding from the current ~10M toward the usual 70-110M would take well over a decade of ordinary saving - so the Hantei have also resorted to measures well outside the ordinary fiscal toolkit.  Two more are current campaign facts:

- **Borrowing from the Lords of the Coin.**  The Emperor has taken on debt from the great merchant-banking concerns - an awkward arrangement for an Imperial house socialized to regard open dealing in money as beneath it, and a quiet signal of just how strained the treasury has become.
- **The Mantis sugarcane concession.**  In exchange for a large immediate payment, the Emperor granted the Mantis a permanent low tax rate on their sugarcane crop and restored their right to a family name.  This trades durable future revenue (and Imperial leverage over a rising minor clan) for cash today - the kind of bargain a fiscally healthy Emperor would never strike, and which the Mantis were only too happy to fund.

Together with the Gaheris pledge, these moves illustrate the structural point: an empire that runs on callable favors and accumulated reserves has few painless options once both the favor-bank and the vaults are depleted.  The fastest paths back to solvency all involve mortgaging the future or borrowing against Imperial prestige.

The principle is illustrated in the following story of Hantei the Tenth, told and retold for centuries in Rokugan as a lesson about the nature of Imperial wealth:

> After being named the first Imperial Treasurer, during a morning meeting with His Imperial Majesty, Yasuki Taka suggested that the Hantei Emperor was being overly generous in the gifts and budgets allocated to his retainers.  Members of every clan were being given lavish budgets far above what they needed to fulfil their duties, well beyond the expected extra which would be needed to secure their gratitude and loyalty.  Taka proposed a "modest" reduction to shore up the Imperial treasury, indicating that he himself would propose an even more severe reduction but had deferred to the Hantei's legendary generosity in his more modest proposal.
>
> Hantei the X considered this, and then named a reduction in budgets more significant than what Taka had proposed, asking what the size of his treasury would be had he established this reduction at the beginning of his reign.
>
> To the amazement of all present, Taka's fingers flew over his abacus, and with only the briefest consultation of his notes and budgets was able to answer the Hantei's question within minutes, summed across all Six Ministries, down to the koku.  Even the Emperor could not conceal his surprised regard for his treasurer's skill.
>
> Hantei the X then smiled and turned to his Miya heralds.  "Go out to the Imperial court and tell all present that Hantei the Tenth requires funds.  Ask what each present can pledge to be delivered to the Imperial palace today.  Not in time, not what funds they can raise with effort, but what they can deliver as a gift by nightfall this very day.  Do not instruct them to make this delivery, merely ask what can be supplied and report back with the totals."
>
> A few more minutes passed, and the Miya heralds returned.  A quick calculation showed that the amount of money pledged was far higher than the increase in the Imperial treasury which Taka's proposal had purported to be worth.  Thus, the greatest money manager in the history of the Empire was humbled by the Hantei's wisdom.

## Land productivity

### Rice and arable-land math

The demographic figures throughout this document (population counts, koku-per-parcel output, rice-production totals) are anchored in real-world historical agricultural data, converted from Chinese units into Rokugan's koku-on-the-rice-standard.

#### Historical units

A few units used in the conversion math:

- ***mu***: a unit of area equal to 1/15 hectare
- ***shi*** (*dan*, 石): the Chinese grain measure, and a slippery one - it took two forms that share the character and changed size by era.  As a *volume* it ran ~59 litres in the Tang dynasty and ~100 litres by modern times (1 *dan* = 10 *dou* = 100 *sheng*, a bit over a bushel); as a *weight* a *dan*/picul was 120 *jin*.  The ~155.168-*jin* figure for a *dan* reflects a *modern* ~100-litre *dan* of *milled* (white) rice: ~77.6 kg, or ~155 *jin* at 0.5 kg per modern *jin*.  That is a *milled* basis, distinct from the brown/unhulled volumetric koku below, whereas the Hunan yield figures below use the smaller *Tang* ~59-litre *dan* - so the word "*shi*" does not denote a single fixed quantity here; watch which era's *dan* a given figure assumes.
- ***jin*** (catty): a unit of weight with two values in play.  The *historical* (Tang-era) catty was ~1.33 lbs (~0.6 kg) and is what the koku conversions below use; the *modern* Chinese *jin* is 0.5 kg, and that is the basis of the twentieth-century Hunan yield figures.
- A traditional reference figure: 3.33 *shi* of rice is enough to feed a person for a year
- **1 koku is ~180 liters** (~48 US gallons, roughly 5 bushels).  The koku's weight depends on milling state: ~150 kg (~330 lb) as the *brown* rice (*genmai*) in which the *kokudaka* system was assessed (the canonical figure), ~136 kg (~300 lb) milled to polished white, and ~187 kg as unhulled paddy.  These standardized koku weights track one harvest losing husk then bran, so they descend across rough, brown, and milled rather than following raw bulk density.  The cross-conversion paths below convert weight to koku-volume at ~138 kg per koku - near the ~136 kg milled-koku weight and ~8% under the ~150 kg brown *kokudaka* koku; that weight-to-volume basis is separate from whether a path also strips milling mass-loss (Path A does, landing in polished terms; Path B does not, staying in unmilled *kokudaka* terms).  Either way, the ~8% slack is absorbed by the deliberately conservative round-number 3,000.

#### Yield reference

Real-world rice yields in twentieth-century Hunan China were 284.40 *jin*/*mu* (a weight, in the modern 0.5-kg *jin*) and 4.00 *shi*/*mu* (a volume, in the Tang ~59-litre *dan*) - both reported figures, each working out to about ~2.1 tons/hectare.  Two independent unit-conversion paths produce a koku-per-square-mile figure consistent with that yield, after applying the deflation factors appropriate to each path's starting figure.  (Path A converts the *jin* figure using the heavier *historical* catty rather than the modern *jin* it was measured in, which inflates the raw figure somewhat before milling loss is applied - one of the era-spanning approximations that make the two-path agreement a magnitude cross-check rather than an exact match.)

Path A (*jin*-based, deflated for milling loss):

```
284.4 jin/mu (early-20th-century Hunan, ~2.1 tons/hectare)
             * 15 mu/hectare
             * 258.998811 hectares/square_mile
             * 1.33 pounds/jin
             * 2.5 cups/pound
             * 0.0625 gallons/cup
             * 0.021 koku/gallon
             = ~4,820 koku per square mile (raw harvested rice)
             * ~0.63 milling factor (rough harvested rice to consumable polished rice, ~37% mass loss)
             = ~3,040 koku per square mile of consumable rice
```

Path B (ton-based, deflated for premodern productivity):

```
4 tons/hectare (modern post-Green-Revolution Hunan yield)
              * 2204.62262 pounds/ton
              * 0.003280 koku/pound
              * 258.998811 hectares/square_mile
              = ~7,490 koku per square mile (modern productivity)
              * ~0.40 premodern productivity deflator (4 t/ha modern -> ~1.6 t/ha empire-wide premodern average)
              = ~3,000 koku per square mile under premodern conditions
```

The two paths apply different implicit deflators because their starting points are different.  Path A's 284.4 *jin*/*mu* is an early-20th-century figure already close to premodern productivity (the Green Revolution had not yet transformed Chinese yields when this measurement was made), so only milling loss needs to be applied to convert harvested rough rice into consumable polished rice.  Path B's 4 tons/hectare is a modern post-Green-Revolution figure, so it requires a much larger deflation to bring it back to historically realistic premodern yields, but no separate milling adjustment - the resulting figure is already in unmilled-koku terms, matching the *kokudaka* convention used throughout these notes.

The two paths land on ~3,000 to ~3,050 koku per square mile.  The agreement is approximate rather than exact - the two endpoints are not on quite the same basis (Path A lands at ~3,040 koku of *consumable, polished* rice, while Path B lands at ~3,000 in the *unmilled* *kokudaka* terms used everywhere else in these notes) - but that is precisely the value of running two independent derivations: starting from different real-world measurements and different conversion routes, they both land in the low thousands once each is reduced to realistic premodern terms - good reassurance that the Rokugani rice estimate is the right general magnitude rather than an artifact of one chain of assumptions.  Downstream calculations use the round-number ~3,000.  That is the more conservative anchor of the two, which suits an empire-wide average; it is also the figure that comes from Path B, whose starting point is a *modern* (post-Green-Revolution) yield - an industrial-era measurement, though of a still largely pre-industrial farming region - that has to be deflated heavily to reach premodern conditions, so leaning on its lower result while noting that the milling-adjusted Path A figure sits just above it (rather than far away) is the cautious reading.  In absolute terms 3,000 sits at the low end of premodern East Asian rice productivity, but the comparison depends on whether one means assessed or actual yield.  It is actually close to Tokugawa Japan's *assessed* prime-paddy grades (~1.1-1.5 koku/*tan*, or ~2,900-3,900 koku/sq mi); it reads as "low" mainly against *actual* harvests, since good Tokugawa paddies yielded ~4,500-5,500 koku/sq mi in practice (well above their assessment) and southern Chinese Yangtze-delta paddies could exceed 5,500 koku/sq mi at the Song-Ming peak.  A deliberately conservative empire-wide average like 3,000 is appropriate because it folds in Rokugan's many marginal-quality paddies in northern, mountain, and frontier regions alongside its prime southern rice country.

#### Historical household-size guidelines

The same ancient Chinese sources provide some calibration on how much land a single household could work:

- 10 *mu* was about the maximum a single landowner could manage on his own; more than that required tenant farmers.
- The classical ~100-*mu* ideal for a household of five (Li Kui, Mencius) is a northern dry-grain figure; intensive wet rice is far more labor-bound, so paddy households work much less.
- 20-30 *mu* was more typical for such a household in crowded metro areas.
- Small household (1-3 members): could work 0.1-5.0 *mu*
- Medium household (4-5 members): could work 5.1-19.5 *mu*
- Large household (8-9 members): could work 20.0-38.5 *mu*

For comparative scale: early Ming China had approximately 40 million hectares of land under cultivation supporting a population of 65 million people.

#### Rokugan arable-land extrapolation

Applying these yields to Rokugan's 1.5 million square miles:

- **15% of Rokugan is arable**: approximately 225,000 square miles total, or ~560 square miles per median-sized domain.
- **4% is suitable for rice farming**: approximately 60,000 square miles total, or ~150 square miles per median-sized domain.  This 4% figure follows imperial Chinese norms (historically ~3-5% of total area, depending on period); Tokugawa Japan's higher ~6% paddy share is not the right anchor for Rokugan, whose continental geography includes mountain ranges, arid borderlands, and frontier regions without close Japanese analogues.

#### Total rice production

At an assumed density of 400 farmers per square mile across Rokugan's ~60,000 sq mi of rice-suitable land:

```
400 farmers/sq mi * 60,000 sq mi = ~24,000,000 farmers on rice-suitable terrain
```

This 24 million is the total farming population living on rice-suitable land.  Of these, roughly 8 million directly work the active wet paddies (the ~1/3 of rice-suitable area under active wet-paddy cultivation in any given year, per the labor-limited utilization frame discussed below); the remaining ~16 million work the supporting hillside soybean and azuki fields whose runoff fertilizes the paddies, the dryland fields for aftercrops and other Five Grains, the small share of upland-rice rotation, and the labor-fallow margins.  Together they constitute the human-economic system of the 60,000 sq mi rice-suitable region.

Annual rice production at 3,000 koku per square mile:

```
3,000 koku/sq mi * 60,000 sq mi = 180,000,000 koku of rice (theoretical maximum at full utilization)
                                * 1/3 (paddy utilization factor, see below)
                                = 60,000,000 koku of rice per year
```

The 1/3 paddy utilization factor reflects the historical reality that wet-rice paddies, once established, can be cropped continuously for centuries without depleting the soil - the flooded paddy fixes atmospheric nitrogen via cyanobacteria, and silt from irrigation water carries in additional nutrients.  The constraint is therefore not soil exhaustion but labor.  Of Rokugan's ~60,000 sq mi of rice-suitable terrain (~150 sq mi per median-sized domain), only about 1/3 (~20,000 sq mi empire-wide, ~50 sq mi per median-sized domain) is actively flooded wet paddy in any given year.  The rest splits roughly into hillside fields growing the soybeans and azuki beans whose runoff and household fertilizer cycling renew the paddies; dryland fields for aftercrops and other Five Grains; a small share given over to upland rice (which does require a multi-year rotation cycle, as the Sparrow Clan's well-documented misfortune demonstrates); and a substantial portion left genuinely fallow because there are not enough farmers to work it.

Note that the 400 farmers/sq mi density is the upper bound, achievable in the best wet-rice paddies; the per-tier population breakdowns elsewhere in this document imply an effective average closer to 300 farmers/sq mi when rice and non-rice land are combined.  This reflects an important historical truth: in most periods and places, farm output was more limited by the number of farmers than the amount of good farmland, and even the prosperous Rokugan (where farming is a punishingly harsh lifestyle by modern standards while being idyllic compared to most historical periods) has large amounts of fallow land in every domain.  In comparative terms, Rokugan's rice-land-per-capita (~600 sq mi per million inhabitants) puts it in roughly the same range as Song and Ming China during their more prosperous and comfortable periods, well below the demographic squeeze of Tokugawa Japan (~310 sq mi per million) or late Qing China (~290-350 sq mi per million).  The Empire has substantial room for population growth into its existing arable base, and the long-run trajectory has been steady expansion: Rokugan a thousand years ago supported only a fraction of its current population, and even allowing for periodic famines and Shadowlands wars, the population continues to grow toward a carrying capacity it is still well short of.

#### Other per-domain derivations

A few smaller calculations that anchor the per-parcel and per-family numbers used elsewhere in this document:

**County and domain family counts**: a county has `156 families (town) + 6 * 70 families per village + 36 * 15 families per hamlet = 1,116 farming families`.  A domain has `36 * 1,116 = 40,176` farming families.

**Average koku per family**: a domain has ~250,000 population, and assuming ~2 koku worth of food per person, that's `500,000 koku per year / 40,176 families ~= 12.45 koku per family`.  This rounds up to ~15 koku per family on average, reflecting a typical surplus.

**Merchant land allocation**: if each "merchant, other" family owned a single parcel, that would total `(12 * 36) + (90 * 6) + 360 = 1,332 parcels = 3.32% of the domain`.  The total number of "merchant, rich" families per domain is `(36 * 2.4) + (6 * 18) + 72 = 266`, and "merchant, very rich" is `(6 * 12) + 48 = 120`.  Assuming roughly 5,000 parcels are owned by samurai, that leaves `40,176 - 1,332 - 5,000 = 33,844 parcels` for distribution among the merchant families.

**Government-officials count**: across a domain's 7 cities (one capital plus six provincial cities), each of the 6 Ministries has a Minister and a Deputy Minister, so `2 * 6 * 7 = 84 ministers and deputy ministers`.  Adding the 6 chancellors on the House council brings the domain's senior officialdom to roughly 90 samurai.  If each comes from a different immediate family, that represents about 9% of the domain's samurai families.

### Unit conversions: land area to rice koku

| Unit | Area | Yield (koku) |
| --- | --- | --- |
| Square mile | 1 | 3000 |
| Acre | 1 | 4.69 |
| Mu | 1 | 0.77 |
| Hectare | 1 | 11.58 |

### Per-family reference

| Family | Acres | Koku |
| --- | --- | --- |
| 1 | 2 | 9.38 |

### Farm families by tier (per domain)

These are the farming households living inside each settlement type (per the caste percentages elsewhere in this document).  Capital and provincial cities have no in-walls farmers - the fertile land surrounding them is worked by villagers counted under the rural tiers.

| Tier | Settlements (N) | Farm families per settlement | Total farm families |
| --- | --- | --- | --- |
| Capital city | 1 | 0 | 0 |
| Provincial city | 6 | 0 | 0 |
| Town | 36 | 156 | 5,616 |
| Village | 216 | 70 | 15,120 |
| Hamlet | 1,296 | 15 | 19,440 |
| **Total** |  |  | **40,176** |

### Arable land allocation (per domain)

This table describes the **land available** in a median domain, not the land actively cropped in a given year (see the labor-limited note below).  Shares follow [Rokugan arable-land extrapolation](#rokugan-arable-land-extrapolation): 15% of total land is arable, of which 4% (of total) is rice-suitable and the remaining 11% is non-rice arable.

| Type | Total domain land (sq mi) | Arable share | Arable area (sq mi) | In acres |
| --- | --- | --- | --- | --- |
| Rice-suitable | 3,750 | 4% | 150 | 96,000 |
| Non-rice arable | 3,750 | 11% | 412.5 | 264,000 |
| **Total arable** | 3,750 | 15% | 562.5 | 360,000 |

**Note on labor utilization (not land utilization)**: Rokugan is currently **labor-limited, not land-limited** (per [Total rice production](#total-rice-production)).  Of the 150 sq mi of rice-suitable land in a median domain, only about **1/3 (~50 sq mi) is in active wet-paddy production** in any given year - that ~50 sq mi yields ~50 × 3,000 = **~150,000 koku of rice per median domain** (which is exactly the canonical empire-wide ~60M koku ÷ 400 median domains).  The other ~2/3 of rice-suitable land, plus the non-rice arable, grows the supporting hillside soybean and azuki fields, dryland aftercrops and other Five Grains, a small share of upland rice in multi-year rotation, and a substantial portion left genuinely fallow because there are not enough farmers to work it.  The constraint is wet-paddy labor, not soil: an established paddy can be cropped continuously for centuries (the flooded field fixes nitrogen and silt renews nutrients), so the latent rice-suitable land would come under the plow as population grows.  The ~40,176 farm families of the domain (per [Farm families by tier](#farm-families-by-tier-per-domain) above) work this land; for tax purposes the median family's output is reckoned at ~15 koku (taxed at 1/3 = ~5 koku), per [l7r.md - Rent and taxes](l7r.md#rent-and-taxes).

**Assessed *kokudaka* vs. actual output, and fallow land**: Rokugani land tax *and* feudal kick-ups are both reckoned on the **assessed** value of designated farmland - the *kokudaka* - not on each year's actual harvest, exactly as in Tokugawa Japan's *jomen* system.  The median domain's assessed *kokudaka* is **~602,640 koku** (the ~40,176 farm families x ~15 koku reckoned output), and this is the base against which the 1/3 land tax (~200,880) and every land-output kick-up are computed.  Because assessments are deliberately conservative and reassessed only infrequently, **actual gross output runs higher - on the order of ~775,000 koku of worked land in a good year** - and the surplus above the assessment is kept by the farmers (the very incentive that makes them work harder).  So ~775,000 is the actual physical harvest, not the obligation base: obligations ride on the ~602,640 assessment.  Fallow land follows the same logic.  The bulk of a domain's uncultivated land is **latent land that has never been designated or assessed** (the labor-limited margin - there are simply not enough farmers to work it), so it is **outside the *kokudaka* and untaxed**, which is why the assessed base sits so far below the land's theoretical ceiling.  Land that *was* once assessed and then falls fallow, by contrast, **stays on the rolls and keeps owing its tax** (removable only through a deliberately difficult formal wasteland reclassification) - the standing incentive to keep it cultivated, the reason magistrates and governors run reclamation projects (Japan's *shinden kaihatsu*, China's *kenhuang* wasteland-opening campaigns) to bring latent land onto the *kokudaka*, and the reason a merchant landholder may try to offload tax-burdened fallow plots on the domain's land market.

### Rice productivity by land quality

| Land | k/ha | k/mi² | P (share) | Proportional production | k/acre |
| --- | --- | --- | --- | --- | --- |
| High | 20 | 5180 | 0.27 | 1398.60 | 8.09 |
| Medium | 15 | 3885 | 0.17 | 660.45 | 6.07 |
| Med-low | 11.4 | 2952.6 | 0.17 | 501.94 | 4.61 |
| Low | 8 | 2072 | 0.30 | 621.60 | 3.24 |
| Awful | 5.4 | 1398.6 | 0.09 | 125.87 | 2.19 |
| **Total** |  |  | **1.00** | **3308.46** |  |
| Average | 12.77 | 3308.46 |  | 3308.46 |  |

The land-quality shares sum to 1.00; the weighted-average ~3,300 koku/sq mi sits just above the ~3,000-3,050 two-path derivation in [Yield reference](#yield-reference) - the same low-thousands magnitude - and downstream calculations use the conservative round-number 3,000 koku/sq mi.

### Wheat productivity by land quality

| Land | bush/acre | bush/ha | bush/mi² | koku/ha | koku/mi² | koku/acre |
| --- | --- | --- | --- | --- | --- | --- |
| High | 50 | 123.55 | 32000 | 17.65 | 4571.43 | 7.14 |
| Medium | 40 | 98.84 | 25600 | 14.12 | 3657.14 | 5.71 |
| Med-low | 30 | 74.13 | 19200 | 10.59 | 2742.86 | 4.29 |
| Low | 20 | 49.42 | 12800 | 7.06 | 1828.57 | 2.86 |
| Awful | 10 | 24.71 | 6400 | 3.53 | 914.29 | 1.43 |

Wheat reference: 1 bushel of wheat = 60 lbs = 55 loaves of bread. 1 koku of rice ≈ 7 bushels of wheat.
