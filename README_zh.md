#外星人盒子：环球音乐圣经👽

![Alien Box](alien_imagotype/screen.png)

🌐 **其他语言版本:** [🇬🇧 English](README.md) | [🇪🇸 Español](README_es.md) | [🇩🇪 Deutsch](README_de.md) | [🇷🇺 Русский](README_ru.md) | [🇯🇵 日本語](README_ja.md) | [🇺🇦 Українська](README_uk.md) | **🇨🇳 中文**

---

---

**Alien Box** 是最先进的多模式取证音频分析引擎和 DAW 模板生成器。它直接连接到全球音乐网络，从任何文本输入中提取真实的元数据，剖析商业曲目的频率和动态参数，并为主要 DAW（Ableton、Logic Pro、Cubase、FL Studio、Pro Tools）生成定制的入门模板。

由 **CHUS BZN** 在 **produktes-code** 上采用精密工程构建。

## 🚀 特点
- **通用搜索：** 输入任何 YouTube 链接、Spotify 链接或自由文本（例如“The Prodigy Poison”）。
- **残酷的取证分析：** 计算目标 LUFS、特定 EQ 曲线（底鼓/低音交叉）和 VCA 压缩启动/释放时间。
- **多模式导出：** 生成包含预先路由的 DAW 模板的真实 ZIP 文件。
- **有机用户界面：** 流畅、呼吸的图形界面，具有动态粒子背景。
- **原生通用 PDF 手册 (V14)：** 生成的高分辨率 PDF 手册对称翻译为 7 种语言，精心格式化并完美缩放，适合 DIN A5 打印。

## 🛠 安装

### 1. 后端设置
后端运行在轻量级 Python 服务器上。
````bash
# 1.启动分析服务器
python3 Alienbox_server.py
````

### 2. 前端
只需在任何现代网络浏览器中打开“splash_screen_organic_v3_final/code.html”即可。

### 3.生成手册(V14)
要以 DIN A5 布局编写绝对对称的 V14 通用手册：
````bash
python3 build_universal_manual_v14.py
节点 print_multilingual_v14_pdf.js
````

## 📦 构建安装程序（macOS 和 Windows）
为了将 Alien Box 打包到本机桌面应用程序中，我们为 Electron/PyInstaller 提供了构建脚本。这为我们的 GitHub 存储库准备了发布。

* **Mac 操作系统 (.dmg):** 运行 `./build_mac.sh`
* **Windows (.exe):** 运行 `build_win.bat`

---
*“产品代码”生态系统的一部分。 CC BY-NC-SA 4.0。企业标准 - 零售就绪。*