# SEO Fixes Detailed - SKY United Website

**Status:** Pending  
**Priority:** High  
**Created:** 2026-06-04

---

## Phase 1: HIGH PRIORITY - H1 Tags (16 pages)

### 1. news.html

| Element | Before | After | Note |
|---------|--------|-------|------|
| **H1 tag** | ❌ Missing | ✅ Add: `<h1>ข่าวสาร</h1>` | Add below hero title |
| **Location** | N/A | Section `.section-block[data-section="why-from-pdf"]` after heading | Make it H1 instead of H2 |

---

### 2. products/moisture-barrier-bags.html

| Element | Before | After | Note |
|---------|--------|-------|------|
| **H1 tag** | ❌ Missing | ✅ Add: `<h1>Moisture Barrier Bags</h1>` | In product-detail-hero section |
| **Location** | N/A | Before product description | Dynamic render - add to hero section |

---

### 3. products/anti-static-gloves.html

| Element | Before | After | Note |
|---------|--------|-------|------|
| **H1 tag** | ❌ Missing | ✅ Add: `<h1>Anti-Static Gloves</h1>` | In product-detail-hero section |

---

### 4-16. Other Product Detail Pages (13 pages)

**Apply same pattern to all product pages:**

- products/static-shielding-bags.html → `<h1>Static Shielding Bags</h1>`
- products/cleanroom-ldpe-bags.html → `<h1>Cleanroom LDPE Bags</h1>`
- products/cleanroom-hdpe-bags.html → `<h1>Cleanroom HDPE Bags</h1>`
- products/vacuum-nylon-packaging-bags.html → `<h1>Vacuum Nylon Packaging Bags</h1>`
- products/humidity-indicator-cards.html → `<h1>Humidity Indicator Cards</h1>`
- products/anti-static-air-bubble-packaging.html → `<h1>Anti-Static Air Bubble Packaging</h1>`
- products/protective-cushioning-wrap.html → `<h1>Protective Cushioning Wrap</h1>`
- products/sulfur-free-paper.html → `<h1>Sulfur-Free Paper</h1>`
- products/cleanroom-cotton-swabs.html → `<h1>Cleanroom Cotton Swabs</h1>`
- products/cleanroom-foam-swabs.html → `<h1>Cleanroom Foam Swabs</h1>`
- products/anti-static-cleanroom-wipers.html → `<h1>Anti-Static Cleanroom Wipers</h1>`
- products/cleanroom-garments-suits.html → `<h1>Cleanroom Garments & Suits</h1>`
- products/gloves.html → `<h1>Anti-Static Gloves & Latex Gloves</h1>`

| Element | Before | After | Note |
|---------|--------|-------|------|
| **H1 tag (all 13 pages)** | ❌ Missing | ✅ Add product name H1 | In hero section, above description |

---

## Phase 2: MEDIUM PRIORITY - Meta Descriptions & Titles

### contact.html

| Element | Before | After | Character Count |
|---------|--------|-------|-----------------|
| **Meta Description** | `ติดต่อเรา - บริษัท สกาย ยูไนเต็ด อินดัสเทรียล` | ❌ Too short (48 chars) | Should be 120-155 |
| **Better version** | Current | `ติดต่อเรา - บริษัท สกาย ยูไนเต็ด อินดัสเทรียล (ประเทศไทย) จำกัด อีเมล โทร ที่อยู่ พร้อมแผนที่ Google` | ✅ 125 chars |
| **Location** | `<head>` | Replace in `<meta name="description">` | |

---

### news.html

| Element | Before | After | Character Count |
|---------|--------|-------|-----------------|
| **Meta Description** | `ข่าวสาร - บริษัท สกาย ยูไนเต็ด อินดัสเทรียล` | ❌ Too short (49 chars) | Should be 120-155 |
| **Better version** | Current | `ข่าวสาร - บริษัท สกาย ยูไนเต็ด อินดัสเทรียล ข้อมูลเกี่ยวกับบรรจุภัณฑ์ ESD และห้องคลีนรูม` | ✅ 98 chars (acceptable) |
| **Alternative** | Current | `ข่าวและบทความเกี่ยวกับบรรจุภัณฑ์ ESD การป้องกันไฟฟ้าสถิต และโซลูชันอุตสาหกรรมจากสกาย ยูไนเต็ด` | ✅ 116 chars |
| **Location** | `<head>` | Replace in `<meta name="description">` | |

---

### index.html

| Element | Before | After | Character Count |
|---------|--------|-------|-----------------|
| **Title Tag** | `บริษัท สกาย ยูไนเต็ด อินดัสเทรียล (ประเทศไทย) จำกัด` | ⚠️ Long (71 chars) | Ideal: 50-60 chars |
| **Better version** | Current | `ESD Packaging Manufacturer Thailand - SKY United Industrial` | ✅ 60 chars (English version) |
| **Thai alternative** | Current | `สกาย ยูไนเต็ด - บรรจุภัณฑ์ ESD ไทย` | ✅ 39 chars |
| **Location** | `<head>` | Update `<title>` tag | Keep Thai OR use shorter version |

---

## Phase 3: MEDIUM PRIORITY - Alt Text Improvements

### Product Detail Pages Gallery Images

**Issue:** Alt text uses file names instead of descriptive text

**Affected pages:** 
- products/mbb.html (10 images)
- products/moisture-barrier-bags.html (10 images)
- products/ssb.html (10 images)
- products/ldpe-hdpe.html (10 images)
- products/vacuum-nylon.html (10 images)
- products/hic.html (10 images)
- products/air-bubble.html (10 images)
- products/cushion-wrap.html (10 images)
- products/sulfur-free-paper.html (10 images)
- products/cotton-swabs.html (10 images)
- products/foam-swabs.html (10 images)
- products/wipers.html (10 images)
- products/garments.html (10 images)
- products/gloves.html (10 images)

**Example - products/mbb.html:**

| Image | Before | After |
|-------|--------|-------|
| Image 1 | `alt="mbb-1.png"` | `alt="Moisture Barrier Bags MBB - Product gallery shot 1"` |
| Image 2 | `alt="mbb-2.png"` | `alt="Moisture Barrier Bags MBB - Product gallery shot 2"` |
| Image 3-10 | `alt="mbb-3.png"` ... | `alt="Moisture Barrier Bags MBB - Product gallery shot 3"` ... |

**Pattern to apply:** 
- Replace: `alt="[filename]"`
- With: `alt="[Product Name] - Product gallery shot [N]"` or `alt="[Product Name] - Packaging sample [N]"`

**Total images to update:** ~140 images across 14 product pages

---

## Phase 4: OPTIONAL - Future Enhancements

### Sitemap.xml
- Create `/sitemap.xml` with all 25+ pages
- Submit to Google Search Console

### Internal Linking Strategy
- Add contextual links in product descriptions pointing to related products
- Link product pages from About page
- Add breadcrumb navigation in product detail pages

### Content Enhancement
- Expand meta descriptions on all product pages (currently 65-100 chars, good)
- Add schema.org structured data (JSON-LD) for products
- Consider adding FAQ section on products

---

## Implementation Checklist

### Phase 1: H1 Tags (HIGH)
- [ ] news.html - add H1
- [ ] products/moisture-barrier-bags.html - add H1
- [ ] products/anti-static-gloves.html - add H1
- [ ] Other 13 product pages - add H1
- [ ] Test: Each page has exactly 1 H1

### Phase 2: Meta & Titles (MEDIUM)
- [ ] contact.html - expand meta description
- [ ] news.html - expand meta description
- [ ] index.html - consider shortening title (optional)
- [ ] Test: All descriptions 120-155 chars (except news, 98+ acceptable)

### Phase 3: Alt Text (MEDIUM)
- [ ] Update product gallery alt text (14 pages × 10 images = 140 images)
- [ ] Test: All `alt="..."` descriptive, not file names

### Phase 4: Future (LOW)
- [ ] Create sitemap.xml
- [ ] Add schema.org structured data
- [ ] Expand blog/news content

---

## Testing Steps

After fixes, verify with:

1. **Google Search Console** - Check for indexing issues
2. **Chrome DevTools** - Inspect H1 tags, meta tags
3. **Lighthouse** - Run SEO audit
4. **Mobile-Friendly Test** - Ensure mobile SEO compatibility

---

## Files to Modify

| File | Changes | Type |
|------|---------|------|
| news.html | Add H1, expand meta | HTML |
| contact.html | Expand meta description | HTML |
| index.html | Shorten title (optional) | HTML |
| products/moisture-barrier-bags.html | Add H1, update 10 alt texts | HTML |
| products/anti-static-gloves.html | Add H1, update 10 alt texts | HTML |
| 12 other product pages | Add H1, update 10 alt texts each | HTML |

---

## Notes

- All changes are **additive** (no deletions)
- H1 tags should appear **once per page** (verify existing content)
- Meta descriptions: 120-155 characters ideal (Google shows 155-160 on desktop, 120 on mobile)
- Alt text: Use natural language, include product name + context
- Test in Google Search Console before and after
