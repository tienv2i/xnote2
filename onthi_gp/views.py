from django.shortcuts import render


def index(request):
    file_list = [
        {'slug': 'chi_duoi_1', 'title': 'Giải phẫu Chi dưới Phần 1'},
        {'slug': 'chi_duoi_2', 'title': 'Giải Phẫu Chi dưới Phần 2'},
        {'slug': 'chi_tren', 'title': 'Giải Phẫu Chi trên'},
        {'slug': 'chi_tren_2', 'title': 'Giải phẫu chi trên phần 2'},
        {'slug': 'ck1_2024', 'title': 'Giải Phẫu Chi dưới Phần 2'},
        {'slug': 'co_xuong_khop', 'title': 'Module cơ xương khớp'},
        {'slug': 'dau_mat_co', 'title': 'Đầu mặt cổ'},
        {'slug': 'gp_bung', 'title': 'Giải Phẫu Bụng'},
        {'slug': 'gp_dai_cuong', 'title': 'Moldule Giải phẫu đại cương'},
        {'slug': 'gp_nguc', 'title': 'Giải Phẫu Ngực'},
        {'slug': 'ho_hap', 'title': 'Module hô hấp'},
        {'slug': 'ngau_nhien_120', 'title': '120 câu ngẫu nhiên'},
        {'slug': 'sinh_san', 'title': 'Module sinh sản'},
        {'slug': 'thac_si_2024', 'title': 'Đề ghi lại Thạc sĩ 2024 (Đọc đáp án)'},
        {'slug': 'than_kinh_1', 'title': 'Giải phẫu Thần kinh phần 1'},
        {'slug': 'than_kinh_2', 'title': 'Giải phẫu Thần kinh phần 2'},
        {'slug': 'than_minh', 'title': 'Thân mình'},
        {'slug': 'tiet_nieu', 'title': 'Module tiết niệu'},
        {'slug': 'tieu_hoa', 'title': 'Module tiêu hóa'},
        {'slug': 'tim_mach', 'title': 'Module tim mạch'},
        {'slug': 'tk_nt_gq', 'title': 'Module thần kinh-nội tiết- giác quan'},
    ] 
    context = {

        'file_list' : file_list,
    }
    return render(request, "onthi_gp/index.html", context)

# Create your views here.
def onthi(request, chu_de):
    template_name = f"onthi_gp/crawl_data/{chu_de}.html"
    context = {
        "template_name": template_name,
    }
    return render(request, "onthi_gp/onthi.html", context)