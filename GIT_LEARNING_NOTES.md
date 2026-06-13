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

**สร้าง:** 2026-06-13  
**ทำการแก้ไขล่าสุด:** 2026-06-13
