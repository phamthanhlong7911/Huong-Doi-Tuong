class CanBo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi

    def hien_thi_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Tuổi: {self.tuoi}")
        print(f"Giới tính: {self.gioi_tinh}")
        print(f"Địa chỉ: {self.dia_chi}")


class CongNhan(CanBo):
    def __init__(self, bac, ho_ten, tuoi, gioi_tinh, dia_chi):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac

        if 1 <= self.bac <= 10:
            self.bac = bac
        else:
            raise ValueError("Bậc phải nằm trong khoảng từ 1 đến 10")

    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()
        print(f"Bậc : {self.bac}")


class Ky_su(CanBo):
    def __init__(self, nganh_dao_tao, ho_ten, tuoi, gioi_tinh, dia_chi):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh_dao_tao = nganh_dao_tao

    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()
        print(f"Ngành đào tạo : {self.nganh_dao_tao}")


class nhan_vien(CanBo):
    def __init__(self, cong_viec, ho_ten, tuoi, gioi_tinh, dia_chi):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()
        print(f"Công việc : {self.cong_viec}")


class QLCB:
    def __init__(self):
        self.danh_sach_can_bo = []

    def them_can_bo(self, cb):
        self.danh_sach_can_bo.append(cb)

    def tim_kiem_theo_ho_ten(self, ho_ten):
        for can_bo in self.danh_sach_can_bo:
            if can_bo.ho_ten == ho_ten:
                can_bo.hien_thi_thong_tin()

    def hien_thi_danh_sach(self):
        for can_bo in self.danh_sach_can_bo:
            can_bo.hien_thi_thong_tin()

    def xoa_can_bo_theo_ten(self, ho_ten):
        for can_bo in self.danh_sach_can_bo:
            if can_bo.ho_ten == ho_ten:
                self.danh_sach_can_bo.remove(can_bo)
            can_bo.hien_thi_thong_tin()


if __name__ == "__main__":
    ql = QLCB()

    cb2 = Ky_su("Tran Thi B", 28, "Nữ", "TP HCM", "Cơ khi")
    cb3 = nhan_vien("Le Van C", 25, "Nam", "Đà Nẵng", "Lễ tân")
    ql.them_can_bo(cb2)
    ql.them_can_bo(cb3)

    print("== DANH SÁCH CÁN BỘ ==")
    ql.hien_thi_danh_sach()

    print("== XOÁ CÁN BỘ CÓ TÊN 'Tran Thi B' ==")
    ql.xoa_can_bo_theo_ten("Tran Thi B")

    print("== DANH SÁCH SAU KHI XOÁ ==")
    ql.hien_thi_danh_sach()
