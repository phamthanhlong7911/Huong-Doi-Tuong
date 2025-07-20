class ThiSinh():
    def __init__(self, so_bao_danh, ho_ten, dia_chi, muc_uu_tien):
        self.so_bao_danh = so_bao_danh
        self.ho_ten = ho_ten
        self.dia_chi = dia_chi
        self.muc_uu_tien = muc_uu_tien

    def hien_thi_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Số báo danh: {self.so_bao_danh}")
        print(f"Mức ưu tiên: {self.muc_uu_tien}")
        print(f"Địa chỉ: {self.dia_chi}")


class Hoc_sinh_khoi_A(ThiSinh):
    to_hop_thi = ["Toán", "Lý", "Hóa"]

    def __init__(self, so_bao_danh, ho_ten, dia_chi, muc_uu_tien):
        super().__init__(so_bao_danh, ho_ten, dia_chi, muc_uu_tien)

    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()
        print(f"tổ hợp thi {self.to_hop_thi}")


class Hoc_sinh_khoi_B(ThiSinh):
    to_hop_thi = ["Toán", "Sinh", "Hóa"]

    def __init__(self, so_bao_danh, ho_ten, dia_chi, muc_uu_tien):
        super().__init__(so_bao_danh, ho_ten, dia_chi, muc_uu_tien)

    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()
        print(f"tổ hợp thi {self.to_hop_thi}")


class Hoc_sinh_khoi_C(ThiSinh):
    to_hop_thi = ["Văn", "Sử", "Địa"]

    def __init__(self, so_bao_danh, ho_ten, dia_chi, muc_uu_tien):
        super().__init__(so_bao_danh, ho_ten, dia_chi, muc_uu_tien)

    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()
        print(f"tổ hợp thi {self.to_hop_thi}")


if __name__ == "__main__":
    a = Hoc_sinh_khoi_A("A1", "Phạm Thanh Long", "Khánh Hòa", 1)
    b = Hoc_sinh_khoi_B("B1", "Đoàn Nguyễn Hoàng Lâm", "Nha Trang", 2)
    c = Hoc_sinh_khoi_C("C1", "Ngô Minh Quân", "TP.HCM", 1)

    print("Thông tin thí sinh khối A:")
    a.hien_thi_thong_tin()
    print("\nThông tin thí sinh khối B:")
    b.hien_thi_thong_tin()
    print("\nThông tin thí sinh khối C:")
    c.hien_thi_thong_tin()


class TuyenSinh:
    def __init__(self):
        self.danh_sach_thi_sinh = []

    def them_thi_sinh(self, thi_sinh):
        self.danh_sach_thi_sinh.append(thi_sinh)

    def hien_thi_tat_ca(self):
        for thi_sinh in self.danh_sach_thi_sinh:
            print(thi_sinh.hien_thi_thong_tin())

    def tim_kiem_theo_sbd(self, so_bao_danh):
        for thi_sinh in self.danh_sach_thi_sinh:
            if thi_sinh.so_bao_danh == so_bao_danh:
                thi_sinh.hien_thi_thong_tin()
                return
        print("Không tìm thấy thí sinh với số báo danh:")
