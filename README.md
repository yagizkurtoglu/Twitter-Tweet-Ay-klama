# Twitter-Tweet-Ayiklama-Araci
Selenium ile belirli kelimelerin geçtiği tweetleri ayıklama.

<ul>
<li>Tarayıcı (driver) default ingilizce olarak başlatılır.</li>
<li>Fonksiyonun kullanımı i&ccedil;in Login koşulu vardır. Login i&ccedil;in herhangi bir kod eklenmesine gerek yok.</li>
<li>Tweetleri filtrelenecek kullanıcı adı girişi beklenir.</li>
<li>Aranacak her kelime danger dizisine atılır.</li>
<li>B&uuml;t&uuml;n tweetler results dizisine atılır.&nbsp;</li>
<li>Son olarak results dizisindeki b&uuml;t&uuml;n indisler danger dizisi ile karşılaştırılır.&nbsp;</li>
<li>Danger dizisindeki herhangi bir kelime dizide ge&ccedil;iyor ise ge&ccedil;en tweetin tamamını dangerous.txt dosyasına yazar.&nbsp;</li>
<li>5 kere ard arda results dizisinin boyutu değişmez ise scroll daha fazla aşağı inemiyor demektir ve buda b&uuml;t&uuml;n takip edilenler alınmış anlamını taşır.</li>
</ul>
