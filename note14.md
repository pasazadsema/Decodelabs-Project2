# Metodologiya
- Bu layihədə 5 əsas Olist e-commerce cədvəli birləşdirilərək vahid dataset formalaşdırılır: orders, order_items, products, order_reviews və product_category_name_translation
- Birləşdirmə əsasən order_id və product_id açarları üzərindən aparılır
- Yalnız “delivered” statuslu sifarişlər saxlanıldı və nəticədə təxminən 96.5K sətrlik təmiz dataset əldə olunur
- Analiz üçün yeni metriklər yaradılır: delivery_time və revenue
- Əsas məqsəd gəlir, çatdırılma performansı və müştəri məmnuniyyəti arasında əlaqəni eyni sistemdə göstərməkdir
# Ümumi KPI 
- Ümumi gəlir 13.59M BRL təşkil edir
- Orta sifariş dəyəri (AOV) 140.7 BRL səviyyəsindədir
- Orta çatdırılma müddəti 12.1 gün olur
- Orta rəy balı 4.09 / 5 olur
# Business insights
- Çatdırılma müddəti artdıqca müştəri məmnuniyyəti azalır Orta çatdırılma 12.1 gün olur və 15+ gün gecikən sifarişlərdə review score 3.5 və daha aşağı olur Bu suala cavab verir ki gecikmə birbaşa müştəri məmnuniyyətini azaldır
- Gəlir yüksək konsentrasiyalıdır bed_bath_table kateqoriyası 1.71M BRL ilə ümumi gəlirin təxminən 12.6 faizini təşkil edir biznes az sayda kateqoriyadan asılıdır və risk konsentrasiyası mövcuddur
- Aşağı rəy alan kateqoriyalar zəif çatdırılma performansına malikdir security_and_services kateqoriyasında orta rəy 2.5 olur və çatdırılma müddəti 15+ gün səviyyəsindədir problem məhsuldan çox əməliyyat gecikməsidir
- Satıcı performansı ciddi şəkildə qeyri-bərabərdir Top 10 satıcı 12.7 faiz gəlir yaradır və ən yaxşı satıcılar 150K–220K BRL zəiflər isə 5K–20K BRL qazanır marketplace-də güclü və zəif satıcılar arasında böyük uçurum var
- Ümumi müştəri məmnuniyyəti yaxşı səviyyədədir lakin çatdırılma problemi qalır Orta review score 4.09 olur və gecikmiş sifarişlərdə bu göstərici 3.5-ə düşür məhsul keyfiyyəti yaxşı olur amma əsas zəif nöqtə delivery performansı olur