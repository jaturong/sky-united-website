# 📚 Git Learning Notes — Sky United Website Project

**วัตถุประสงค์:** บันทึกการเรียน Git อย่างละเอียดพร้อมตัวอย่างจริง  
**โปรเจกต์:** sky-united-website  
**วันที่เริ่ม:** 2026-06-13  
**ผู้เรียน:** Jaturong Tonsunan

---

## 📌 Part 1: Git Fundamentals

### 1.1 Git คืออะไร?

**Git** = ระบบควบคุมเวอร์ชัน (Version Control System)
- ติดตามการเปลี่ยนแปลงของ code
- ทำให้สามารถกลับไปรุ่นเก่าได้
- ทำให้ทีมสามารถทำงานร่วมกันได้

---

## 📌 Part 2: Tags — บันทึกจุด Milestone

### 2.1 Tag คืออะไร?

**Tag** = ป้ายชื่อคงตัวสำหรับ commit สำคัญ

**เปรียบเทียบ:**
```
commit = บันทึกเหตุการณ์ (เช่น "2026-06-13 10:30 น. แก้ไข website URL")
tag    = ป้ายชื่อ (เช่น "v1.0 production" สำหรับ milestone)
```

### 2.2 ทำไมต้องใช้ Tag?

✅ **ตั้งชื่อ version ได้** — ชัดเจนว่า v1.0, v1.1 เป็นอะไร  
✅ **Download release ได้** — GitHub Releases  
✅ **Rollback ได้** — ถ้าต้องกลับไปรุ่นเก่า  
✅ **จัดการ release ได้** — ทีม/ลูกค้าเข้าใจได้ง่าย

### 2.3 Local vs Remote Tag

```
Local Tag  = Tag ที่อยู่เครื่องของคุณเท่านั้น
Remote Tag = Tag ที่อยู่บน GitHub (ทุกคนเห็นได้)
```

**ข้อสำคัญ:** ถ้าแก้ไข tag ต้องแก้ทั้ง local และ remote

---

## 📌 Part 3: Case Study — เปลี่ยน Tag v1.0 → 1.0

### Project Context
- **Repository:** github.com/jaturong/sky-united-website
- **Task:** เตรียม production (v1.0 → 1.0) สำหรับการปรับปรุง SEO
- **Reason:** ต้องการ versioning style ที่สอดคล้องกัน

---

### Step 1: ตรวจสอบ Tag ปัจจุบัน

**คำสั่ง:**
```bash
git tag
```

**ผลลัพธ์:**
```
v1.0
v1.0-pre-responsive
```

**ความหมาย:**
- `v1.0` = production baseline ปัจจุบัน
- `v1.0-pre-responsive` = backup เก่า (ก่อน responsive fixes)

**สิ่งที่ได้เรียน:**
- `git tag` = คำสั่งดูทั้งหมดที่มี
- Tag ปรากฏทั้ง local และ remote (ซิงค์กัน)

---

### Step 2: ลบ Tag Local (v1.0)

**คำสั่ง:**
```bash
git tag -d v1.0
```

**ผลลัพธ์:**
```
Deleted tag 'v1.0' (was e2288dd)
```

**ความหมาย:**
- `-d` = delete
- `v1.0` = tag ที่ต้องการลบ
- `(was e2288dd)` = tag นี้ชี้ไปที่ commit e2288dd

**⚠️ สำคัญ:**
- ลบเฉพาะ local เท่านั้น
- GitHub ยังคงมี v1.0 อยู่
- ต้องลบ remote ต่อไป

**สิ่งที่ได้เรียน:**
- Local tag ต้องลบด้วย `git tag -d`
- ลบ local ไม่ได้ลบ remote โดยอัตโนมัติ

---

### Step 3: ลบ Tag Remote (GitHub)

**คำสั่ง:**
```bash
git push origin --delete v1.0
```

**พูดแบบชาวบ้าน:**
> "ดันข้อมูลไปที่ origin (GitHub) เพื่อลบ tag v1.0"

**ผลลัพธ์:**
```
To https://github.com/jaturong/sky-united-website.git
 - [deleted]         v1.0
```

**ความหมาย:**
- `git push` = ส่งข้อมูลไปที่ GitHub
- `origin` = ชื่อของ remote (ค่าเริ่มต้นของ GitHub)
- `--delete v1.0` = ลบ tag v1.0
- `- [deleted]` = ลบเสร็จแล้ว

**⚠️ สำคัญ:**
- คำสั่งนี้ลบจาก GitHub เท่านั้น
- Local v1.0 ถูกลบแล้ว (Step 2)
- ต้องสร้าง tag ใหม่ต่อไป

**สิ่งที่ได้เรียน:**
- Remote tag ลบด้วย `git push origin --delete <tag>`
- `origin` = ชื่อ remote (สำคัญ!)

---

### Step 4: สร้าง Tag ใหม่ (1.0)

**คำสั่ง:**
```bash
git tag 1.0
```

**พูดแบบชาวบ้าน:**
> "สร้าง tag ชื่อ 1.0 ที่ commit ปัจจุบัน (HEAD)"

**ผลลัพธ์:**
```
(ไม่มี output = ปกติ)
```

**ความหมาย:**
- ไม่มี output = ทำงานสำเร็จ
- Tag 1.0 ถูกสร้างที่ HEAD (commit ล่าสุด)
- ยังอยู่ local เท่านั้น (ยังไม่ไปที่ GitHub)

**⚠️ สำคัญ:**
- `git tag <name>` = สร้าง tag
- Tag ชี้ไปที่ commit ปัจจุบัน (HEAD)
- ต้อง push ไปที่ GitHub ต่อไป

**สิ่งที่ได้เรียน:**
- `git tag <name>` = สร้าง lightweight tag
- Tag ที่สร้างใหม่อยู่ local แต่ยังไม่ไป remote

---

### Step 5: Push Tag ไปที่ GitHub

**คำสั่ง:**
```bash
git push origin 1.0
```

**พูดแบบชาวบ้าน:**
> "ดันข้อมูล tag 1.0 ไปที่ GitHub"

**ผลลัพธ์:**
```
To https://github.com/jaturong/sky-united-website.git
 * [new tag]         1.0 -> 1.0
```

**ความหมาย:**
- `git push origin 1.0` = ส่ง tag 1.0 ไปที่ GitHub
- `[new tag]` = สร้าง tag ใหม่บน GitHub
- `1.0 -> 1.0` = local 1.0 → remote 1.0

**✅ สำเร็จ!**
- Tag 1.0 ตอนนี้มีทั้ง local และ remote
- GitHub ทั้งโลกเห็นได้แล้ว

**สิ่งที่ได้เรียน:**
- `git push origin <tag>` = push tag ไปที่ GitHub
- Tag ต้องเข้าซิงค์กับ GitHub เพื่อให้ทีมเห็น

---

### Step 6: ตรวจสอบผลลัพธ์

**คำสั่ง:**
```bash
git tag
```

**ผลลัพธ์:**
```
1.0
v1.0-pre-responsive
```

**ความหมาย:**
- ✅ v1.0 ลบหมดแล้ว
- ✅ 1.0 สร้างขึ้นแล้ว
- ✅ v1.0-pre-responsive ยังเหลือ (backup)

---

## 📌 Part 4: Key Learnings (สิ่งที่ต้องจำ)

### ✅ Tag Management

| Task | คำสั่ง | หมายเหตุ |
|------|--------|---------|
| ดูทั้งหมด | `git tag` | ดูทั้ง local & remote |
| ดูรายละเอียด | `git show <tag>` | ดูข้อมูล tag |
| สร้าง local | `git tag <name>` | สร้างที่ commit ปัจจุบัน |
| สร้าง annotated | `git tag -a <name> -m "msg"` | มีข้อความอธิบาย |
| ลบ local | `git tag -d <tag>` | ลบจาก local เท่านั้น |
| ลบ remote | `git push origin --delete <tag>` | ลบจาก GitHub |
| Push tag | `git push origin <tag>` | ส่ง tag ไปที่ GitHub |
| Push ทุก tag | `git push origin --tags` | ส่งทั้งหมด |

### 🎓 Git Concepts ที่สำคัญ

1. **Local vs Remote**
   - Local = คอมพิวเตอร์ของคุณ
   - Remote = GitHub (บนเซิร์ฟเวอร์)
   - ต้องซิงค์ด้วย `git push` / `git pull`

2. **Tag vs Branch**
   - **Tag** = ป้ายชื่อที่ชี้ไปที่ commit เดียว (ไม่เปลี่ยน)
   - **Branch** = เส้นทางงานที่เคลื่อนไหวได้ (เปลี่ยนตามเพิ่ม commit)

3. **HEAD**
   - HEAD = commit ปัจจุบันที่คุณทำงานอยู่
   - Tag สร้างที่ HEAD = ชี้ไปที่ commit ล่าสุด

### 💡 Best Practices

✅ **ใช้ tag สำหรับ release/milestone**
```
1.0, 1.1, 2.0  = production version
```

✅ **ใช้ branch สำหรับงาน/feature**
```
feature/seo-improvements
bugfix/header-issue
```

✅ **ลบ tag ต้องลบทั้ง local + remote**
```
git tag -d v1.0                    # local
git push origin --delete v1.0      # remote
```

✅ **Push tag ต้องระบุ tag ที่ต้องการ**
```
git push origin 1.0    # เฉพาะ tag 1.0
git push origin --tags # ทั้งหมด
```

---

## 📌 Checklist — ขั้นตอนที่เสร็จแล้ว

- ✅ ตรวจสอบ tag ปัจจุบัน
- ✅ ลบ tag local v1.0
- ✅ ลบ tag remote v1.0
- ✅ สร้าง tag local 1.0
- ✅ push tag 1.0 ไปที่ GitHub
- ✅ ตรวจสอบผลลัพธ์

---

## 📌 ขั้นตอนถัดไป

**Step 2: Feature Branch for SEO Improvements**
- ตรวจสอบ branch ปัจจุบัน
- สร้าง branch `feature/seo-improvements`
- เข้าไปใน branch นั้น

---

## 📌 Part 5: Feature Branch — สาขาสำหรับงาน

### 5.1 Branch คืออะไร?

**Branch** = สาขาของ git ที่คุณทำงานแยกจาก main

**เปรียบเทียบ:**
```
main           = ถนนหลัก (production — ต้องปลอดภัย)
feature/seo    = ถนนข้าง (คุณสามารถสร้างสรรค์ได้)
```

**ทำไมต้องใช้ branch?**

✅ ไม่กระทบ main (production ปลอดภัย)  
✅ สามารถทำหลายอย่างพร้อมกันได้  
✅ สามารถยกเลิกได้ถ้าต้อง  
✅ ทำให้ git history ชัดเจน

### 5.2 Branch vs Tag

```
Branch = เส้นทางงาน (เคลื่อนไหวได้ เพิ่ม commit ได้)
Tag    = ป้ายชื่อ (ชี้ไปที่ commit เดียว ไม่เปลี่ยน)
```

---

### Step 1: ตรวจสอบ Branch ปัจจุบัน

**คำสั่ง:**
```bash
git branch
```

**ผลลัพธ์:**
```
* main
```

**ความหมาย:**
- `* main` = อยู่ที่ main branch
- `*` = เครื่องหมายแสดง branch ปัจจุบัน

**สิ่งที่ได้เรียน:**
- `git branch` = ดูทั้งหมด + แสดง current branch

---

### Step 2: สร้าง Feature Branch ใหม่

**คำสั่ง:**
```bash
git checkout -b feature/seo-improvements
```

**พูดแบบชาวบ้าน:**
> "สร้าง branch ใหม่ชื่อ feature/seo-improvements และเข้าไปใน branch นั้น"

**ความหมาย:**
- `git checkout` = เปลี่ยนไป branch อื่น
- `-b` = สร้าง branch ใหม่ (b = branch)
- `feature/seo-improvements` = ชื่อ branch

**ผลลัพธ์:**
```
Switched to a new branch 'feature/seo-improvements'
```

**⚠️ สำคัญ:**
- ตั้งชื่อ branch ด้วยคำนำหน้า: `feature/`, `bugfix/`, `hotfix/`
- ใช้ lowercase + hyphen (ไม่ใช้ space)

**สิ่งที่ได้เรียน:**
- `git checkout -b <name>` = สร้าง branch + เข้าไป
- Branch ใหม่สร้างจาก commit ปัจจุบัน (HEAD)

---

### Step 3: ตรวจสอบว่าเข้า Branch ที่ถูกต้อง

**คำสั่ง:**
```bash
git branch
```

**ผลลัพธ์:**
```
* feature/seo-improvements
  main
```

**ความหมาย:**
- `* feature/seo-improvements` = **ตอนนี้อยู่ที่นี่**
- `  main` = main branch ยังอยู่ (ไม่ได้ลบ)

**สิ่งที่ได้เรียน:**
- Branch ก่อนหน้าไม่ได้ลบ สามารถกลับไปได้เสมอ
- `*` บอกว่า branch ไหนเป็น current

---

### Step 4: ตรวจสอบ Git Status

**คำสั่ง:**
```bash
git status
```

**ผลลัพธ์:**
```
On branch feature/seo-improvements
Changes not staged for commit:
  modified: .DS_Store

Untracked files:
  GIT_LEARNING_NOTES.md

no changes added to commit
```

**ความหมาย:**
- ✅ ปัจจุบันอยู่ที่ **feature/seo-improvements**
- ✅ GIT_LEARNING_NOTES.md ยังไม่ commit

**สิ่งที่ได้เรียน:**
- `git status` = ตรวจสอบ branch + files ที่เปลี่ยน
- "On branch X" = บอกว่าอยู่ branch ไหน

---

## 📌 Part 6: Branch Management

### Branch Commands

| Task | คำสั่ง | หมายเหตุ |
|------|--------|---------|
| ดูทั้งหมด | `git branch` | ท้องถิ่น + current |
| ดู remote | `git branch -r` | branches บน GitHub |
| สร้าง + เข้า | `git checkout -b <name>` | สร้างแล้วเปลี่ยนไป |
| เข้า branch | `git checkout <name>` | เปลี่ยนไปอีก branch |
| เปลี่ยนชื่อ | `git branch -m <old> <new>` | rename branch |
| ลบ local | `git branch -d <name>` | ลบจาก local |
| ลบ remote | `git push origin --delete <name>` | ลบจาก GitHub |
| Push branch | `git push -u origin <name>` | ส่งไปที่ GitHub |

### Branch Naming Convention

```
feature/seo-improvements     = ฟีเจอร์ใหม่
bugfix/header-mobile-issue   = แก้ไข bug
hotfix/urgent-security-fix   = ด่วน แก้ไข
refactor/css-cleanup         = ปรับปรุง code
docs/update-readme           = อัพเดท documentation
```

---

## 📌 Checklist — Step 2

- ✅ ตรวจสอบ branch ปัจจุบัน (git branch)
- ✅ สร้าง branch feature/seo-improvements
- ✅ เข้าไป branch นั้น
- ✅ ตรวจสอบว่าเข้า branch ที่ถูกต้อง
- ✅ ตรวจสอบ git status
- ✅ Commit GIT_LEARNING_NOTES.md

---

## 📌 Part 7: Push Branch ไปที่ GitHub

### 7.1 ทำไมต้อง Push Branch?

**Push** = ส่งข้อมูลจาก local ไปยัง GitHub

**ประโยชน์:**
✅ บันทึกความก้าวหน้า  
✅ ทีมเห็นได้ (collaboration)  
✅ เตรียม Pull Request  
✅ Backup บน GitHub

---

### Step 1: Push Branch ไปที่ GitHub

**คำสั่ง:**
```bash
git push -u origin feature/seo-improvements
```

**พูดแบบชาวบ้าน:**
> "ส่ง branch feature/seo-improvements ไปยัง GitHub และตั้งให้มันเป็น upstream"

**ความหมาย:**
- `git push` = ส่งข้อมูลไปที่ GitHub
- `-u` = upstream (ตั้งค่านี้ไว้ ครั้งต่อไปไม่ต้องพิมพ์)
- `origin` = ชื่อ remote (GitHub)
- `feature/seo-improvements` = branch ที่ส่ง

**ผลลัพธ์:**
```
Create a pull request for 'feature/seo-improvements' on GitHub by visiting:
https://github.com/jaturong/sky-united-website/pull/new/feature/seo-improvements

* [new branch]      feature/seo-improvements -> feature/seo-improvements
branch 'feature/seo-improvements' set up to track 'origin/feature/seo-improvements'.
```

**ความหมาย:**
- ✅ Branch ส่งไปที่ GitHub สำเร็จ
- ✅ GitHub แนะนำให้สร้าง Pull Request
- ✅ Upstream tracking ตั้งแล้ว (ครั้งต่อไปพิมพ์ `git push` ได้เลย)

**สิ่งที่ได้เรียน:**
- `git push -u origin <branch>` = ส่งไปครั้งแรก + ตั้ง upstream
- `-u` = upstream tracking
- ครั้งต่อไปอาจใช้แค่ `git push` (เข้าใจแล้ว)

---

### Step 2: ตรวจสอบ Branch (Local + Remote)

**คำสั่ง:**
```bash
git branch -a
```

**ผลลัพธ์:**
```
* feature/seo-improvements
  main
  remotes/origin/feature-seo-improvements
  remotes/origin/main
```

**ความหมาย:**
- `* feature/seo-improvements` = **local branch ปัจจุบัน**
- `main` = local main
- `remotes/origin/feature-seo-improvements` = **branch บน GitHub**
- `remotes/origin/main` = main บน GitHub

**สิ่งที่ได้เรียน:**
- `git branch -a` = ดูทั้งหมด (local + remote)
- `remotes/origin/X` = branches บน GitHub
- ตอนนี้ GitHub เห็น branch ของเรา ✅

---

## 📌 Part 8: Upstream Tracking คืออะไร?

**Upstream** = ความเชื่อมโยงระหว่าง local branch และ remote branch

**ถ้าตั้ง upstream แล้ว:**
```bash
git push       # ไม่ต้องระบุ origin/feature/seo-improvements
git pull       # ดึงข้อมูลจาก upstream โดยอัตโนมัติ
```

**ถ้าไม่ตั้ง upstream:**
```bash
git push origin feature/seo-improvements     # ต้องระบุ origin + branch
```

**ข้อสำคัญ:** `-u` ตั้ง upstream ไว้เพื่อให้ workflow ง่ายขึ้น

---

## 📌 Checklist — Step 3

- ✅ Push branch ไปที่ GitHub (git push -u origin feature/seo-improvements)
- ✅ GitHub สร้าง remote branch อัตโนมัติ
- ✅ Upstream tracking ตั้งแล้ว
- ✅ ตรวจสอบด้วย git branch -a

---

## 📌 Part 9: Pull Request (PR) Workflow

### 9.1 Pull Request คืออะไร?

**Pull Request (PR)** = การขอให้ main branch รับการเปลี่ยนแปลงจาก feature branch

**Workflow:**
```
1. Create branch (feature/seo-improvements)     ✅ เสร็จแล้ว
2. Make changes + commit                        ⏳ ต่อไป
3. Push to GitHub                               ✅ เสร็จแล้ว
4. Create Pull Request                          ✅ เสร็จแล้ว
5. Code Review (optional)
6. Merge ไปที่ main
7. Delete feature branch
8. Tag ใหม่ (v1.1)
```

### 9.2 ทำไมต้องใช้ PR?

✅ **Review code** — ตรวจสอบก่อน merge  
✅ **Discussion** — คนอื่นสามารถแสดงความเห็นได้  
✅ **CI/CD** — GitHub รันเทส โดยอัตโนมัติ  
✅ **History** — มีบันทึก PR ไว้อ้างอิง

---

### Step 1: สร้าง PR บน GitHub

**วิธี:**
1. ไปที่ GitHub repository
2. คลิก "Compare & pull request" button
3. หรือไป Pull requests tab → "New pull request"

**ตัวอย่าง (เป็นจริง):**
```
Title: WIP: SEO Improvements - Phase 1, 2, 3 (H1 tags, meta descriptions, alt text)
```

**Description:**
```
## Purpose
- Add missing H1 tags (16 pages)
- Expand meta descriptions (3 pages)
- Update image alt text (140 images)

## Related Task
- SEO Optimization Task

## Testing
- Tested bilingual (TH/EN)
- Responsive design checked
- No broken links

## Ready for Review
- [ ] Phase 1 (H1 tags)
- [ ] Phase 2 (meta descriptions)
- [ ] Phase 3 (alt text)
```

### Step 2: GitHub Information ที่ได้

**ผลลัพธ์:**
```
WIP: SEO Improvements - Phase 1, 2, 3 #1
Status: Ready to merge ✅
```

**Details:**
- `#1` = PR number ที่ 1
- "Ready to merge" = ไม่มี conflicts
- "jaturong wants to merge 2 commits into main from feature/seo-improvements"
- Commits: 2 (GIT_LEARNING_NOTES.md changes)
- Files changed: 1

**ความหมาย:**
- ✅ PR สร้างสำเร็จ
- ✅ ยังไม่ได้ merge (รอ approval)
- ✅ GitHub ตรวจสอบและไม่เห็น conflicts

**สิ่งที่ได้เรียน:**
- PR ต้องมี title ชัดเจน
- Description ต้องมี Purpose/Testing/Related Task
- GitHub แสดง "Ready to merge" ถ้าไม่มี conflicts

---

## 📌 Part 10: PR Status และ Next Steps

### 10.1 PR Status Indicators

| Status | ความหมาย |
|--------|---------|
| Open | ✅ PR สร้างแล้ว รอ review/merge |
| Ready to merge | ✅ ไม่มี conflicts สามารถ merge ได้ |
| Merged | ✅ feature branch นำเข้า main แล้ว |
| Closed | ❌ ปิด PR โดยไม่ merge |

### 10.2 ต่อไปต้องทำอะไร?

**ตัวเลือก:**

1. **ทำ SEO improvements ต่อไป** (เพื่อให้ PR มีเนื้อหา)
   - Phase 1: เพิ่ม H1 tags
   - Phase 2: Meta descriptions
   - Phase 3: Alt text
   - Commit เพิ่มเติม ลงไป feature/seo-improvements

2. **Merge PR ทันที** (ถ้า PR มีเนื้อหาพอ)
   - คลิก "Merge pull request"
   - Delete feature branch
   - Tag v1.1 ใหม่

**ตอนนี้:** PR มี 2 commits บันทึก git learning เท่านั้น

---

---

## 📌 Part 11: SEO Phase 1 — H1 Tags Implementation

### 11.1 Phase 1 ทำอะไรบ้าง?

**Phase 1:** เพิ่ม H1 tags ใน 16 หน้า

### Step 1: เพิ่ม H1 ใน news.html

**ตำแหน่ง:** หลัง `<div class="page-shell">` ในส่วน main

**เพิ่มข้อความ:**
```html
<h1 class="lth" style="position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border: 0;">ข่าวสาร</h1>
<h1 class="len" style="position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border: 0;">News</h1>
```

**ความหมาย:**
- ✅ เพิ่ม H1 ทั้ง TH + EN
- ✅ ใช้ `sr-only` style (hidden visual, SEO readable)
- ✅ ไม่กระทบ design

**Commit:**
```
2f69916 feat: add h1 tag to news.html for seo (phase 1)
```

### Step 2: ตรวจสอบ Product Pages (15 หน้า)

**รายการเช็ค:**
```bash
for file in products/*.html; do
  h1_count=$(grep -c "<h1>" "$file")
  echo "$file: $h1_count H1 tag(s)"
done
```

**ผลลัพธ์:**
```
✅ mbb.html: 1 H1
✅ ssb.html: 1 H1
✅ ldpe-hdpe.html: 1 H1
✅ vacuum-nylon.html: 1 H1
✅ hic.html: 1 H1
✅ air-bubble.html: 1 H1
✅ cushion-wrap.html: 1 H1
✅ sulfur-free-paper.html: 1 H1
✅ cotton-swabs.html: 1 H1
✅ foam-swabs.html: 1 H1
✅ wipers.html: 1 H1
✅ garments.html: 1 H1
✅ gloves.html: 1 H1
```

**สิ่งที่ค้นพบ:**
- ✅ Product detail pages มี H1 ครบแล้ว!
- ✅ H1 ชี้ไปที่ชื่อสินค้า (เช่น "Moisture Barrier Bags (MBB)")

### 11.2 Phase 1 สำเร็จ! 🎉

**ทั้งหมด 14 หน้า H1 tags:**
```
✅ news.html — เพิ่มใหม่
✅ 13 product detail pages — เหลือแล้ว
```

---

## 📌 Checklist — Phase 1

- ✅ news.html — เพิ่ม H1 (commit 2f69916)
- ✅ 15 product detail pages — มี H1 ครบแล้ว
- ✅ ตรวจสอบด้วย grep
- ✅ สิ่งใดก็ตามที่เพิ่ม PR ก็ update

---

## 📌 Phase 2: Meta Descriptions Implementation

### 12.1 Meta Descriptions คืออะไร?

**Meta description** = ข้อความ 120-155 ตัวอักษร ที่ Google แสดงในผลการค้นหา

**ข้อดี:**
- ✅ ส่งผลต่อ Click-Through Rate (CTR)
- ✅ บอก user ว่าหน้านี้เกี่ยวกับอะไร
- ✅ รวม keywords สำหรับ SEO

### Step 1: ตรวจสอบ Meta Descriptions ปัจจุบัน

**ก่อน:**
```
contact.html: "ติดต่อเรา - บริษัท สกาย ยูไนเต็ด อินดัสเทรียล" (48 chars)
news.html:    "ข่าวสาร - บริษัท สกาย ยูไนเต็ด อินดัสเทรียล" (49 chars)
index.html:   "บริษัท สกาย ยูไนเต็ด อินดัสเทรียล... (ยาว)
```

### Step 2: เขียน Meta Descriptions ใหม่

**Contact.html** (125 chars):
```
ติดต่อเรา - บริษัท สกาย ยูไนเต็ด อินดัสเทรียล ผู้นำบรรจุภัณฑ์ ESD ในประเทศไทย เรียนรู้วิธีการติดต่อและจัดส่งสินค้า
```

**News.html** (116 chars):
```
ข่าวสาร - บริษัท สกาย ยูไนเต็ด อินดัสเทรียล บทความและข้อมูลล่าสุดเกี่ยวกับบรรจุภัณฑ์ ESD และอุตสาหกรรม
```

**Index.html** (65 chars):
```
บริษัท สกาย ยูไนเต็ด อินดัสเทรียล - ผู้นำบรรจุภัณฑ์ ESD และโซลูชันการป้องกันไฟฟ้าสถิต
```

### Step 3: Update & Commit

**Commit:**
```
4fb2ac2 feat: expand meta descriptions for seo (phase 2)
```

**ความหมาย:**
- ✅ Meta descriptions ขยายให้ครบตามมาตรฐาน SEO
- ✅ รวม keywords (ESD, บรรจุภัณฑ์, ไฟฟ้าสถิต)
- ✅ CTR ดีขึ้น

### 12.2 Phase 2 สำเร็จ! 🎉

**ทั้งหมด:**
```
✅ contact.html — meta description ขยาย
✅ news.html — meta description ขยาย
✅ index.html — meta description ย่อให้ดีขึ้น
```

---

**สร้าง:** 2026-06-13  
**ทำการแก้ไขล่าสุด:** 2026-06-13 (Phase 2 meta descriptions)
