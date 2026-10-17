import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "7 Kebiasaan Anak Indonesia Hebat"
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT

    # --- Header Aplikasi ---
    header = ft.Column(
        controls=[
            ft.Text("7 Kebiasaan Anak Indonesia Hebat", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_800),
            ft.Text("Dibuat oleh: Dennis Pardjer", size=14, weight=ft.FontWeight.W_500, color=ft.colors.BLUE_600),
            ft.Container(height=5),
            ft.Text("Isi data absensi dan beri tanda centang pada kebiasaan yang sudah kamu lakukan hari ini!", size=13, color=ft.colors.GREY_700, text_align=ft.TextAlign.CENTER),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # --- Section 1: Form Absensi (Nama & Tanggal) ---
    input_nama = ft.TextField(
        label="Nama Lengkap",
        hint_text="Masukkan nama kamu...",
        prefix_icon=ft.icons.PERSON,
        border_radius=10,
        expand=True
    )

    # Tanggal otomatis hari ini (format: YYYY-MM-DD)
    tanggal_sekarang = datetime.now().strftime("%Y-%m-%d")
    input_tanggal = ft.TextField(
        label="Tanggal Absen",
        value=tanggal_sekarang,
        prefix_icon=ft.icons.CALENDAR_TODAY,
        border_radius=10,
        expand=True
    )

    form_absensi = ft.Card(
        content=ft.Container(
            padding=15,
            content=ft.Column(
                controls=[
                    ft.Text("Data Absensi", size=18, weight=ft.FontWeight.BOLD),
                    ft.ResponsiveRow(
                        controls=[
                            ft.Container(content=input_nama, col={"sm": 12, "md": 6}),
                            ft.Container(content=input_tanggal, col={"sm": 12, "md": 6}),
                        ]
                    )
                ]
            )
        )
    )

    # --- Section 2: Daftar 7 Kebiasaan ---
    kebiasaan_list = [
        "1. Bangun Pagi Tepat Waktu",
        "2. Beribadah dan Berdoa",
        "3. Merapikan Tempat Tidur & Membantu Orang Tua",
        "4. Mandi Bersih dan Sarapan Sehat",
        "5. Belajar dan Membaca Buku",
        "6. Berolahraga atau Beraktivitas Fisik",
        "7. Tidur Malam Tidak Terlalu Larut"
    ]

    # Membuat checkbox untuk masing-masing kebiasaan
    checkboxes = [ft.Checkbox(label=k, value=False) for k in kebiasaan_list]

    form_kebiasaan = ft.Card(
        content=ft.Container(
            padding=15,
            content=ft.Column(
                controls=[
                    ft.Text("Daftar Kebiasaan Hari Ini", size=18, weight=ft.FontWeight.BOLD),
                    *checkboxes
                ]
            )
        )
    )

    # --- Section 3: Status & Output Hasil ---
    txt_hasil = ft.Text(value="", size=14, color=ft.colors.GREEN_700, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)

    def simpan_absensi(e):
        nama = input_nama.value.strip()
        tgl = input_tanggal.value.strip()

        if not nama:
            txt_hasil.value = "⚠️ Harap masukkan nama terlebih dahulu!"
            txt_hasil.color = ft.colors.RED
        else:
            # Menghitung berapa kebiasaan yang dicentang
            tercentang = [cb.label for cb.value, cb in zip([c.value for c in checkboxes], checkboxes) if cb.value]
            
            txt_hasil.value = (
                f"✅ Absen Berhasil!\n"
                f"Nama: {nama}\n"
                f"Tanggal: {tgl}\n"
                f"Kebiasaan Selesai: {len(tercentang)} dari 7"
            )
            txt_hasil.color = ft.colors.GREEN_800
        
        page.update()

    btn_simpan = ft.ElevatedButton(
        text="Simpan Absen & Kebiasaan",
        icon=ft.icons.SAVE,
        style=ft.ButtonStyle(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.BLUE_600,
            padding=15
        ),
        on_click=simpan_absensi
    )

    # Footer Kredit Pembuat
    footer = ft.Text("© Aplikasi 7 Kebiasaan - Developed by Dennis Pardjer", size=11, color=ft.colors.GREY_500)

    # --- Menambahkan Semua Elemen ke Halaman ---
    page.add(
        header,
        ft.Divider(height=20, color=ft.colors.TRANSPARENT),
        form_absensi,
        form_kebiasaan,
        ft.Container(height=10),
        ft.Column(
            controls=[btn_simpan, txt_hasil, ft.Container(height=10), footer],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)