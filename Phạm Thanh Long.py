from guizero import App, Text, TextBox, PushButton, ListBox, Box, Window, warn, info, Combo
import matplotlib.pyplot as plt
import os

class WasteManager:
    def __init__(self, app):
        self.app = app
        self.waste_data = []

        # --- Tiêu đề ---
        Text(app, "🌍 HỆ THỐNG QUẢN LÝ RÁC THẢI & BẢO VỆ MÔI TRƯỜNG",
             size=35, color="darkgreen", font="Arial", align="top")

        # --- Khung nhập liệu ---
        input_box = Box(app, layout="grid", border=True)
        input_box.bg = "#FFFACD"

        Text(input_box, "♻️ Loại rác:", grid=[0, 0], size=25, color="purple")
        # ComboBox thay cho TextBox
        self.waste_type = Combo(input_box, options=[
            "nhựa", "hữu cơ", "giấy", "kim loại", "thủy tinh", "pin", "ắc quy", "điện tử"
        ], grid=[1, 0])
        self.waste_type.text_size = 16
        self.waste_type.text_bold = True

        Text(input_box, "⚖️ Khối lượng (kg):", grid=[0, 1], size=25, color="brown")
        self.waste_amount = TextBox(input_box, grid=[1, 1], width=20, height=23)

        # --- Hàng nút ---
        button_box = Box(input_box, grid=[0, 2, 2, 1], layout="grid")
        self.make_button(button_box, "➕ Thêm", "lightgreen", self.add_waste, 0, 0)
        self.make_button(button_box, "❌ Xóa mục", "tomato", self.delete_selected, 1, 0)
        self.make_button(button_box, "📊 Phân tích", "skyblue", self.analyze_waste, 2, 0)
        self.make_button(button_box, "📋 Thống kê", "orange", self.show_table, 3, 0)
        self.make_button(button_box, "🧹 Xóa toàn bộ", "orchid", self.clear_all, 4, 0)
        self.make_button(button_box, "💾 Xuất báo cáo", "gold", self.export_report, 5, 0)
        self.make_button(button_box, "📈 Biểu đồ", "lightpink", self.plot_chart, 6, 0)
        button_box.text_size = 8
        button_box.text_bold = True
        # --- Danh sách dữ liệu ---
        Text(app, "📋 Danh sách rác đã nhập:", size=25, color="blue")
        self.list_box = ListBox(app, items=[], width=200, height=250)
        self.list_box.bg = "#F0FFF0"
        self.list_box.text_size = 15

        # --- Bảng thống kê ---
        Text(app, "📊 Bảng thống kê:", size=27, color="darkblue")
        self.stats_box = Box(app, layout="grid", border=True)
        self.stats_box.bg = "#E6F7FF"

    # ====== Helper ======
    def make_button(self, box, text, color, cmd, gx, gy):
        btn = PushButton(box, text=text, grid=[gx, gy], width=24, height=3, command=cmd)
        btn.bg = color
        btn.text_color = "black"
        return btn

    # ====== Các chức năng ======
    def add_waste(self):
        waste_type = self.waste_type.value.strip().lower()
        try:
            amount = float(self.waste_amount.value)
        except ValueError:
            warn("Lỗi", "⚠️ Vui lòng nhập số kg hợp lệ!")
            return

        if not waste_type:
            warn("Lỗi", "⚠️ Vui lòng chọn loại rác!")
            return

        self.waste_data.append({"type": waste_type, "amount": amount})
        self.list_box.append(f"{waste_type} - {amount} kg")

        info("Thành công", f"✅ Đã thêm {waste_type} ({amount} kg)")
        self.waste_amount.value = ""

    def delete_selected(self):
        selected = self.list_box.value
        if not selected:
            warn("Thông báo", "⚠️ Vui lòng chọn mục cần xóa!")
            return
        self.list_box.remove(selected)
        self.waste_data = [item for item in self.waste_data if f"{item['type']} - {item['amount']} kg" != selected]

    def clear_all(self):
        self.list_box.clear()
        self.waste_data.clear()

    def search_waste(self):
        keyword = self.search_input.value.strip().lower()
        if not keyword:
            warn("Thông báo", "⚠️ Nhập từ khóa để tìm kiếm!")
            return
        results = [f"{item['type']} - {item['amount']} kg" for item in self.waste_data if keyword in item['type']]
        if results:
            self.list_box.clear()
            self.list_box.append(results)
        else:
            warn("Kết quả", "❌ Không tìm thấy dữ liệu")

    def analyze_waste(self):
        report = self.generate_report()
        if report:
            self.show_report_window("Báo cáo phân tích", report)

    def show_table(self):
        for widget in self.stats_box.children:
            widget.destroy()

        if not self.waste_data:
            Text(self.stats_box, "⚠️ Chưa có dữ liệu", grid=[0, 0], size=22, color="red")
            return

        Text(self.stats_box, "Loại rác", grid=[0, 0], color="blue", size=22)
        Text(self.stats_box, "Khối lượng (kg)", grid=[1, 0], color="blue", size=22)

        detail = {}
        for item in self.waste_data:
            detail[item["type"]] = detail.get(item["type"], 0) + item["amount"]

        row = 1
        for t, amt in detail.items():
            color = "red" if amt > 20 else "black"
            Text(self.stats_box, t, grid=[0, row], size=12, color=color)
            Text(self.stats_box, str(amt), grid=[1, row], size=12, color=color)
            row += 1

    def generate_report(self):
        if not self.waste_data:
            warn("Thông báo", "⚠️ Chưa có dữ liệu để phân tích!")
            return None

        total = sum(item["amount"] for item in self.waste_data)
        detail = {}
        for item in self.waste_data:
            detail[item["type"]] = detail.get(item["type"], 0) + item["amount"]

        report = f"📌 Tổng lượng rác: {total} kg\n"
        for t, amt in detail.items():
            report += f"- {t}: {amt} kg\n"

        report += "\n--- 🔎 Khuyến nghị & Giải pháp ---\n"
        if detail.get("nhựa", 0) > total * 0.3:
            report += "🚫 Nhựa nhiều → hạn chế túi nilon, dùng túi sinh học.\n"
        if detail.get("hữu cơ", 0) > total * 0.4:
            report += "🌱 Hữu cơ nhiều → triển khai mô hình ủ compost, Biogas.\n"
        if detail.get("giấy", 0) > 10:
            report += "📚 Giấy nhiều → tái chế giấy, in 2 mặt, văn phòng điện tử.\n"

        report += "\n--- 🌍 Giải pháp tổng thể ---\n"
        report += "1️⃣ Phân loại rác tại nguồn.\n2️⃣ Tái chế - Tái sử dụng.\n3️⃣ Giáo dục cộng đồng về Zero Waste.\n"

        return report

    def export_report(self):
        report = self.generate_report()
        if report:
            filename = "bao_cao_rac_thai.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(report)
            info("Xuất báo cáo", f"💾 Báo cáo đã lưu: {os.path.abspath(filename)}")

    def show_report_window(self, title, content):
        win = Window(self.app, title, width=900, height=680)
        Text(win, title, size=27, color="darkblue")
        box = Box(win, width="fill", height="fill")
        txt = TextBox(box, text=content, multiline=True, scrollbar=True, width=120, height=35)
        txt.text_size = 20
        txt.bg = "#FDF5E6"

    def plot_chart(self):
        if not self.waste_data:
            warn("Thông báo", "⚠️ Không có dữ liệu để vẽ biểu đồ!")
            return

        detail = {}
        for item in self.waste_data:
            detail[item["type"]] = detail.get(item["type"], 0) + item["amount"]

        labels = list(detail.keys())
        sizes = list(detail.values())

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title("Tỉ lệ các loại rác")
        plt.show()


# ====== MAIN APP ======
if __name__ == "__main__":
    app = App("Quản lý Rác thải & Môi Trường", width=1500, height=1200, bg="lightblue")
    WasteManager(app)
    app.display()
