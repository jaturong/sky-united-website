#!/usr/bin/env python3
"""Generate individual product detail pages for SKY United Industrial website."""

import os

BASE = "/Users/jaturong/Desktop/Claude-folder/sky-united-website/products"

# ─────────────────────────────────────────────────────────────────────────────
# HEADER / FOOTER TEMPLATES
# ─────────────────────────────────────────────────────────────────────────────

def header(title_th, title_en):
    return f'''<!doctype html>
<html lang="th">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title_en} | SKY United Industrial</title>
    <meta name="description" content="{title_th} - บริษัท สกาย ยูไนเต็ด อินดัสเทรียล">
    <meta property="og:title" content="{title_en} | SKY United Industrial">
    <meta property="og:type" content="website">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../assets/css/base.css">
    <link rel="stylesheet" href="../assets/css/layout.css">
    <link rel="stylesheet" href="../assets/css/components.css">
    <link rel="stylesheet" href="../assets/css/pages.css">
    <link rel="stylesheet" href="../assets/css/animations.css">
  </head>
  <body data-page="product-detail">
    <a class="skip-link" href="#main" data-i18n="global.skip">ข้ามไปยังเนื้อหา</a>
    <header class="site-header" data-component="site-header">
      <nav class="nav-shell" aria-label="Main navigation">
        <a class="brand-mark" href="../index.html" aria-label="SKY UNITED INDUSTRIAL home">
          <img src="../assets/images/logo/sky-united-industrial-logo-sm.png" alt="SKY UNITED INDUSTRIAL" class="brand-logo">
          <span>
            <strong data-i18n="global.brandShort">SKY United Industrial</strong>
            <small data-i18n="global.brandType">ผู้นำด้านบรรจุภัณฑ์ไฮเทคและการป้องกันไฟฟ้าสถิตย์ระดับอุตสาหกรรม</small>
          </span>
        </a>
        <div class="nav-links" aria-label="Primary pages">
          <a href="../index.html" data-i18n="nav.home">หน้าหลัก</a>
          <a href="../about.html" data-i18n="nav.about">เกี่ยวกับเรา</a>
          <a href="../products.html" data-i18n="nav.products">ผลิตภัณฑ์</a>
          <a href="../news.html" data-i18n="nav.news">ข่าวสาร</a>
          <a href="../contact.html" data-i18n="nav.contact">ติดต่อเรา</a>
        </div>
        <button class="hamburger" type="button" aria-label="Toggle navigation" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
        <div class="nav-actions">
          <button class="language-pill" type="button" aria-label="Switch language" data-language-toggle>EN</button>
        </div>
      </nav>
      <nav class="mobile-nav" aria-label="Mobile navigation">
        <a href="../index.html" data-i18n="nav.home">หน้าหลัก</a>
        <a href="../about.html" data-i18n="nav.about">เกี่ยวกับเรา</a>
        <a href="../products.html" data-i18n="nav.products">ผลิตภัณฑ์</a>
        <a href="../news.html" data-i18n="nav.news">ข่าวสาร</a>
        <a href="../contact.html" data-i18n="nav.contact">ติดต่อเรา</a>
        <button class="language-pill mobile-nav-lang" type="button" aria-label="Switch language" data-language-toggle>EN</button>
      </nav>
    </header>
    <main id="main">'''

FOOTER = '''    </main>
    <footer class="site-footer" data-component="site-footer">
      <div class="footer-shell">
        <div class="footer-content">
          <div class="footer-column--brand">
            <h3 class="footer-brand-title" data-i18n="footer.company">บริษัท สกาย ยูไนเต็ด อินดัสเทรียล (ประเทศไทย) จำกัด</h3>
            <p class="footer-brand-subtitle" data-i18n="global.brandType">ผู้นำด้านบรรจุภัณฑ์ไฮเทคและการป้องกันไฟฟ้าสถิตย์ระดับอุตสาหกรรม</p>
            <p class="footer-brand-description" data-i18n="home.hero.description">ผลิตและจำหน่ายวัสดุบรรจุภัณฑ์พลาสติกเพื่อใช้ในอุตสาหกรรม</p>
          </div>
          <div class="footer-column--contact">
            <h3 class="footer-heading" data-i18n="footer.heading">ติดต่อเรา</h3>
            <p class="footer-company-name" data-i18n="footer.company">บริษัท สกาย ยูไนเต็ด อินดัสเทรียล (ประเทศไทย) จำกัด</p>
            <p class="footer-location-full" data-i18n="footer.locationFull">จังหวัดพระนครศรีอยุธยา, ประเทศไทย</p>
            <div class="footer-contact-items">
              <div class="footer-contact-item">
                <span class="footer-label" data-i18n="footer.email.label">Email:</span>
                <a href="mailto:Sales@skyunitedindustrial.com" class="footer-value">Sales@skyunitedindustrial.com</a>
              </div>
              <div class="footer-contact-item">
                <span class="footer-label" data-i18n="footer.phone.label">โทร:</span>
                <a href="tel:0996536354" class="footer-value">099-653-6354</a>
              </div>
              <div class="footer-contact-item">
                <span class="footer-label" data-i18n="footer.website.label">เว็บไซต์:</span>
                <a href="https://www.skyunitedindustrial.com" class="footer-value">www.skyunitedindustrial.com</a>
              </div>
            </div>
          </div>
        </div>
        <p class="footer-copyright" data-i18n="footer.copyright">© 2026 SKY United Industrial (Thailand) Co., Ltd. สงวนลิขสิทธิ์ทั้งหมด</p>
      </div>
    </footer>
    <script src="../assets/js/main.js" defer></script>
    <script src="../assets/js/animations.js" defer></script>
    <script src="../assets/js/i18n.js" defer></script>
  </body>
</html>'''

# ─────────────────────────────────────────────────────────────────────────────
# TABLE BUILDER
# ─────────────────────────────────────────────────────────────────────────────

def missing_block(heading_th, heading_en):
    return f'''      <div class="prod-info-block">
        <h2 class="data-missing lth">{heading_th}</h2>
        <h2 class="data-missing len">{heading_en}</h2>
        <div class="prod-info-missing">
          <span class="lth">⚠️ ยังไม่มีข้อมูลในส่วนนี้ — จะเพิ่มเติมในภายหลัง</span>
          <span class="len">⚠️ Data not yet available — will be updated soon</span>
        </div>
      </div>'''

def table_block(heading_th, heading_en, col2_th, col2_en, col3_th, col3_en, col4_th, col4_en, rows):
    rows_html = ""
    for i, row in enumerate(rows, 1):
        c2th, c2en, c3th, c3en, c4th, c4en = row
        rows_html += f'''          <tr>
            <td>{i}</td>
            <td><span class="lth">{c2th}</span><span class="len">{c2en}</span></td>
            <td><span class="lth">{c3th}</span><span class="len">{c3en}</span></td>
            <td><span class="lth">{c4th}</span><span class="len">{c4en}</span></td>
          </tr>\n'''
    return f'''      <div class="prod-info-block">
        <h2 class="lth">{heading_th}</h2>
        <h2 class="len">{heading_en}</h2>
        <div class="prod-table-wrapper">
          <table class="prod-table">
            <thead>
              <tr>
                <th>#</th>
                <th><span class="lth">{col2_th}</span><span class="len">{col2_en}</span></th>
                <th><span class="lth">{col3_th}</span><span class="len">{col3_en}</span></th>
                <th><span class="lth">{col4_th}</span><span class="len">{col4_en}</span></th>
              </tr>
            </thead>
            <tbody>
{rows_html}          </tbody>
          </table>
        </div>
      </div>'''

# ─────────────────────────────────────────────────────────────────────────────
# GALLERY BUILDER
# ─────────────────────────────────────────────────────────────────────────────

def gallery_section(image_path, count=6):
    items = f'''          <div class="prod-gallery-item">
            <img src="../assets/images/products/{image_path}" alt="Product image">
          </div>\n'''
    for _ in range(count - 1):
        items += '''          <div class="prod-gallery-item">
            <div class="prod-gallery-placeholder">
              <span class="lth">เร็วๆ นี้</span>
              <span class="len">Coming Soon</span>
            </div>
          </div>\n'''
    return f'''      <section class="section-block prod-gallery-section" data-section="prod-gallery">
        <div class="page-shell">
          <p class="eyebrow">Gallery</p>
          <h2 class="lth">รูปภาพสินค้า</h2>
          <h2 class="len">Product Gallery</h2>
          <div class="prod-gallery-grid">
{items}          </div>
        </div>
      </section>'''

# ─────────────────────────────────────────────────────────────────────────────
# PAGE BUILDER
# ─────────────────────────────────────────────────────────────────────────────

def build_page(p):
    desc_th_html = "".join(f'          <p class="lth">{para}</p>\n' for para in p['desc_th'])
    desc_en_html = "".join(f'          <p class="len">{para}</p>\n' for para in p['desc_en'])

    types_html  = p.get('types_block', missing_block('ประเภทสินค้าที่มีจำหน่าย', 'Available Types'))
    feat_html   = p.get('feat_block',  missing_block('คุณสมบัติเด่น', 'Key Features'))
    app_html    = p.get('app_block',   missing_block('การใช้งาน', 'Applications'))

    gallery_html = gallery_section(p['image'])

    return f'''{header(p['subtitle_th'], p['name'])}

      <!-- HERO -->
      <section class="section-block prod-page-hero" data-section="prod-hero">
        <div class="page-shell">
          <a href="../products.html" class="back-link">
            <span class="lth">← ผลิตภัณฑ์ทั้งหมด</span>
            <span class="len">← All Products</span>
          </a>
          <span class="prod-category-badge lth">{p['cat_th']}</span>
          <span class="prod-category-badge len">{p['cat_en']}</span>
          <h1>{p['name']}</h1>
          <p class="prod-thai-subtitle lth">{p['subtitle_th']}</p>
        </div>
      </section>

      <!-- DESCRIPTION -->
      <section class="section-block" data-section="prod-desc">
        <div class="page-shell">
          <div class="prod-desc-grid">
            <div class="prod-desc-img">
              <img src="../assets/images/products/{p['image']}" alt="{p['name']}">
            </div>
            <div class="prod-desc-text">
{desc_th_html}{desc_en_html}            </div>
          </div>
        </div>
      </section>

      <!-- INFO TABLES -->
      <section class="section-block prod-tables-section" data-section="prod-tables">
        <div class="page-shell">
          <p class="eyebrow lth">ข้อมูลรายละเอียด</p>
          <p class="eyebrow len">Product Information</p>
{types_html}
{feat_html}
{app_html}
          <!-- Comparison Table: Coming Soon -->
        </div>
      </section>

      <!-- GALLERY -->
{gallery_html}

{FOOTER}'''

# ─────────────────────────────────────────────────────────────────────────────
# PRODUCT DATA
# ─────────────────────────────────────────────────────────────────────────────

DASH = "—"

# Helper: col tuple (TH, EN, detail_TH, detail_EN, note_TH, note_EN)
def row(c2th, c2en, c3th=DASH, c3en=DASH, c4th=DASH, c4en=DASH):
    return (c2th, c2en, c3th, c3en, c4th, c4en)

# ── MBB ──────────────────────────────────────────────────────────────────────
mbb = {
    'slug': 'mbb',
    'name': 'Moisture Barrier Bags (MBB)',
    'subtitle_th': 'ถุงป้องกันความชื้นและไฟฟ้าสถิต',
    'cat_th': 'โซลูชันบรรจุภัณฑ์ ESD',
    'cat_en': 'ESD Packaging Solutions',
    'image': 'mbb/mbb-1.png',
    'desc_th': [
        'ถุงป้องกันความชื้นและไฟฟ้าสถิต (MBB) หรือที่รู้จักกันในชื่อ ถุงกันความชื้น ESD หรือ ถุงฟอยล์อลูมิเนียม ถูกออกแบบมาเพื่อปกป้องชิ้นส่วนอิเล็กทรอนิกส์ที่บอบบางและไวต่อสิ่งกระตุ้นจากความชื้น การคายประจุไฟฟ้าสถิต (ESD) ฝุ่น และการปนเปื้อนต่างๆ',
        'ผลิตภัณฑ์ MBB ของเราถูกนำไปใช้งานอย่างแพร่หลายในบรรจุภัณฑ์สำหรับเซมิคอนดักเตอร์ บรรจุภัณฑ์แผ่นวงจรพิมพ์ (PCB) รวมถึงบรรจุภัณฑ์สำหรับชิ้นส่วนที่ไวต่อไฟฟ้าสถิต เพื่อมอบการปกป้องที่เชื่อถือได้สำหรับอุตสาหกรรมไฮเทค',
        'ในฐานะผู้ให้บริการโซลูชันบรรจุภัณฑ์ ESD และบรรจุภัณฑ์คลีนรูมที่ได้รับความไว้วางใจ บริษัท สกาย ยูไนเต็ด อินดัสเทรียล (ประเทศไทย) จำกัด ผลิตถุงป้องกันความชื้นคุณภาพสูงในประเทศไทย ด้วยคุณภาพที่เสถียร ระยะเวลาในการผลิตที่รวดเร็ว (Lead time) และเป็นไปตามมาตรฐานการผลิตในห้องคลีนรูม',
        'ถุงป้องกันความชื้น (MBB) ประสิทธิภาพสูง ได้รับการออกแบบมาเพื่อปกป้องชิ้นส่วนอิเล็กทรอนิกส์ที่บอบบางจากความชื้น ความชื้นสัมพัทธ์ ปฏิกิริยาออกซิเดชัน (สนิม/สารเคลือบหมอง) และการปนเปื้อน ตลอดกระบวนการจัดเก็บและการขนส่ง',
    ],
    'desc_en': [
        'Moisture Barrier Bags (MBB Bags), also known as ESD Moisture Barrier Bags or Aluminum Foil Bags, are designed to protect sensitive electronic components from moisture, electrostatic discharge (ESD), dust, and contamination.',
        'Widely used in Semiconductor Packaging, PCB Packaging, and Static Sensitive Component Packaging, our MBB products provide reliable protection for high-tech industries.',
        'As a trusted provider of ESD Packaging Solutions and Cleanroom Packaging, SKY United Industrial (Thailand) Co., Ltd. manufactures high-quality Moisture Barrier Bags in Thailand with stable quality, fast lead time, and cleanroom production standards.',
        'High-performance Moisture Barrier Bag (MBB) designed to protect sensitive electronic components from moisture, humidity, oxidation, and contamination throughout storage and transportation.',
    ],
    'feat_block': table_block(
        'คุณสมบัติเด่น', 'Key Features',
        'คุณสมบัติ', 'Feature',
        'รายละเอียด', 'Details',
        'หมายเหตุ', 'Note',
        [
            row('Cleanroom Manufactured', 'Cleanroom Manufactured', 'ผลิตภายในห้องคลีนรูมที่ได้มาตรฐาน', 'Manufactured in certified cleanroom conditions'),
            row('High Barrier Aluminum Layer', 'High Barrier Aluminum Layer', 'ชั้นฟอยล์อลูมิเนียมที่มีคุณสมบัติในการป้องกันสูง', 'High-barrier aluminum foil layer for superior protection'),
            row('ESD &amp; Moisture Protection', 'ESD &amp; Moisture Protection', 'ปกป้องทั้งไฟฟ้าสถิตและกันความชื้น', 'Dual protection against ESD and moisture'),
            row('Factory Direct Supply from Thailand', 'Factory Direct Supply from Thailand', 'ส่งตรงจากโรงงานผู้ผลิตในประเทศไทย', 'Direct supply from our Thailand manufacturing facility'),
        ]
    ),
}

# ── SSB ──────────────────────────────────────────────────────────────────────
ssb = {
    'slug': 'ssb',
    'name': 'Static Shielding Bags (SSB)',
    'subtitle_th': 'ถุงป้องกันไฟฟ้าสถิต (ถุงชีลด์)',
    'cat_th': 'โซลูชันบรรจุภัณฑ์ ESD',
    'cat_en': 'ESD Packaging Solutions',
    'image': 'ssb/ssb-1.png',
    'desc_th': [
        'ถุงป้องกันไฟฟ้าสถิต (Static Shielding Bags: SSB) หรือที่เรียกว่า ถุงป้องกัน ESD หรือถุงกันไฟฟ้าสถิต ถูกออกแบบมาเป็นพิเศษเพื่อปกป้องชิ้นส่วนอิเล็กทรอนิกส์ที่มีความไวต่อไฟฟ้าสถิต จากการคายประจุไฟฟ้าสถิต (ESD) ไฟฟ้าสถิต ฝุ่น และความเสียหายระหว่างการจัดเก็บและการขนส่ง',
        'ถุง SSB ถูกใช้อย่างแพร่หลายในงานบรรจุภัณฑ์เซมิคอนดักเตอร์ บรรจุภัณฑ์ PCB ฮาร์ดดิสก์ (HDD) IC และการบรรจุชิ้นส่วนอิเล็กทรอนิกส์ที่ไวต่อไฟฟ้าสถิตอื่นๆ ซึ่งจำเป็นต้องมีการป้องกัน ESD ที่เชื่อถือได้',
        'ผลิตจากวัสดุนำไฟฟ้าและวัสดุป้องกันไฟฟ้าสถิต ผลิตภัณฑ์ SSB ของเราช่วยปกป้องอุปกรณ์อิเล็กทรอนิกส์ได้อย่างมีประสิทธิภาพ พร้อมรองรับมาตรฐานคลีนรูมและข้อกำหนดด้านบรรจุภัณฑ์อุตสาหกรรม',
        'บริษัท สกาย ยูไนเต็ด อินดัสเทรียล (ประเทศไทย) จำกัด ผลิตถุงกันไฟฟ้าสถิตคุณภาพสูงในประเทศไทย ด้วยคุณภาพที่สม่ำเสมอ ระยะเวลาจัดส่งรวดเร็ว และมาตรฐานการผลิตระดับคลีนรูม',
    ],
    'desc_en': [
        'Static Shielding Bags (SSB), also known as ESD Shielding Bags or Anti-Static Shielding Bags, are specially designed to protect sensitive electronic components from electrostatic discharge (ESD), static electricity, dust, and handling damage during storage and transportation.',
        'SSB bags are widely used in Semiconductor Packaging, PCB Packaging, HDD, IC, and other Static Sensitive Component Packaging applications where reliable ESD protection is essential.',
        'Manufactured using conductive and static shielding materials, our SSB products provide effective protection for electronic devices while supporting cleanroom and industrial packaging requirements.',
        'As a trusted provider of ESD Packaging Solutions and Cleanroom Packaging, SKY United Industrial (Thailand) Co., Ltd. manufactures high-quality Anti-Static Bags in Thailand with stable quality, fast lead time, and cleanroom production standards.',
    ],
    'feat_block': table_block(
        'คุณสมบัติเด่น', 'Key Features',
        'คุณสมบัติ', 'Feature',
        'รายละเอียด', 'Details',
        'หมายเหตุ', 'Note',
        [
            row('การป้องกันไฟฟ้าสถิต', 'Static Shielding Protection', 'ป้องกันการคายประจุไฟฟ้าสถิต (ESD)', 'Protects against electrostatic discharge (ESD)'),
            row('คลีนรูมที่ผลิต', 'Cleanroom Manufactured', 'ผลิตภายในห้องคลีนรูมที่ได้มาตรฐาน', 'Manufactured in certified cleanroom conditions'),
            row('เหมาะสำหรับ PCB / เซมิคอนดักเตอร์ / ฮาร์ดดิสก์', 'Suitable for PCB / Semiconductor / HDD', 'ครอบคลุมการใช้งานในอุตสาหกรรมอิเล็กทรอนิกส์หลัก', 'Covers major electronics industry applications'),
            row('ผู้จัดจำหน่ายตรงจากโรงงานในประเทศไทย', 'Factory Direct Supplier in Thailand', 'ส่งตรงจากโรงงานผู้ผลิตในประเทศไทย', 'Direct supply from our Thailand manufacturing facility'),
        ]
    ),
}

# ── LDPE / HDPE ───────────────────────────────────────────────────────────────
ldpe = {
    'slug': 'ldpe-hdpe',
    'name': 'Cleanroom LDPE &amp; HDPE Bags',
    'subtitle_th': 'ถุงพลาสติกสำหรับใช้ในห้องคลีนรูม',
    'cat_th': 'โซลูชันบรรจุภัณฑ์ ESD',
    'cat_en': 'ESD Packaging Solutions',
    'image': 'ldpe/ldpe-hdpe-1.png',
    'desc_th': [
        'ถุง LDPE และ HDPE สำหรับห้องปลอดเชื้อ เป็นบรรจุภัณฑ์อุตสาหกรรมคุณภาพสูงที่ออกแบบมาสำหรับอุตสาหกรรมอิเล็กทรอนิกส์ เซมิคอนดักเตอร์ PCB HDD และการผลิตที่ต้องการความแม่นยำสูง โดยต้องการวัสดุบรรจุภัณฑ์ที่สะอาดและมีการปนเปื้อนต่ำ',
        'ถุง LDPE และ HDPE ของเราผลิตภายใต้สภาวะการผลิตในห้องปลอดเชื้อ จึงให้ความสะอาดเป็นเลิศ มีการเกิดอนุภาคน้อย และให้การปกป้องที่เชื่อถือได้สำหรับชิ้นส่วนอิเล็กทรอนิกส์ที่ไวต่อไฟฟ้าสถิตในระหว่างการจัดเก็บและการขนส่ง',
        'ถุง LDPE และ HDPE สำหรับห้องคลีนรูมของเรามีจำหน่ายในเกรดที่ปราศจากซิลิโคนและอะไมด์ ทำให้เหมาะสำหรับบรรจุภัณฑ์เซมิคอนดักเตอร์ บรรจุภัณฑ์สำหรับห้องคลีนรูม และโซลูชั่นบรรจุภัณฑ์ป้องกันไฟฟ้าสถิต ซึ่งการควบคุมการปนเปื้อนมีความสำคัญอย่างยิ่ง',
    ],
    'desc_en': [
        'Cleanroom LDPE &amp; HDPE Bags are high-quality industrial packaging solutions designed for electronics, semiconductor, PCB, HDD, and precision manufacturing industries requiring clean, low-contamination packaging materials.',
        'Manufactured under cleanroom production conditions, our LDPE and HDPE bags provide excellent cleanliness, low particle generation, and reliable protection for sensitive electronic and static-sensitive components during storage and transportation.',
        'Our Cleanroom LDPE &amp; HDPE Bags are available in Non-Silicone and Non-Amide grades, making them suitable for Semiconductor Packaging, Cleanroom Packaging, and ESD Packaging Solutions where contamination control is critical.',
    ],
    'app_block': table_block(
        'การใช้งาน', 'Applications',
        'การใช้งาน', 'Application',
        'อุตสาหกรรม / ตัวอย่าง', 'Industry / Example',
        'หมายเหตุ', 'Note',
        [
            row('บรรจุภัณฑ์สารกึ่งตัวนำ', 'Semiconductor packaging', DASH, DASH),
            row('การป้องกันซิปไอซี', 'IC chip protection', DASH, DASH),
            row('การป้องกันความชื้นของ PCB', 'PCB moisture protection', DASH, DASH),
            row('บรรจุภัณฑ์ส่วนประกอบ HDD', 'HDD component packaging', DASH, DASH),
            row('ชิ้นส่วนอิเล็กทรอนิกส์ยานยนต์', 'Automotive electronics parts', DASH, DASH),
            row('ชิ้นส่วนอิเล็กทรอนิกส์ที่มีความแม่นยำ', 'Precision electronic components', DASH, DASH),
        ]
    ),
}

# ── VACUUM NYLON ─────────────────────────────────────────────────────────────
vacuum = {
    'slug': 'vacuum-nylon',
    'name': 'Vacuum Nylon Packaging Bags',
    'subtitle_th': 'ถุงไนลอนสำหรับบรรจุภัณฑ์สูญญากาศ',
    'cat_th': 'โซลูชันบรรจุภัณฑ์ ESD',
    'cat_en': 'ESD Packaging Solutions',
    'image': 'vacuum-nylon/vacuum-nylon-1.png',
    'desc_th': [
        'ถุงไนลอนสำหรับบรรจุภัณฑ์สูญญากาศ (Vacuum Nylon Packaging Bags) คือโซลูชันบรรจุภัณฑ์เกรดอุตสาหกรรมประสิทธิภาพสูง ที่ถูกออกแบบมาเพื่อให้ประสิทธิภาพการซีลสูญญากาศที่ยอดเยี่ยม ป้องกันความชื้น ทนทานต่อการเจาะทะลุ และปกป้องผลิตภัณฑ์ได้อย่างดีเยี่ยม เหมาะสำหรับงานอิเล็กทรอนิกส์และงานอุตสาหกรรมที่มีความละเอียดอ่อน',
        'ด้วยกระบวนการผลิตจากวัสดุไนลอนหลายชั้น (Multilayer Nylon) ที่มีความทนทาน ถุงประเภทนี้จึงมีคุณสมบัติในการป้องกันสิ่งเจือปนและสภาพแวดล้อมภายนอกได้อย่างดีเยี่ยม (Strong Barrier Performance) ได้รับความนิยมและนำไปใช้งานอย่างแพร่หลายในการบรรจุภัณฑ์สารกึ่งตัวนำ (Semiconductor Packaging), การบรรจุแผงวงจรพิมพ์ (PCB Packaging), ชิ้นส่วนอิเล็กทรอนิกส์, บรรจุภัณฑ์อาหาร ตลอดจนชิ้นส่วนอุตสาหกรรมที่มีความแม่นยำสูง',
        'ถุงสูญญากาศเนื้อไนลอนของเรา เหมาะสำหรับใช้งานในห้องคลีนรูม (Cleanroom) และสภาพแวดล้อมทางอุตสาหกรรม ที่เน้นความสำคัญในเรื่องความแข็งแรงของบรรจุภัณฑ์ที่เชื่อถือได้ อัตราการปนเปื้อนต่ำ และต้องการการปกป้องผลิตภัณฑ์ในระยะยาวอย่างมีประสิทธิภาพ',
    ],
    'desc_en': [
        'Vacuum Nylon Packaging Bags are high-performance industrial packaging solutions designed to provide excellent vacuum sealing, moisture resistance, puncture resistance, and product protection for sensitive electronic and industrial applications.',
        'Manufactured using durable multilayer nylon materials, these bags offer strong barrier performance and are widely used in Semiconductor Packaging, PCB Packaging, electronic components, food packaging, and precision industrial products requiring vacuum protection during storage and transportation.',
        'Our Vacuum Nylon Bags are suitable for cleanroom and industrial environments where reliable packaging strength, low contamination, and long-term product protection are essential.',
    ],
}

# ── HIC ──────────────────────────────────────────────────────────────────────
hic = {
    'slug': 'hic',
    'name': 'Humidity Indicator Cards (HIC)',
    'subtitle_th': 'การ์ดหรือแผ่นวัดระดับความชื้น',
    'cat_th': 'โซลูชันบรรจุภัณฑ์ ESD',
    'cat_en': 'ESD Packaging Solutions',
    'image': 'hic/hic-1.png',
    'desc_th': [
        'การ์ดวัดความชื้น (Humidity Indicator Cards หรือ HIC) คือแผ่นตรวจสอบความชื้นที่ใช้สำหรับตรวจวัดระดับความชื้นภายในถุงกันความชื้น (Moisture Barrier Bags หรือ MBB) และบรรจุภัณฑ์ที่ปิดผนึกอย่างแน่นหนา สำหรับชิ้นส่วนอิเล็กทรอนิกส์และสารกึ่งตัวนำ (Semiconductor) ที่มีความละเอียดอ่อน',
        'การ์ด HIC มีให้เลือกใช้งานทั้งแบบ 3 จุด (3 dots) และ 6 จุด (6 dots) รวมถึงเวอร์ชันปลอดสารโคบอลต์ (Cobalt-free) และไม่มีส่วนผสมของโคบอลต์ (Non-cobalt) โดยจะแสดงระดับความชื้นด้วยการเปลี่ยนสีที่เห็นได้อย่างชัดเจน เพื่อช่วยป้องกันความเสียหายที่เกิดจากความชื้นในระหว่างการจัดเก็บและการขนส่ง',
        'การ์ดวัดความชื้นนี้ได้รับความนิยมและนำไปใช้งานอย่างแพร่หลายในการบรรจุภัณฑ์สารกึ่งตัวนำ (Semiconductor Packaging), การบรรจุแผงวงจรพิมพ์ (PCB Packaging) และโซลูชันบรรจุภัณฑ์ป้องกันไฟฟ้าสถิต (ESD Packaging Solutions) ถือเป็นอุปกรณ์ชิ้นสำคัญที่ไม่สามารถละเลยได้ในการปกป้องชิ้นส่วนอิเล็กทรอนิกส์ที่ไวต่อความชื้นและไฟฟ้าสถิต',
    ],
    'desc_en': [
        'Humidity Indicator Cards (HIC) are moisture detection cards used to monitor humidity levels inside Moisture Barrier Bags (MBB) and sealed packaging for sensitive electronic and semiconductor components.',
        'Available in 3 dots and 6 dots types, including cobalt-free and non-cobalt versions, HIC cards provide clear visual humidity indication to help prevent moisture damage during storage and transportation.',
        'Widely used in Semiconductor Packaging, PCB Packaging, and ESD Packaging Solutions, Humidity Indicator Cards are essential for protecting moisture-sensitive and static-sensitive electronic components.',
    ],
    'types_block': table_block(
        'ประเภทสินค้าที่มีจำหน่าย', 'Available Types',
        'ประเภท', 'Type',
        'คำอธิบาย', 'Description',
        'หมายเหตุ', 'Note',
        [
            row('การ์ดวัดความชื้นแบบ 3 จุด', '3 Dots Humidity Indicator Cards', DASH, DASH),
            row('การ์ดวัดความชื้นแบบ 6 จุด', '6 Dots Humidity Indicator Cards', DASH, DASH),
            row('การ์ดวัดความชื้นแบบปลอดสารโคบอลต์', 'Cobalt-Free HIC Cards', DASH, DASH),
            row('การ์ดวัดความชื้นแบบไม่มีส่วนผสมของโคบอลต์', 'Non-Cobalt Humidity Indicator Cards', DASH, DASH),
            row('บริการปรับแต่งขนาด, รูปแบบดีไซน์ และระดับค่าความชื้นตามต้องการ', 'Customizable Size, Design, and Humidity Levels Available', DASH, DASH, 'Custom ✓', 'Custom ✓'),
        ]
    ),
}

# ── AIR BUBBLE ────────────────────────────────────────────────────────────────
airbubble = {
    'slug': 'air-bubble',
    'name': 'Anti-Static Air Bubble Packaging',
    'subtitle_th': 'พลาสติกกันกระแทกแบบป้องกันไฟฟ้าสถิต',
    'cat_th': 'โซลูชันบรรจุภัณฑ์ ESD',
    'cat_en': 'ESD Packaging Solutions',
    'image': 'air-bubble/air-bubble-1.png',
    'desc_th': [
        'คุณสมบัติป้องกันไฟฟ้าสถิต (Anti-Static): พลาสติกกันกระแทก (Air Bubble) ได้รับการออกแบบมาเพื่อเป็นวัสดุรองรับแรงกระแทกที่ช่วยปกป้องชิ้นส่วนอิเล็กทรอนิกส์และเซมิคอนดักเตอร์ที่บอบบาง ให้ปลอดภัยจากไฟฟ้าสถิต (ESD) แรงกระแทก การสั่นสะเทือน และความเสียหายที่อาจเกิดขึ้นระหว่างการขนส่ง',
        'กระบวนการผลิตที่มีคุณภาพ (Manufactured): ผลิตภัณฑ์พลาสติกกันกระแทกป้องกันไฟฟ้าสถิตของเรา ผลิตจากเม็ดพลาสติก PE ใหม่ (Virgin PE) คุณภาพสูง จึงให้ประสิทธิภาพในการรองรับแรงกระแทกที่เชื่อถือได้ พร้อมทั้งช่วยลดการเกิดไฟฟ้าสถิตในระหว่างการหยิบจับและการจัดส่งสินค้า',
        'ตัวเลือกหลากหลายและการใช้งาน (Applications): มีให้เลือกใช้งานทั้งแบบใสและแบบสีชมพู (ชนิดป้องกันไฟฟ้าสถิต) วัสดุบรรจุภัณฑ์เหล่านี้ได้รับการยอมรับและใช้งานอย่างแพร่หลายในอุตสาหกรรมการบรรจุภัณฑ์เซมิคอนดักเตอร์ การบรรจุภัณฑ์แผ่นวงจรพิมพ์ (PCB) โซลูชันบรรจุภัณฑ์ป้องกันไฟฟ้าสถิต (ESD) รวมถึงบรรจุภัณฑ์สำหรับใช้ในห้องคลีนรูม (Cleanroom) สำหรับผลิตภัณฑ์ที่ไวต่อไฟฟ้าสถิต',
        'รูปแบบและขนาด (Forms and Sizes): บรรจุภัณฑ์พลาสติกกันกระแทกป้องกันไฟฟ้าสถิตของเรา มีจำหน่ายทั้งในรูปแบบม้วนและรูปแบบถุง พร้อมบริการปรับแต่งขนาดตามความต้องการ (Customized sizes) เพื่อให้ตอบโจทย์ทุกข้อกำหนดในงานบรรจุภัณฑ์ภาคอุตสาหกรรมที่แตกต่างกัน',
    ],
    'desc_en': [
        'Anti-Static Air Bubble Packaging is protective cushioning packaging designed to protect sensitive electronic and semiconductor components from electrostatic discharge (ESD), shock, vibration, and transportation damage.',
        'Manufactured using high-quality virgin PE materials, our Anti-Static Air Bubble products provide reliable cushioning performance while helping reduce static electricity during handling and shipping.',
        'Available in clear and pink anti-static types, these packaging materials are widely used in Semiconductor Packaging, PCB Packaging, ESD Packaging Solutions, and Cleanroom Packaging applications for static-sensitive products.',
        'Our Anti-Static Air Bubble Packaging is available in both roll and bag forms with customized sizes to meet different industrial packaging requirements.',
    ],
    'types_block': table_block(
        'ประเภทสินค้าที่มีจำหน่าย', 'Available Types',
        'ประเภท', 'Type',
        'คำอธิบาย', 'Description',
        'หมายเหตุ', 'Note',
        [
            row('พลาสติกกันกระแทกป้องกันไฟฟ้าสถิต ชนิดสีใส', 'Clear Anti-Static Air Bubble', DASH, DASH),
            row('พลาสติกกันกระแทกป้องกันไฟฟ้าสถิต ชนิดสีชมพู', 'Pink Anti-Static Air Bubble', DASH, DASH),
            row('พลาสติกกันกระแทก ผลิตจากเม็ดพลาสติกใหม่ 100% (เกรด Virgin PE)', 'Virgin PE Grade Air Bubble', DASH, DASH),
            row('พลาสติกกันกระแทกแบบม้วน', 'Air Bubble Roll', DASH, DASH),
            row('ถุงพลาสติกกันกระแทก / ซองบับเบิ้ล', 'Air Bubble Bags', DASH, DASH),
            row('มีบริการสั่งผลิตตามขนาดที่ต้องการ', 'Customized Sizes Available', DASH, DASH, 'Custom ✓', 'Custom ✓'),
        ]
    ),
    'feat_block': table_block(
        'คุณสมบัติเด่น', 'Key Features',
        'คุณสมบัติ', 'Feature',
        'รายละเอียด', 'Details',
        'หมายเหตุ', 'Note',
        [
            row('ป้องกันการสะสมของไฟฟ้าสถิต', 'Anti-static protection', 'ช่วยปกป้องชิ้นส่วนอิเล็กทรอนิกส์', 'Protects electronic components from ESD'),
            row('ประสิทธิภาพการกันกระแทกดีเยี่ยม', 'Excellent cushioning performance', DASH, DASH),
            row('น้ำหนักเบา แต่มีความทนทานสูง', 'Lightweight and durable', 'ไม่ฉีกขาดง่าย', 'Resistant to tearing'),
            row('ซับแรงกระแทกและลดแรงสั่นสะเทือนได้ดี', 'Good shock absorption', DASH, DASH),
            row('สะอาด ปลอดภัย ผลิตจากเม็ดพลาสติกใหม่เกรดพรีเมียม', 'Clean and high-quality virgin PE material', 'Virgin PE 100%', 'Virgin PE 100%'),
            row('สามารถสั่งผลิตตามขนาดและรูปแบบที่ต้องการได้', 'Custom sizes and formats available', 'แบบม้วน แบบแผ่น หรือแบบถุง', 'Roll, sheet, or bag forms'),
        ]
    ),
}

# ── CUSHION WRAP ──────────────────────────────────────────────────────────────
cushion = {
    'slug': 'cushion-wrap',
    'name': 'Protective Cushioning Wrap',
    'subtitle_th': 'วัสดุห่อหุ้มเพื่อการปกป้องและกันกระแทก',
    'cat_th': 'โซลูชันบรรจุภัณฑ์ ESD',
    'cat_en': 'ESD Packaging Solutions',
    'image': 'cushion-wrap/cushion-wrap-1.png',
    'desc_th': [
        'ผลิตภัณฑ์นี้คือฟิล์มพลาสติกกันกระแทกป้องกันไฟฟ้าสถิต ผลิตจากวัสดุโพลีเอสเตอร์ (PET) และเมทัลโลซีน พีอี (Metallocene PE) คุณภาพสูง ถูกออกแบบมาเพื่อประสิทธิภาพในการกันกระแทก และเป็นบรรจุภัณฑ์ที่ปลอดภัยจากไฟฟ้าสถิต (ESD-safe) เหมาะสำหรับอุปกรณ์อิเล็กทรอนิกส์ที่มีความละเอียดอ่อนและสินค้าอุตสาหกรรม',
    ],
    'desc_en': [
        'This product is an Anti-Static Air Bubble Film made from high-quality Polyester (PET) and Metallocene PE materials. It is designed for cushioning protection and ESD-safe packaging for sensitive electronic and industrial products.',
    ],
}

# ── SULFUR-FREE PAPER ─────────────────────────────────────────────────────────
sulfur = {
    'slug': 'sulfur-free-paper',
    'name': 'Sulfur-Free Paper for Electronic Components',
    'subtitle_th': 'กระดาษปราศจากซัลเฟอร์สำหรับชิ้นส่วนอิเล็กทรอนิกส์',
    'cat_th': 'โซลูชันบรรจุภัณฑ์ ESD',
    'cat_en': 'ESD Packaging Solutions',
    'image': 'sulfur-free-paper/sulfur-free-paper-1.png',
    'desc_th': [
        'กระดาษไร้สารซัลเฟอร์สำหรับส่วนประกอบอิเล็กทรอนิกส์ คือกระดาษบรรจุภัณฑ์ปกป้องผิวชนิดพิเศษ ที่ถูกออกแบบมาสำหรับชิ้นส่วนอิเล็กทรอนิกส์และเซมิคอนดักเตอร์ที่มีความละเอียดอ่อน ซึ่งจำเป็นต้องใช้บรรจุภัณฑ์ที่ปลอดสิ่งปนเปื้อนในระหว่างการจัดเก็บและการขนส่ง กระดาษปราศจากกำมะถันนี้ผ่านกระบวนการผลิตที่ไม่มีสารปนเปื้อนของกำมะถัน จึงช่วยป้องกันการกัดกร่อน การเกิดออกซิเดชัน (สนิม) และปฏิกิริยาทางเคมีที่อาจสร้างความเสียหายต่อพื้นผิวโลหะที่ไวต่อสิ่งกระตุ้น เช่น เงิน, ทองแดง, นิกเกิล และโลหะอื่นๆ ที่ใช้ในชิ้นส่วนอิเล็กทรอนิกส์',
        'ถูกออกแบบมาเพื่อป้องกันรอยขีดข่วน ป้องกันการเกิดออกซิเดชัน (คราบสนิม) และปกป้องแบบแยกชั้น (Isolation Protection) สำหรับแผ่นฐานวงจรพิมพ์ขาเข้า (CCL Substrates), แผ่นฐานรองไอซี (IC Carrier Substrates) รวมถึงงานบรรจุภัณฑ์ไอซี (IC Packaging) เหมาะสำหรับการปกป้องแผ่นวงจรพิมพ์ทั้งแบบอ่อนและแบบแข็ง รวมถึงบรรจุภัณฑ์แยกชั้นสำหรับ PCB และ FPC ช่วยลดความเสียหายบนพื้นผิว ลดการปนเปื้อน และลดการสัมผัสของเนื้อวัสดุในระหว่างการจัดเก็บและการขนส่ง',
    ],
    'desc_en': [
        'Sulfur-Free Paper is specialized protective packaging paper designed for sensitive electronic and semiconductor components that require contamination-free packaging during storage and transportation. Sulfur-Free Paper is manufactured without sulfur contaminants, helping prevent corrosion, oxidation, and chemical reactions that may damage silver, copper, nickel, and other sensitive metal surfaces used in electronic components.',
        'Designed for anti-scratch, oxidation prevention, and isolation protection for CCL substrates, IC carrier substrates, and IC packaging applications. Suitable for soft and hard circuit board protection, including PCB and FPC isolation packaging, helping reduce surface damage, contamination, and material contact during storage and transportation.',
    ],
    'types_block': table_block(
        'รายชื่อผลิตภัณฑ์', 'Product List',
        'ประเภท', 'Type',
        'คำอธิบาย', 'Description',
        'หมายเหตุ', 'Note',
        [
            row('กระดาษคลีนรูม / กระดาษปลอดฝุ่น', 'Purification Paper', 'สำหรับห้องควบคุมความสะอาด', 'For cleanroom environments'),
            row('กระดาษปราศจากกำมะถัน (กระดาษไร้ซัลเฟอร์)', 'Sulfur-Free Paper', DASH, DASH),
            row('ฟิล์มคอมโพสิตพีพี', 'PP Composite Film', 'ฟิล์มพลาสติก PP ชนิดผสมซ้อนชั้น', 'Multilayer PP plastic film'),
            row('กระดาษรองอบ', 'Baking Paper', 'ใช้รองชิ้นส่วนในกระบวนการอบความร้อน', 'Used for heat process applications'),
            row('กระดาษการ์ดขาว / กระดาษกล่องขาว', 'White Board Paper', 'สำหรับใช้รองหรือกั้นชิ้นงาน', 'For component separation and support'),
        ]
    ),
}

# ── COTTON SWABS ──────────────────────────────────────────────────────────────
cotton = {
    'slug': 'cotton-swabs',
    'name': 'Cleanroom Cotton Swabs',
    'subtitle_th': 'ก้านสำลี (คอตตอนบัด) สำหรับใช้ในห้องคลีนรูม',
    'cat_th': 'สินค้าสิ้นเปลืองสำหรับห้องคลีนรูม',
    'cat_en': 'Cleanroom &amp; ESD Consumables',
    'image': 'cotton-swab/cotton-swab-1.png',
    'desc_th': [
        'คอตตอนบัดสำหรับห้องคลีนรูม (Cleanroom Cotton Swabs) คือก้านเช็ดทำความสะอาดชนิดพิเศษที่ถูกออกแบบมาสำหรับสภาพแวดล้อมที่ไวต่อสิ่งปนเปื้อน เช่น อุตสาหกรรมเซมิคอนดักเตอร์, อิเล็กทรอนิกส์, แผ่นวงจรพิมพ์ (PCB), อุปกรณ์ออปติก (เลนส์และกระจก) รวมถึงอุตสาหกรรมการผลิตชิ้นส่วนความแม่นยำสูง',
        'ผลิตขึ้นโดยใช้วัสดุที่ก่อให้เกิดอนุภาคฝุ่นต่ำ (Low-particle) และรองรับการใช้งานในห้องคลีนรูม ก้านเช็ดเหล่านี้จึงเหมาะสำหรับการทำความสะอาดที่ต้องการความแม่นยำสูง การขจัดฝุ่น และการควบคุมสิ่งปนเปื้อนบนพื้นผิวที่บอบบาง รวมถึงชิ้นส่วนอิเล็กทรอนิกส์ต่างๆ',
        'คอตตอนบัดสำหรับห้องคลีนรูม เหมาะสำหรับงานทำความสะอาดทั่วไปในห้องคลีนรูม งานขจัดฝุ่นละออง และงานเช็ดทำความสะอาดชิ้นส่วนอิเล็กทรอนิกส์ทั่วไป',
    ],
    'desc_en': [
        'Cleanroom Cotton Swabs are specialized cleaning swabs designed for contamination-sensitive environments such as semiconductor, electronics, PCB, optical, and precision manufacturing industries.',
        'Manufactured using low-particle and cleanroom-compatible materials, these swabs are used for precision cleaning, dust removal, and contamination control on delicate surfaces and electronic components.',
        'Cleanroom Cotton Swabs are suitable for general cleanroom cleaning, dust removal, and electronic component cleaning applications.',
    ],
}

# ── FOAM SWABS ────────────────────────────────────────────────────────────────
foam = {
    'slug': 'foam-swabs',
    'name': 'Cleanroom Foam Swabs',
    'subtitle_th': 'ก้านโฟมเช็ดทำความสะอาดสำหรับใช้ในห้องคลีนรูม',
    'cat_th': 'สินค้าสิ้นเปลืองสำหรับห้องคลีนรูม',
    'cat_en': 'Cleanroom &amp; ESD Consumables',
    'image': 'foam-swab/foam-swab-1.png',
    'desc_th': [
        'ก้านโฟมเช็ดทำความสะอาดสำหรับห้องคลีนรูม (Cleanroom Foam Swabs) แนะนำสำหรับงานทำความสะอาดที่ต้องการความแม่นยำสูงมาก ซึ่งจำเป็นต้องควบคุมการเกิดอนุภาคฝุ่นให้อยู่ในระดับต่ำและต้องการประสิทธิภาพแบบไร้ขุย 100% โดยเฉพาะในอุตสาหกรรมเซมิคอนดักเตอร์, อุปกรณ์ออปติก (เลนส์และกระจก) รวมถึงสภาพแวดล้อมที่ไวต่อไฟฟ้าสถิต (ESD)',
        'เปรียบเทียบความแตกต่างระหว่าง คอตตอนบัดเกรดคลีนรูม กับ ก้านโฟมเช็ดทำความสะอาด: คอตตอนบัดเหมาะสำหรับงานทำความสะอาดทั่วไป ในขณะที่ก้านโฟมเหมาะสำหรับงานที่ต้องการความแม่นยำสูงและควบคุมอนุภาคได้ดีกว่า',
    ],
    'desc_en': [
        'Cleanroom Foam Swabs are recommended for high-precision cleaning applications requiring low particle generation and lint-free performance, especially in semiconductor, optical, and ESD-sensitive environments.',
        'Cleanroom Cotton Swabs are suitable for general cleanroom cleaning, dust removal, and electronic component cleaning applications — while Foam Swabs are preferred where even stricter particle control is required.',
    ],
}

# ── WIPERS ────────────────────────────────────────────────────────────────────
wipers = {
    'slug': 'wipers',
    'name': 'Anti-Static Cleanroom Wipers',
    'subtitle_th': 'ผ้าเช็ดทำความสะอาดในห้องคลีนรูมแบบป้องกันไฟฟ้าสถิต',
    'cat_th': 'สินค้าสิ้นเปลืองสำหรับห้องคลีนรูม',
    'cat_en': 'Cleanroom &amp; ESD Consumables',
    'image': 'wipers/wipers-1.png',
    'desc_th': [
        'ผ้าเช็ดทำความสะอาดป้องกันไฟฟ้าสถิตสำหรับห้องคลีนรูม (Anti-Static Cleanroom Wipers) คือผ้าเช็ดทำความสะอาดชนิดพิเศษที่ถูกออกแบบมาเพื่อควบคุมสิ่งปนเปื้อนและใช้งานในสภาพแวดล้อมที่ไวต่อไฟฟ้าสถิต เช่น อุตสาหกรรมเซมิคอนดักเตอร์, อิเล็กทรอนิกส์, แผ่นวงจรพิมพ์ (PCB), ฮาร์ดดิสก์ไดรฟ์ (HDD) รวมถึงอุตสาหกรรมการผลิตชิ้นส่วนความแม่นยำสูง',
        'ผลิตขึ้นจากวัสดุที่ก่อให้เกิดอนุภาคฝุ่นต่ำและไร้ขุย (Lint-free) ผ้าเช็ดเกรดคลีนรูมนี้จึงช่วยขจัดฝุ่นละออง อนุภาคขนาดเล็ก คราบน้ำมัน และสิ่งปนเปื้อนต่างๆ ได้เป็นอย่างดี พร้อมทั้งช่วยลดการเกิดไฟฟ้าสถิต (ESD) ในระหว่างกระบวนการเช็ดทำความสะอาด',
        'ผ้าเช็ดทำความสะอาดป้องกันไฟฟ้าสถิตชนิดนี้ นิยมใช้งานกันอย่างแพร่หลายในกระบวนการบรรจุภัณฑ์สำหรับห้องคลีนรูม บรรจุภัณฑ์เซมิคอนดักเตอร์ การประกอบแผ่นวงจรพิมพ์ (PCB Assembly) และพื้นที่การผลิตที่ต้องควบคุมไฟฟ้าสถิต',
    ],
    'desc_en': [
        'Anti-Static Cleanroom Wipers are specialized cleaning wipes designed for contamination control and static-sensitive environments such as semiconductor, electronics, PCB, HDD, and precision manufacturing industries.',
        'Manufactured using low-particle and lint-free materials, these cleanroom wipers help remove dust, particles, oil, and contaminants while reducing electrostatic discharge (ESD) during cleaning processes.',
        'Widely used in Cleanroom Packaging, Semiconductor Packaging, PCB assembly, and ESD-safe production areas, Anti-Static Cleanroom Wipers provide reliable cleaning performance for sensitive electronic components and cleanroom equipment.',
    ],
    'feat_block': table_block(
        'คุณสมบัติเด่น', 'Key Features',
        'คุณสมบัติ', 'Feature',
        'รายละเอียด', 'Details',
        'หมายเหตุ', 'Note',
        [
            row('Anti-static (ESD-safe) performance', 'Anti-static (ESD-safe) performance', 'มีประสิทธิภาพในการป้องกันไฟฟ้าสถิต (ปลอดภัยต่ออุปกรณ์ ESD)', 'Effective ESD-safe performance'),
            row('Low particle generation', 'Low particle generation', 'ก่อให้เกิดอนุภาคฝุ่นต่ำมาก', 'Minimal particle generation'),
            row('Lint-free material', 'Lint-free material', 'ผลิตจากวัสดุไร้ขุย 100% ไม่ทิ้งเศษขนหรือเส้นใยหลุดร่วง', '100% lint-free, no fiber shedding'),
            row('Excellent absorbency', 'Excellent absorbency', 'มีประสิทธิภาพในการดูดซับน้ำและสารละลายได้อย่างดีเยี่ยม', 'Excellent absorption of liquids and solvents'),
            row('Soft and non-abrasive texture', 'Soft and non-abrasive texture', 'เนื้อสัมผัสนุ่มนวล ไม่ทำให้ผิวชิ้นงานเป็นรอยขีดข่วน', 'Soft texture, no surface scratching'),
            row('Cleanroom compatible', 'Cleanroom compatible', 'รองรับการใช้งานในห้องควบคุมความสะอาด (ห้องคลีนรูม) ได้อย่างสมบูรณ์แบบ', 'Fully compatible with cleanroom environments'),
        ]
    ),
}

# ── GARMENTS ──────────────────────────────────────────────────────────────────
garments = {
    'slug': 'garments',
    'name': 'Cleanroom Garments &amp; Suits',
    'subtitle_th': 'เสื้อผ้าและชุดปฏิบัติการสำหรับห้องคลีนรูม',
    'cat_th': 'สินค้าสิ้นเปลืองสำหรับห้องคลีนรูม',
    'cat_en': 'Cleanroom &amp; ESD Consumables',
    'image': 'garments/garments-1.png',
    'desc_th': [
        'ชุดและเครื่องแต่งกายสำหรับห้องคลีนรูม (Cleanroom Garments &amp; Suits) คือเครื่องแต่งกายป้องกันชนิดพิเศษที่ถูกออกแบบมาเพื่อลดการปนเปื้อนของอนุภาคฝุ่นและการเกิดไฟฟ้าสถิต (ESD) ในห้องคลีนรูมและสภาพแวดล้อมการผลิตที่ไวต่อไฟฟ้าสถิต',
        'ผลิตภัณฑ์นี้ได้รับการใช้งานอย่างแพร่หลายในอุตสาหกรรมเซมิคอนดักเตอร์, อิเล็กทรอนิกส์, แผ่นวงจรพิมพ์ (PCB), ยาและเวชภัณฑ์, อุปกรณ์ออปติก (เลนส์และกระจก) รวมถึงอุตสาหกรรมการผลิตชิ้นส่วนความแม่นยำสูง ชุดคลีนรูมจะช่วยรักษามาตรฐานความสะอาด พร้อมทั้งปกป้องผลิตภัณฑ์ที่บอบบางและกระบวนการผลิตให้ปลอดภัยจากฝุ่นละออง เส้นใยผ้าและสิ่งปนเปื้อนที่มาจากตัวบุคคล',
        'ชุดคลีนรูมของเราผลิตจากวัสดุที่เกิดขุยต่ำ (Low-lint) และปลอดภัยจากไฟฟ้าสถิต (ESD-safe) จึงสวมใส่สบาย มีความทนทาน และมอบประสิทธิภาพการควบคุมสิ่งปนเปื้อนที่เชื่อถือได้สำหรับการปฏิบัติงานในห้องคลีนรูม',
    ],
    'desc_en': [
        'Cleanroom Garments &amp; Suits are specialized protective apparel designed to minimize particle contamination and electrostatic discharge (ESD) in cleanroom and static-sensitive manufacturing environments.',
        'Widely used in semiconductor, electronics, PCB, pharmaceutical, optical, and precision manufacturing industries, cleanroom garments help maintain cleanliness standards while protecting sensitive products and production processes from dust, fibers, and human contamination.',
        'Manufactured using low-lint and ESD-safe materials, our cleanroom garments provide comfort, durability, and reliable contamination control for cleanroom operations.',
    ],
    'types_block': table_block(
        'ประเภทสินค้าที่มีจำหน่าย', 'Available Types',
        'ประเภท', 'Type',
        'คำอธิบาย (ไทย)', 'Description',
        'หมายเหตุ', 'Note',
        [
            row('Cleanroom Coveralls', 'Cleanroom Coveralls', 'ชุดหมีคลีนรูม (ชุดชิ้นเดียวคลุมทั้งตัวเสื้อและกางเกง)', 'One-piece full-body cleanroom suit'),
            row('Cleanroom Suits', 'Cleanroom Suits', 'ชุดคลีนรูม / ชุดปฏิบัติงานในห้องปลอดฝุ่น', 'Cleanroom work suits'),
            row('Cleanroom Jackets &amp; Pants', 'Cleanroom Jackets &amp; Pants', 'เสื้อแจ็กเก็ตและกางเกงแยกชิ้นสำหรับห้องคลีนรูม', 'Separate jacket and pants'),
            row('ESD Garments', 'ESD Garments', 'ชุดป้องกันไฟฟ้าสถิต (ESD)', 'ESD-safe protective garments'),
            row('Hood &amp; Cap', 'Hood &amp; Cap', 'ฮูดและหมวกคลุมศีรษะเกรดคลีนรูม', 'Cleanroom-grade hood and cap'),
            row('Cleanroom Lab Coats', 'Cleanroom Lab Coats', 'เสื้อกราวน์ / เสื้อคลุมยาวสำหรับห้องคลีนรูม', 'Laboratory gown for cleanroom use'),
            row('Anti-Static Uniforms', 'Anti-Static Uniforms', 'ชุดยูนิฟอร์มป้องกันไฟฟ้าสถิต', 'Anti-static uniform'),
            row('Cleanroom Sleeves &amp; Accessories', 'Cleanroom Sleeves &amp; Accessories', 'ปลอกแขนคลีนรูมและอุปกรณ์เสริมต่างๆ', 'Sleeves and supplementary accessories'),
        ]
    ),
}

# ── GLOVES ────────────────────────────────────────────────────────────────────
gloves = {
    'slug': 'gloves',
    'name': 'Anti-Static &amp; Latex Gloves',
    'subtitle_th': 'ถุงมือป้องกันไฟฟ้าสถิต และถุงมือยางลาเท็กซ์',
    'cat_th': 'สินค้าสิ้นเปลืองสำหรับห้องคลีนรูม',
    'cat_en': 'Cleanroom &amp; ESD Consumables',
    'image': 'esd-gloves/esd-gloves-1.png',
    'desc_th': [
        'ถุงมือป้องกันไฟฟ้าสถิต (Anti-Static Gloves) และถุงมือยางลาเท็กซ์ (Latex Gloves) สำหรับใช้งานในห้องคลีนรูมและสภาพแวดล้อมที่ไวต่อไฟฟ้าสถิต ปกป้องมือผู้ปฏิบัติงานพร้อมควบคุมการปนเปื้อนในกระบวนการผลิตที่ต้องการความสะอาดสูง',
    ],
    'desc_en': [
        'Anti-Static ESD Gloves and Cleanroom Latex Gloves for cleanroom and static-sensitive manufacturing environments. Provides hand protection while maintaining contamination control in high-precision semiconductor, PCB, and electronics production processes.',
    ],
}

# ─────────────────────────────────────────────────────────────────────────────
# GENERATE ALL PAGES
# ─────────────────────────────────────────────────────────────────────────────

all_products = [mbb, ssb, ldpe, vacuum, hic, airbubble, cushion, sulfur,
                cotton, foam, wipers, garments, gloves]

for p in all_products:
    filename = os.path.join(BASE, f"{p['slug']}.html")
    content = build_page(p)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✓ {filename}")

print(f"\nDone — {len(all_products)} pages generated.")
