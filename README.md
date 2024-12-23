# Insider UI Test Otomasyon
Bu projede "https://useinsider.com/ " domaininde 5 adımlı bir otomasyon senaryosu yazılmıştır. Proje Python dilinde yazılmış olup, selenium ve python kütüphaneleri kullanılmıştır. Proje page object model(POM) yapısına uygun olarak yazılmıştır. Bu projede yer alan sınıf ve fonksiyonlar aşağıdaki gibidir:
## base.page_py
BasePage sayfası senaryolarda çok sık kullandığım metotları daha kısa hale getirip daha anlışılır kılmak amacıyla kullandığım bir class. Bu classta oluşturulan metodlar ve kullanım amaçları:
find_element: İçine verilen By tipindeki locator değerini sayfada var olana kadar bekleyip bu elementi bulmaya yarayan metot.
click_element: Element tıklanabilir olana kadar bekleyip ilgili elemente tıklayan metot.
is_element_present: Metodun içine verilen locator değerinin görünür olup olmadığını kontrol etmek için yazdığım metot.
scroll_to_element: Belli bir elemente kadar sayfanın sürüklenmesini sağlayan metod.
scroll_by: Belli değerlerde sayfanın sürüklenmesi için yazdığım metod.
## careers.page_py
Careers sayfasına özgü adımları içerir.
navigate_to_teams: Tüm ekipler butonuna basarak sayfayı genişletmeye yarayan metottur.
## home_page.py
Ana sayfada yapılan menü işlemlerini (Company> Careers) içerir. Ayrıca cookileri kabul eden bir metod barındırıyor.
accept_cookie
navigate_to_company
navigate_to_careers
## jobs_page.py
Kullanıcının iş ilanlarını filtreleyebilmesi ve kendisi için uygun olan ilanın başvuru sayfasına ulaşması için gerekli metodları bulunduruyor.
filter_jobs_by_location: iş ilanlarını belirli bir lokasyona göre filtreleme imkanı sağlayan metod."Select" nesnesi oluşturarak açılır menüyü kullanıyor.
verify_job_list_exists: iş ilanları listesinin sayfada mevcut olup olmadığını kontrol ediyor.
view_role: ilanın başvuru sayfasına gidebilmek için view role butonuna tıklıyor. Buton üzrine gelince belirdiği için hover metodunu kullandım.
## qualityassurance_page.py
Qaulity Assurance sayfasına özgü linklerin yönlendirilmesi adımlarını içeriyor.
navigate_to_qa_team
navigate_to_jobs
## insider_test.py
Otomasyona ait adımların , metodlarla birlikte sırayla çağrıldığı main classtır. Otomasyon seneryosunun adımları şu şekildedir:
1-"https://useinsider.com/" sayfasına gidilir ve sayfanın başarıyla yüklendiği kontrol edilir.
2-Menüden Company sonrasında Carees seçilir ve Careers sayfasının başarıyla yüklendiği kontrol edilir.
3- See All Jobs ile sayfa genişletirlerek Quality Assurance seçilir. Filtreleme butonununda "Istanbul, Turkey" konumu filtrelenir. 
4-Bu filtreye uygun ilanların varlığı kontrol edilir.
5.“View Role”butonuna basılarak , url'in Lever Application Form sayfasına yönlendirildiği kontrol edilir.                                                                                                                          
                                                              
