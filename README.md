# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.
Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis

**Jaya Jaya Institute tengah menghadapi persoalan serius terkait tingginya angka mahasiswa yang tidak menyelesaikan studi (dropout), yang berpotensi memberikan dampak negatif terhadap citra institusi, penilaian akreditasi, serta kepercayaan publik terhadap mutu pendidikan yang diselenggarakan.**. Ketidaksanggupan dalam mengidentifikasi mahasiswa yang berisiko putus studi sejak awal menghambat langkah-langkah preventif serta pemberian pendampingan secara tepat, yang pada akhirnya dapat mengancam keberlanjutan dan posisi kompetitif institusi di tengah persaingan dunia pendidikan yang semakin ketat.

**Untuk menjawab tantangan ini, institusi perlu memiliki kemampuan untuk mendeteksi dan memperkirakan mahasiswa yang berpotensi mengalami dropout sedini mungkin** sehingga intervensi yang sesuai dapat diberikan guna meningkatkan tingkat penyelesaian studi.

### Cakupan Proyek

- Persiapan Data (Data Preparation)
- Analisis Data Eksploratif (Exploratory Data Analysis - EDA)
- Preprocessing Data sebelum melakukan modeling
- Pengembangan Model Prediktif
- Membuat business dashboard dari faktor penyebab tingginya tingkat dropout
- Deploy ke streamlit

### Persiapan

**Sumber data:**
- [Students' Performance](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/refs/heads/main/students_performance/data.csv)

**Setup environment:**

1. Clone this Repository
   ```bash
   git clone https://github.com/iwacooy/ml-terapan-2.git
   ```

2. Create Anaconda Virtual Environment
   ```bash
   conda env create -f edutech.yml
   ```

3. Activate the Environment
   ```bash
   conda activate edutech-ml-terapan 
   ```

## Business Dashboard
### 📊 Insight Visualisasi Status Mahasiswa per Program Studi
![1](https://github.com/user-attachments/assets/49be0544-9699-4359-8e62-61d581077948)
![2](https://github.com/user-attachments/assets/3e0fdecb-3235-48b0-ad97-aa8a071c5549)
![3](https://github.com/user-attachments/assets/e0a3ed0b-ba5e-46ca-b99a-716c63779758)
## 📊 Insight Data Mahasiswa

### 🎓 Status Akademik Mahasiswa
- **50% mahasiswa telah lulus**, sementara **32% mengalami dropout** dan **18% masih terdaftar (enrolled)**.
- Jurusan **Nursing** memiliki jumlah lulusan tertinggi, namun juga menunjukkan dropout dan pendaftaran aktif yang tinggi.
- Jurusan seperti **Journalism and Communication**, **Communication Design**, dan **Management** juga memiliki tingkat kelulusan tinggi.

### Proporsi Gender
- Sebagian besar mahasiswa adalah **perempuan (65%)**, sementara **laki-laki (35%)**.
- Ketidakseimbangan gender ini perlu dipertimbangkan dalam penyusunan program dan kebijakan pendidikan.

### 🕒 Waktu Perkuliahan
- Mayoritas mahasiswa (89%) mengikuti program **Daytime**, dan hanya 11% mengikuti **Evening Attendance**.
- Ini menunjukkan bahwa sebagian besar mahasiswa mungkin memiliki waktu belajar penuh, dan bisa berdampak pada keterlibatan akademik mereka.

### 🎓 Beasiswa
- **Hanya 25% mahasiswa yang menerima beasiswa**, sedangkan **75% tidak menerima beasiswa**.
- Mengingat korelasi antara beasiswa dan kelulusan yang lebih tinggi pada visual sebelumnya, peningkatan akses terhadap beasiswa bisa menjadi strategi penting dalam menekan angka dropout.

###  Nilai Rata-Rata Penerimaan
- Rata-rata nilai penerimaan mahasiswa berada di angka **126.98**, menunjukkan tingkat seleksi dan kualitas awal mahasiswa relatif sedang.

### 📚Distribusi Dropout Berdasarkan Jurusan
- Jurusan seperti **Management (Evening)** dan **Social Service (Evening)** menunjukkan jumlah dropout yang cukup tinggi.
- **Biofuel Production Technologies** dan **Oral Hygiene** memiliki jumlah mahasiswa yang relatif sedikit, namun presentase dropout tetap perlu dicermati.

---
## 📋 Insight Tambahan: Mode Aplikasi & Penerima Beasiswa

###  Mode Aplikasi Mahasiswa
- Mayoritas mahasiswa mendaftar melalui:
  - **1st Phase - General Contingent** dengan jumlah tertinggi (lebih dari 1.700 mahasiswa).
  - Diikuti oleh **2nd Phase - General Contingent** dan kategori **Over 23 Years Old**.
- Hanya sedikit mahasiswa yang masuk melalui jalur khusus seperti:
  - **Special Contingent (Azores/Madeira Island)**
  - **International Student (Bachelor)**
  - **Transfer** dan **Short Cycle Diploma Holders**

> **Insight**: Strategi penerimaan paling efektif saat ini berada pada jalur **General Contingent**, sedangkan jalur-jalur alternatif memiliki potensi dikembangkan untuk meningkatkan keberagaman latar belakang mahasiswa.

### 🎓 Beasiswa Berdasarkan Gender
- Lebih banyak mahasiswa **tidak menerima beasiswa**, baik laki-laki maupun perempuan.
- Dari total penerima beasiswa:
  - **Perempuan** lebih banyak menerima beasiswa dibandingkan **laki-laki**.
  
> **Insight**: Ketimpangan akses beasiswa perlu ditinjau lebih lanjut, dan perluasan program beasiswa berpotensi meningkatkan akses pendidikan, khususnya bagi kelompok rentan.

---



## Menjalankan Sistem Machine Learning

Untuk mendukung institusi dalam mengidentifikasi potensi siswa yang berisiko mengalami dropout serta melakukan pencegahan secara dini, telah dikembangkan sebuah sistem prediksi. Sistem ini dibangun menggunakan framework **Streamlit**.
Untuk menjalankan sistem ini secara lokal, Anda dapat menggunakan perintah berikut pada **Terminal**:

```bash
streamlit run app.py
```

Sistem prediksi tersebut juga tersedia secara online dan dapat diakses langsung melalui [tautan berikut ini](https://submission-2-edutech.streamlit.app/). Sistem ini telah dideploy menggunakan **Streamlit Cloud**, sehingga pengguna tidak perlu melakukan instalasi atau konfigurasi lokal untuk mencobanya.


## Conclusion

Berdasarkan visualisasi data mahasiswa, berikut adalah poin-poin utama yang dapat disimpulkan:

1. **Status Akademik Mahasiswa**
   - Sebanyak **50% mahasiswa telah lulus (graduate)**, namun terdapat **32% yang dropout**, menunjukkan adanya risiko putus studi yang cukup tinggi.
   - Program studi seperti **Nursing** dan **Journalism and Communication** memiliki jumlah mahasiswa tertinggi yang lulus, sementara beberapa jurusan lain menunjukkan angka dropout yang cukup mencolok.

2. **Jenis Kelamin**
   - Komposisi mahasiswa didominasi oleh **perempuan (65%)**, sementara **laki-laki hanya 35%**.
   - Hal ini bisa mencerminkan minat atau preferensi gender terhadap bidang studi tertentu, yang dapat menjadi pertimbangan dalam promosi dan rekrutmen program studi.

3. **Waktu Perkuliahan**
   - Sebagian besar mahasiswa mengikuti **kelas siang (daytime)** sebanyak **89%**, dibandingkan dengan **11% untuk kelas malam (evening)**.
   - Ini menunjukkan kelas siang lebih diminati, mungkin karena persepsi fleksibilitas atau keterjangkauan jadwal.

4. **Beasiswa**
   - Hanya **25% mahasiswa yang menerima beasiswa**, sedangkan **75% lainnya tidak**.
   - Dari penerima beasiswa, mayoritas adalah perempuan, yang bisa menjadi indikator perlunya pemerataan dalam distribusi bantuan pendidikan.

5. **Jalur Masuk**
   - Jalur masuk terbanyak adalah **1st Phase - General Contingent**, diikuti oleh **2nd Phase** dan jalur **Over 23 Years Old**.
   - Jalur-jalur khusus seperti transfer, internasional, atau jalur diploma masih sedikit dimanfaatkan.


### Recommended Action Items

Berikut sejumlah strategi yang bisa diterapkan oleh institusi pendidikan guna menurunkan angka mahasiswa yang tidak menyelesaikan studi:

- **Memperluas cakupan program bantuan pendidikan**, khususnya bagi mahasiswa yang teridentifikasi berisiko tinggi untuk keluar dari studi karena kendala finansial.
- **Menawarkan skema pembayaran fleksibel** seperti cicilan tanpa bunga atau program keringanan pembayaran bagi mahasiswa dengan pencapaian akademik tinggi namun memiliki tunggakan biaya kuliah.
- **Menginisiasi program pendampingan akademik** yang difokuskan pada mahasiswa dengan performa rendah, terutama bagi mereka yang berusia lebih dewasa atau telah menikah.
- **Membangun pusat layanan konseling dan dukungan psikologis**, guna membantu mahasiswa yang mengalami tekanan emosional akibat tantangan akademik atau keuangan.
- **Melakukan monitoring rutin terhadap mahasiswa aktif (enrolled)**, sekaligus menerapkan model prediksi risiko dropout berbasis machine learning yang telah dikembangkan melalui sistem prediksi yang dapat diakses di website berikut: [Student Dropout Prediction](https://submission-2-edutech.streamlit.app/).

