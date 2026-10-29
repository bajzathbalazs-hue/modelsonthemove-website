# -*- coding: utf-8 -*-
from shell import BASE_URL

ROLUNK_BODY = """
%%BREADCRUMB%%
<section class="subhero">
  <div class="wrap">
    <span class="eyebrow rv">RÓLUNK</span>
    <h1 class="rv">Két ember, egy közös szemlélet.</h1>
    <p class="lead rv">Mindent személyesen viszünk, ezért pontosan tudod, kivel dolgozol, és ki felel az eredményért.</p>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">A TÖRTÉNETÜNK</span>
      <p>Divatbemutatókkal kezdtük, ma pedig prémium eseményeket szervezünk, és cégeknek építünk arculatot, weboldalt és marketinget. A két világ jobban összefügg, mint gondolnád: mindkettőben az számít, hogy az emberek felfigyeljenek rád, és emlékezzenek rád.</p>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="feature-list rv">
      <div class="feature">
        <div class="num">01</div>
        <div><h3>Bajzáth Balázs</h3>
        <p style="color:var(--bronze-bright);font-size:12.5px;letter-spacing:.04em;text-transform:uppercase;margin-bottom:10px;">Alapító · stratégia, weboldal, marketing</p>
        <p>A céges projektek felelőse. Weboldalakat épít, marketingstratégiát tervez és menedzsel, és ő tartja a kapcsolatot az üzleti partnerekkel.</p></div>
      </div>
      <div class="feature">
        <div class="num">02</div>
        <div><h3>Molnár Míra</h3>
        <p style="color:var(--bronze-bright);font-size:12.5px;letter-spacing:.04em;text-transform:uppercase;margin-bottom:10px;">Alapító · tartalom, influencerkapcsolatok, események</p>
        <p>A Miss Universe Hungary 2024 második udvarhölgye. Tartalomgyártóként nagyjából 1,4 millió megtekintést ért el a TikTok-profilján. Ő felel a tartalmak stílusáért, az influencerhálózatért és az események hangulatáért.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">AMIT VALLUNK</span></div>
    <ul class="bullet-list" style="margin:0 auto;">
      <li><b style="color:var(--ivory);">Személyesen:</b> nincs közvetítő, közvetlenül velünk dolgozol.</li>
      <li><b style="color:var(--ivory);">Átláthatóan:</b> azt ígérjük, amit be is tudunk tartani.</li>
      <li><b style="color:var(--ivory);">Mérhetően:</b> minden eredményt számokkal mutatunk meg.</li>
      <li><b style="color:var(--ivory);">Igényesen:</b> a legkisebb részletre is figyelünk.</li>
    </ul>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">CSAPATUNK</span>
      <p>Állandó, profi felszerelésű operatőrünk és vágónk, valamint fotósok, sminkesek, stylistok, jogász és fejlesztők, projektenként összeállítva.</p>
    </div>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="sec-head rv"><span class="eyebrow">SZÁMOKBAN</span></div>
    <div class="stat-row rv-stagger" style="margin-top:0;">
      <div><b>4</b><span>ESEMÉNY</span></div>
      <div><b>10+</b><span>CÉGES PROJEKT</span></div>
      <div><b>16</b><span>INFLUENCERPARTNER</span></div>
      <div><b>≈790 ezer</b><span>ELÉRHETŐ KÖVETŐ</span></div>
    </div>
  </div>
</section>

<section class="cta-band rule">
  <div class="wrap rv">
    <h2>Ismerjük meg egymást.</h2>
    <div class="ctas"><a href="../kapcsolat/" class="btn filled magnetic">Ingyenes konzultációt kérek</a></div>
  </div>
</section>
"""

KAPCSOLAT_BODY = """
%%BREADCRUMB%%
<section class="subhero">
  <div class="wrap">
    <span class="eyebrow rv">KAPCSOLAT</span>
    <h1 class="rv">Írj nekünk.</h1>
    <p class="lead rv">Egy munkanapon belül válaszolunk.</p>
  </div>
</section>

<section class="pad rule">
  <div class="wrap">
    <div class="biz-grid rv">
      <form class="form-panel" id="bizForm" name="kapcsolat" data-netlify="true" data-netlify-honeypot="website" data-motm-form data-msg-id="bizMsg" data-event="contact_form_submit" novalidate style="max-width:560px;">
        <input type="hidden" name="form-name" value="kapcsolat">
        <input type="hidden" name="page_url" value="">
        <input type="hidden" name="referrer_url" value="">
        <div class="hp-field" aria-hidden="true"><label>Weboldal (ne töltsd ki)</label><input type="text" name="website" tabindex="-1" autocomplete="off"></div>

        <div class="field"><label for="k-name">NÉV</label><input id="k-name" name="name" type="text" required></div>
        <div class="field"><label for="k-email">E-MAIL</label><input id="k-email" name="email" type="email" required></div>
        <div class="field"><label for="k-msg">ÜZENET</label><textarea id="k-msg" name="message" required></textarea></div>
        <label class="check"><input type="checkbox" name="consent" required> Elfogadom az Adatvédelmi tájékoztatót.</label>

        <div class="submit-row">
          <button type="submit" class="btn filled magnetic">Elküldöm az üzenetem</button>
        </div>
        <div class="form-msg" id="bizMsg"><h4>KÖSZÖNJÜK.</h4><p>Egy munkanapon belül válaszolunk.</p></div>
      </form>

      <div class="biz-facts">
        <div class="biz-fact"><div class="k">KÖZVETLEN ELÉRHETŐSÉG</div><div class="v">Telefon: <a class="inline" href="tel:+36309404148" style="color:var(--bronze-bright);">+36 30 940 4148</a></div></div>
        <div class="biz-fact"><div class="k">KÖVESS</div><div class="v">
          <a href="https://www.instagram.com/models_on_the_move/" target="_blank" rel="noopener" style="color:var(--bronze-bright);">Instagram</a> ·
          <a href="https://www.facebook.com/profile.php?id=61586682312593" target="_blank" rel="noopener" style="color:var(--bronze-bright);">Facebook</a> ·
          <a href="https://www.tiktok.com/@models.on.the.move" target="_blank" rel="noopener" style="color:var(--bronze-bright);">TikTok</a>
        </div></div>
        <div class="biz-fact"><div class="k">KOMOLYABB PROJEKTED VAN?</div><div class="v">Indítsuk el együtt.<br><a href="../projekt-inditasa/" class="btn small magnetic" style="margin-top:12px;">Elindítom a projektem</a></div></div>
      </div>
    </div>
  </div>
</section>
"""

NOTFOUND_BODY = f"""
<section class="notfound">
  <div class="code">404</div>
  <h1>Ez az oldal nem található.</h1>
  <p>A keresett oldal elköltözött, átnevezésre került, vagy sosem létezett. Nézz vissza a főoldalra, vagy fedezd fel a szolgáltatásainkat.</p>
  <div class="ctas">
    <a href="{BASE_URL}/" class="btn filled magnetic">Visszamegyek a főoldalra</a>
    <a href="{BASE_URL}/kapcsolat/" class="btn magnetic">Írok nektek</a>
  </div>
</section>
"""
