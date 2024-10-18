## FontBakery report

fontbakery version: 0.12.10





## Check results



<details><summary>[17] Samaano-Italic[wdth,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> STAT table has Axis Value tables? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.stat.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>STAT table has no Axis Value tables.</p>
 [code: no-axis-value-tables]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.metrics.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 978, but got 958 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">nl_Latn (Dutch)</td>
<td align="left">Shaper didn't attach acutecomb to j</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Validate STAT particle names and values match the fallback names in GFAxisRegistry. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.axisregistry.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>STAT table is missing Axis Value Records</p>
 [code: missing-axis-values]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 434 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check glyphs in mark glyph class are non-spacing. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following spacing glyphs may be in the GDEF mark glyph class by mistake:
glyph094D (unencoded), uni0930_uni094D.blwf (unencoded), uni0930_uni094D.rphf (unencoded), uni093A (U+093A), uni093C (U+093C), uni0945 (U+0945), uni0946 (U+0946), uni0947 (U+0947), uni0948 (U+0948), uni0951 (U+0951), uni0952 (U+0952), uni0953 (U+0953), uni0954 (U+0954), uni0955 (U+0955), uni0956 (U+0956), uni0957 (U+0957), uni0962 (U+0962) and uni0963 (U+0963)</p>
 [code: spacing-mark-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
hookabovecomb (U+0309) and uni0305 (U+0305)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>









* ⚠️ **WARN** <p>dcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>Lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>tcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Detect any interpolation issues in the font. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Interpolation issues were found in the font:</p>
<pre><code>- Contour order differs in glyph 'uni094C_uni0902.abvs': [0, 1, 2, 3, 4] in wght=700,wdth=100, [0, 1, 3, 4, 2] in wght=700,wdth=200.

- Contour 4 start point differs in glyph 'uni094C_uni0902.abvs' between location wght=700,wdth=100 and location wght=700,wdth=200

- Contour order differs in glyph 'uni094C_uni0902.abvs': [0, 1, 2, 3, 4] in wght=700,wdth=200, [0, 1, 2, 4, 3] in wght=100,wdth=100.

- Contour order differs in glyph 'uni094C_uni0902.abvs': [0, 1, 2, 3, 4] in wght=100,wdth=100, [0, 1, 3, 4, 2] in wght=100,wdth=200.

- Contour order differs in glyph 'uni0946_uni0902.abvs': [0, 1, 2, 3, 4] in wght=700,wdth=100, [0, 3, 2, 4, 1] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0946_uni0902.abvs': [0, 1, 2, 3, 4] in wght=700,wdth=200, [0, 1, 2, 4, 3] in wght=100,wdth=100.

- Contour order differs in glyph 'uni0946_uni0902.abvs': [0, 1, 2, 3, 4] in wght=100,wdth=100, [0, 1, 2, 4, 3] in wght=100,wdth=200.

- Contour order differs in glyph 'uni0949_uni0902.abvs': [0, 1, 2, 3, 4, 5] in wght=700,wdth=100, [0, 1, 5, 3, 4, 2] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0947_uni0902.abvs': [0, 1, 2] in wght=700,wdth=100, [0, 2, 1] in wght=700,wdth=200.

- Contour 2 start point differs in glyph 'uni0947_uni0902.abvs' between location wght=700,wdth=100 and location wght=700,wdth=200

- Contour order differs in glyph 'uni0946_uni0930_uni094D.abvs': [0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=100, [4, 1, 5, 3, 6, 2, 0] in wght=700,wdth=200.

- Contour 0 start point differs in glyph 'uni0946_uni0930_uni094D.abvs' between location wght=700,wdth=100 and location wght=700,wdth=200

- Contour 0 in glyph 'uni0946_uni0930_uni094D.abvs': becomes underweight between wght=700,wdth=100 and wght=700,wdth=200.

- Contour 5 start point differs in glyph 'uni0946_uni0930_uni094D.abvs' between location wght=700,wdth=100 and location wght=700,wdth=200

- Contour 6 start point differs in glyph 'uni0946_uni0930_uni094D.abvs' between location wght=700,wdth=100 and location wght=700,wdth=200

- Contour 6 in glyph 'uni0946_uni0930_uni094D.abvs': becomes underweight between wght=700,wdth=100 and wght=700,wdth=200.

- Contour order differs in glyph 'uni0945_uni0930_uni094D.abvs': [0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=100, [4, 2, 5, 3, 6, 0, 1] in wght=700,wdth=200.

- Contour 0 start point differs in glyph 'uni0945_uni0930_uni094D.abvs' between location wght=700,wdth=100 and location wght=700,wdth=200

- Contour 0 in glyph 'uni0945_uni0930_uni094D.abvs': becomes underweight between wght=700,wdth=100 and wght=700,wdth=200.

- Contour 1 start point differs in glyph 'uni0945_uni0930_uni094D.abvs' between location wght=700,wdth=100 and location wght=700,wdth=200

- Contour 1 in glyph 'uni0945_uni0930_uni094D.abvs': becomes underweight between wght=700,wdth=100 and wght=700,wdth=200.

- Contour 5 start point differs in glyph 'uni0945_uni0930_uni094D.abvs' between location wght=700,wdth=100 and location wght=700,wdth=200

- Contour 5 in glyph 'uni0945_uni0930_uni094D.abvs': becomes underweight between wght=700,wdth=100 and wght=700,wdth=200.

- Contour order differs in glyph 'uni0945_uni0902.abvs': [0, 1, 2, 3, 4] in wght=700,wdth=100, [0, 2, 3, 4, 1] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0945_uni0902.abvs': [0, 1, 2, 3, 4] in wght=100,wdth=100, [0, 1, 2, 4, 3] in wght=100,wdth=200.

- Contour order differs in glyph 'Dcaron': [0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=100, [0, 1, 2, 5, 4, 6, 3] in wght=700,wdth=200.

- Contour 3 start point differs in glyph 'Dcaron' between location wght=700,wdth=100 and location wght=700,wdth=200

- Contour 3 in glyph 'Dcaron': becomes underweight between wght=700,wdth=100 and wght=700,wdth=200.

- Contour 5 start point differs in glyph 'Dcaron' between location wght=700,wdth=100 and location wght=700,wdth=200

- Contour 5 in glyph 'Dcaron': becomes underweight between wght=700,wdth=100 and wght=700,wdth=200.

- Contour order differs in glyph 'Dcaron': [0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=200, [0, 6, 2, 1, 4, 3, 5] in wght=100,wdth=100.

- Contour 1 in glyph 'Dcaron': becomes underweight between wght=700,wdth=200 and wght=100,wdth=100.

- Contour 5 start point differs in glyph 'Dcaron' between location wght=700,wdth=200 and location wght=100,wdth=100

- Contour 5 in glyph 'Dcaron': becomes underweight between wght=700,wdth=200 and wght=100,wdth=100.

- Contour 6 start point differs in glyph 'Dcaron' between location wght=700,wdth=200 and location wght=100,wdth=100

- Contour 6 in glyph 'Dcaron': becomes underweight between wght=700,wdth=200 and wght=100,wdth=100.

- Contour order differs in glyph 'uni0948_uni0902.abvs': [0, 1, 2, 3] in wght=700,wdth=100, [0, 2, 3, 1] in wght=700,wdth=200.

- Contour 3 start point differs in glyph 'uni0948_uni0902.abvs' between location wght=700,wdth=100 and location wght=700,wdth=200

- Contour 3 in glyph 'uni0948_uni0902.abvs': becomes underweight between wght=700,wdth=100 and wght=700,wdth=200.
</code></pre>
 [code: interpolation-issues]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- glyph094D

- uni0930_uni094D.abvs

- uni0930_uni094D.vatu
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, cherokee, tifinagh, coptic</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: coptic, math, gothic, elbasan, glagolitic</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: malayalam, coptic, todhri, canadian-aboriginal, duployan, math, hebrew, tifinagh, syriac, tai-le, old-permic</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: cherokee, caucasian-albanian, thai, gothic, tifinagh, syriac, sunuwar</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>devanagari</code>, <code>latin</code>, <code>latin-ext</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̅ i̇ ỉ ǐ ị̅ ị̇ ị̉ ị̊ ị̋ ị̌ i̦̅ i̦̇ ỉ̦ i̦̊ i̦̋ ǐ̦ i̧̅ i̧̇ ỉ̧ i̧̊</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Basaa (Latn, 332,940 speakers), Lugbara (Latn, 2,200,000 speakers), Dii (Latn, 71,000 speakers), Avokaya (Latn, 100,000 speakers), Southern Kisi (Latn, 360,000 speakers), Dutch (Latn, 31,709,104 speakers), Vute (Latn, 21,000 speakers), Gulay (Latn, 250,478 speakers), Bafut (Latn, 158,146 speakers), Fur (Latn, 1,230,163 speakers), Bete-Bendi (Latn, 100,000 speakers), Aghem (Latn, 38,843 speakers), Ngbaka (Latn, 1,020,000 speakers), Ejagham (Latn, 120,000 speakers), South Central Banda (Latn, 244,000 speakers), Mfumte (Latn, 79,000 speakers), Mango (Latn, 77,000 speakers), Zapotec (Latn, 490,000 speakers), Nateni (Latn, 100,000 speakers), Kom (Latn, 360,685 speakers), Cicipu (Latn, 44,000 speakers), Ma’di (Latn, 584,000 speakers), Sar (Latn, 500,000 speakers), Navajo (Latn, 166,319 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Ekpeye (Latn, 226,000 speakers), Ebira (Latn, 2,200,000 speakers), Makaa (Latn, 221,000 speakers), Koonzime (Latn, 40,000 speakers), Nzakara (Latn, 50,000 speakers), Dan (Latn, 1,099,244 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Belarusian (Cyrl, 10,064,517 speakers), Mundani (Latn, 34,000 speakers), Yala (Latn, 200,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Igbo (Latn, 27,823,640 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have on-curve points which have potentially incorrect y coordinates:</p>
<pre><code>* Eng (U+014A): X=395.0,Y=1550.0 (should be at cap-height 1548?)

* Eng (U+014A): X=1194.0,Y=1550.0 (should be at cap-height 1548?)

* uni1E4D (U+1E4D): X=663.0,Y=1550.0 (should be at cap-height 1548?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure variable fonts include an avar table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This variable font does not have an avar table.</p>
 [code: missing-avar]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.os2.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>OS/2 VendorID value 'anir' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>

<details><summary>[17] Samaano[wdth,wght].ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#"></a></summary>
    <div>







* 💥 **ERROR** <p>Failed to access: <a href="http://namecheck.fontdata.com">http://namecheck.fontdata.com</a>.
This check relies on the external service <a href="http://namecheck.fontdata.com">http://namecheck.fontdata.com</a> via the internet. While the service cannot be reached or does not respond this check is broken.</p>
<pre><code>	You can exclude this check with the command line option:
	-x com.google.fonts/check/fontdata_namecheck

	Or you can wait until the service is available again.
	If the problem persists please report this issue at: https://github.com/fonttools/fontbakery/issues

	Original error message:
	&lt;class 'requests.exceptions.ReadTimeout'&gt;
</code></pre>
 [code: namecheck-service]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.metrics.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 978, but got 958 instead</p>
 [code: descent]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">nl_Latn (Dutch)</td>
<td align="left">Shaper didn't attach acutecomb to j</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 441 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



* ⚠️ **WARN** <p>Font is monospaced but 1 glyphs (0.14%) have a different width. You should check the widths of: ['ldot']</p>
 [code: mono-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check glyphs in mark glyph class are non-spacing. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following spacing glyphs may be in the GDEF mark glyph class by mistake:
acutecomb (U+0301), dotbelowcomb (U+0323), glyph094D (unencoded), gravecomb (U+0300), tildecomb (U+0303), uni0304 (U+0304), uni0306 (U+0306), uni0307 (U+0307), uni0308 (U+0308), uni030A (U+030A), uni030B (U+030B), uni030C (U+030C), uni0326 (U+0326), uni0327 (U+0327), uni0328 (U+0328), uni0331 (U+0331), uni0930_uni094D.blwf (unencoded), uni0930_uni094D.rphf (unencoded), uni093A (U+093A), uni093C (U+093C), uni0945 (U+0945), uni0946 (U+0946), uni0947 (U+0947), uni0948 (U+0948), uni0955 (U+0955), uni0956 (U+0956), uni0957 (U+0957), uni0962 (U+0962) and uni0963 (U+0963)</p>
 [code: spacing-mark-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
hookabovecomb (U+0309) and uni0305 (U+0305)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>









* ⚠️ **WARN** <p>dcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>Lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>tcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Detect any interpolation issues in the font. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Interpolation issues were found in the font:</p>
<pre><code>- Contour order differs in glyph 'uni0929_uni094D.haln': [0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=100, [4, 6, 0, 1, 2, 3, 5] in wght=700,wdth=200.

- Contour order differs in glyph 'uni092D_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] in wght=700,wdth=100, [8, 9, 0, 1, 2, 3, 4, 5, 6, 7] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0932_uni094D.haln': [0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=100, [5, 6, 0, 1, 2, 3, 4] in wght=700,wdth=200.

- Contour order differs in glyph 'uni095A_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7] in wght=700,wdth=100, [6, 7, 0, 1, 2, 3, 4, 5] in wght=700,wdth=200.

- Contour order differs in glyph 'uni091A_uni094D.haln': [0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=100, [5, 6, 0, 1, 2, 3, 4] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0926_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7] in wght=700,wdth=100, [6, 7, 0, 1, 2, 3, 4, 5] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0940_uni0902.abvs': [0, 1, 2, 3, 4] in wght=700,wdth=100, [4, 0, 1, 2, 3] in wght=700,wdth=200.

- Contour order differs in glyph 'uni094C_uni0902.abvs': [0, 1, 2, 3, 4] in wght=700,wdth=100, [4, 0, 1, 2, 3] in wght=700,wdth=200.

- Contour order differs in glyph 'uni091B_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] in wght=700,wdth=100, [9, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8] in wght=700,wdth=200.

- Contour order differs in glyph 'uni091C_uni094D_uni091E_uni094D': [0, 1, 2, 3, 4, 5, 6, 7] in wght=700,wdth=100, [6, 7, 0, 1, 2, 3, 4, 5] in wght=700,wdth=200.

- Contour 0 start point differs in glyph 'hbar' between location wght=700,wdth=100 and location wght=700,wdth=200

- Contour 1 start point differs in glyph 'hbar' between location wght=700,wdth=100 and location wght=700,wdth=200

- Contour 2 start point differs in glyph 'hbar' between location wght=700,wdth=100 and location wght=700,wdth=200

- Contour 3 start point differs in glyph 'hbar' between location wght=700,wdth=100 and location wght=700,wdth=200

- Contour order differs in glyph 'uni092F_uni094D.haln': [0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=100, [5, 6, 0, 1, 2, 3, 4] in wght=700,wdth=200.

- Contour order differs in glyph 'uni091C_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7] in wght=700,wdth=100, [6, 7, 0, 1, 2, 3, 4, 5] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0934_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7, 8] in wght=700,wdth=100, [6, 8, 0, 1, 2, 3, 4, 5, 7] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0915_uni094D_uni0937_uni094D': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] in wght=700,wdth=100, [9, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8] in wght=700,wdth=200.

- Contour order differs in glyph 'uni092A_uni094D.haln': [0, 1, 2, 3, 4, 5] in wght=700,wdth=100, [4, 5, 0, 1, 2, 3] in wght=700,wdth=200.

- Contour 0 start point differs in glyph 'Hbar' between location wght=700,wdth=100 and location wght=700,wdth=200

- Contour 1 start point differs in glyph 'Hbar' between location wght=700,wdth=100 and location wght=700,wdth=200

- Contour 2 start point differs in glyph 'Hbar' between location wght=700,wdth=100 and location wght=700,wdth=200

- Contour 3 start point differs in glyph 'Hbar' between location wght=700,wdth=100 and location wght=700,wdth=200

- Contour order differs in glyph 'uni095C_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] in wght=700,wdth=100, [8, 10, 0, 1, 2, 3, 4, 5, 6, 7, 9] in wght=700,wdth=200.

- Contour order differs in glyph 'uni091F_uni094D.haln': [0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=100, [5, 6, 0, 1, 2, 3, 4] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0933_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7] in wght=700,wdth=100, [6, 7, 0, 1, 2, 3, 4, 5] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0946_uni0902.abvs': [0, 1, 2, 3, 4] in wght=700,wdth=100, [4, 0, 1, 2, 3] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0927_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7, 8] in wght=700,wdth=100, [7, 8, 0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0931_uni094D.haln': [0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=100, [4, 6, 0, 1, 2, 3, 5] in wght=700,wdth=200.

- Contour order differs in glyph 'uni092E_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7] in wght=700,wdth=100, [6, 7, 0, 1, 2, 3, 4, 5] in wght=700,wdth=200.

- Contour order differs in glyph 'uni095B_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7, 8] in wght=700,wdth=100, [7, 8, 0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0940_uni0930_uni094D.abvs': [0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=100, [3, 4, 5, 6, 0, 1, 2] in wght=700,wdth=200.

- Contour order differs in glyph 'uni095E_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7] in wght=700,wdth=100, [6, 7, 0, 1, 2, 3, 4, 5] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0920_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7] in wght=700,wdth=100, [6, 7, 0, 1, 2, 3, 4, 5] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0949_uni0930_uni094D.abvs': [0, 1, 2, 3, 4, 5, 6, 7] in wght=700,wdth=100, [3, 4, 5, 6, 7, 0, 1, 2] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0921_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] in wght=700,wdth=100, [8, 9, 0, 1, 2, 3, 4, 5, 6, 7] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0936_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7, 8] in wght=700,wdth=100, [7, 8, 0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=200.

- Contour order differs in glyph 'uni094A_uni0930_uni094D.abvs': [0, 1, 2, 3, 4, 5, 6, 7] in wght=700,wdth=100, [3, 4, 5, 6, 7, 0, 1, 2] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0916_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] in wght=700,wdth=100, [8, 9, 0, 1, 2, 3, 4, 5, 6, 7] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0918_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7] in wght=700,wdth=100, [6, 7, 0, 1, 2, 3, 4, 5] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0930_uni094D.haln': [0, 1, 2, 3, 4, 5] in wght=700,wdth=100, [4, 5, 0, 1, 2, 3] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0949_uni0902.abvs': [0, 1, 2, 3, 4, 5] in wght=700,wdth=100, [5, 0, 1, 2, 3, 4] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0938_uni094D.haln': [0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=100, [5, 6, 0, 1, 2, 3, 4] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0939_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] in wght=700,wdth=100, [8, 9, 0, 1, 2, 3, 4, 5, 6, 7] in wght=700,wdth=200.

- Contour order differs in glyph 'uni092C_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7] in wght=700,wdth=100, [6, 7, 0, 1, 2, 3, 4, 5] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0919_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] in wght=700,wdth=100, [9, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0947_uni0902.abvs': [0, 1, 2] in wght=700,wdth=100, [2, 0, 1] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0923_uni094D.haln': [0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=100, [5, 6, 0, 1, 2, 3, 4] in wght=700,wdth=200.

- Contour order differs in glyph 'uni091D_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] in wght=700,wdth=100, [9, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8] in wght=700,wdth=200.

- Contour order differs in glyph 'uni095D_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] in wght=700,wdth=100, [7, 9, 0, 1, 2, 3, 4, 5, 6, 8] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0946_uni0930_uni094D.abvs': [0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=100, [3, 4, 5, 6, 0, 1, 2] in wght=700,wdth=200.

- Contour order differs in glyph 'uni094B_uni0902.abvs': [0, 1, 2, 3] in wght=700,wdth=100, [3, 0, 1, 2] in wght=700,wdth=200.

- Contour order differs in glyph 'uni094C_uni0930_uni094D.abvs': [0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=100, [3, 4, 5, 6, 0, 1, 2] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0945_uni0930_uni094D.abvs': [0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=100, [3, 4, 5, 6, 0, 1, 2] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0924_uni094D.haln': [0, 1, 2, 3, 4, 5] in wght=700,wdth=100, [4, 5, 0, 1, 2, 3] in wght=700,wdth=200.

- Contour order differs in glyph 'uni091E_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7] in wght=700,wdth=100, [6, 7, 0, 1, 2, 3, 4, 5] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0947_uni0930_uni094D.abvs': [0, 1, 2, 3, 4] in wght=700,wdth=100, [3, 4, 0, 1, 2] in wght=700,wdth=200.

- Contour order differs in glyph 'uni092B_uni094D.haln': [0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=100, [5, 6, 0, 1, 2, 3, 4] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0945_uni0902.abvs': [0, 1, 2, 3, 4] in wght=700,wdth=100, [4, 0, 1, 2, 3] in wght=700,wdth=200.

- Contour 0 start point differs in glyph 'endash' between location wght=700,wdth=100 and location wght=700,wdth=200

- Contour order differs in glyph 'uni0917_uni094D.haln': [0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=100, [5, 6, 0, 1, 2, 3, 4] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0959_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] in wght=700,wdth=100, [8, 10, 0, 1, 2, 3, 4, 5, 6, 7, 9] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0928_uni094D.haln': [0, 1, 2, 3, 4, 5] in wght=700,wdth=100, [4, 5, 0, 1, 2, 3] in wght=700,wdth=200.

- Contour order differs in glyph 'uni094A_uni0902.abvs': [0, 1, 2, 3, 4, 5] in wght=700,wdth=100, [5, 0, 1, 2, 3, 4] in wght=700,wdth=200.

- Contour order differs in glyph 'uni094B_uni0930_uni094D.abvs': [0, 1, 2, 3, 4, 5] in wght=700,wdth=100, [3, 4, 5, 0, 1, 2] in wght=700,wdth=200.

- Contour order differs in glyph 'uni093E_uni0930_uni094D.abvs': [0, 1, 2, 3, 4] in wght=700,wdth=100, [3, 4, 0, 1, 2] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0958_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] in wght=700,wdth=100, [7, 9, 0, 1, 2, 3, 4, 5, 6, 8] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0937_uni094D.haln': [0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=100, [5, 6, 0, 1, 2, 3, 4] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0925_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7, 8] in wght=700,wdth=100, [7, 8, 0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0948_uni0902.abvs': [0, 1, 2, 3] in wght=700,wdth=100, [3, 0, 1, 2] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0935_uni094D.haln': [0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=100, [5, 6, 0, 1, 2, 3, 4] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0915_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7, 8] in wght=700,wdth=100, [7, 8, 0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0922_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7, 8] in wght=700,wdth=100, [7, 8, 0, 1, 2, 3, 4, 5, 6] in wght=700,wdth=200.

- Contour order differs in glyph 'uni0948_uni0930_uni094D.abvs': [0, 1, 2, 3, 4, 5] in wght=700,wdth=100, [3, 4, 5, 0, 1, 2] in wght=700,wdth=200.

- Contour order differs in glyph 'uni095F_uni094D.haln': [0, 1, 2, 3, 4, 5, 6, 7] in wght=700,wdth=100, [5, 7, 0, 1, 2, 3, 4, 6] in wght=700,wdth=200.
</code></pre>
 [code: interpolation-issues]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- glyph094D

- uni0930_uni094D.abvs

- uni0930_uni094D.vatu
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, cherokee, tifinagh, coptic</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: coptic, math, gothic, elbasan, glagolitic</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: malayalam, coptic, todhri, canadian-aboriginal, duployan, math, hebrew, tifinagh, syriac, tai-le, old-permic</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: cherokee, caucasian-albanian, thai, gothic, tifinagh, syriac, sunuwar</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>devanagari</code>, <code>latin</code>, <code>latin-ext</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̅ i̇ ỉ ǐ ị̅ ị̇ ị̉ ị̊ ị̋ ị̌ i̦̅ i̦̇ ỉ̦ i̦̊ i̦̋ ǐ̦ i̧̅ i̧̇ ỉ̧ i̧̊</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Basaa (Latn, 332,940 speakers), Lugbara (Latn, 2,200,000 speakers), Dii (Latn, 71,000 speakers), Avokaya (Latn, 100,000 speakers), Southern Kisi (Latn, 360,000 speakers), Dutch (Latn, 31,709,104 speakers), Vute (Latn, 21,000 speakers), Gulay (Latn, 250,478 speakers), Bafut (Latn, 158,146 speakers), Fur (Latn, 1,230,163 speakers), Bete-Bendi (Latn, 100,000 speakers), Aghem (Latn, 38,843 speakers), Ngbaka (Latn, 1,020,000 speakers), Ejagham (Latn, 120,000 speakers), South Central Banda (Latn, 244,000 speakers), Mfumte (Latn, 79,000 speakers), Mango (Latn, 77,000 speakers), Zapotec (Latn, 490,000 speakers), Nateni (Latn, 100,000 speakers), Kom (Latn, 360,685 speakers), Cicipu (Latn, 44,000 speakers), Ma’di (Latn, 584,000 speakers), Sar (Latn, 500,000 speakers), Navajo (Latn, 166,319 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Ekpeye (Latn, 226,000 speakers), Ebira (Latn, 2,200,000 speakers), Makaa (Latn, 221,000 speakers), Koonzime (Latn, 40,000 speakers), Nzakara (Latn, 50,000 speakers), Dan (Latn, 1,099,244 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Belarusian (Cyrl, 10,064,517 speakers), Mundani (Latn, 34,000 speakers), Yala (Latn, 200,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Igbo (Latn, 27,823,640 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have on-curve points which have potentially incorrect y coordinates:</p>
<pre><code>* Eng (U+014A): X=112.0,Y=1550.0 (should be at cap-height 1548?)

* Eng (U+014A): X=911.0,Y=1550.0 (should be at cap-height 1548?)

* uni0162 (U+0162): X=862.0,Y=-617.0 (should be at descender -615?)

* uni0162 (U+0162): X=710.0,Y=-617.0 (should be at descender -615?)

* uni01C4 (U+01C4): X=213.0,Y=1550.0 (should be at cap-height 1548?)

* uni01C4 (U+01C4): X=213.0,Y=1549.0 (should be at cap-height 1548?)

* uni01C4 (U+01C4): X=132.0,Y=1549.0 (should be at cap-height 1548?)

* uni01C5 (U+01C5): X=214.0,Y=1550.0 (should be at cap-height 1548?)

* uni01C5 (U+01C5): X=214.0,Y=1549.0 (should be at cap-height 1548?)

* uni01C5 (U+01C5): X=133.0,Y=1549.0 (should be at cap-height 1548?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* Hbar (U+0126) has a counter-clockwise outer contour

* Hbar (U+0126) has a counter-clockwise outer contour

* Hbar (U+0126) has a counter-clockwise outer contour

* Hbar (U+0126) has a counter-clockwise outer contour

* endash (U+2013) has a counter-clockwise outer contour

* hbar (U+0127) has a counter-clockwise outer contour

* hbar (U+0127) has a counter-clockwise outer contour

* hbar (U+0127) has a counter-clockwise outer contour

* hbar (U+0127) has a counter-clockwise outer contour
</code></pre>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure variable fonts include an avar table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This variable font does not have an avar table.</p>
 [code: missing-avar]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.os2.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>OS/2 VendorID value 'anir' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>

<details><summary>[1] Family checks</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure VFs have 'ital' STAT axis. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.stat.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Font Samaano[wdth,wght].ttf is missing an 'ital' axis.</p>
 [code: missing-ital-axis]



* 🔥 **FAIL** <p>Font Samaano-Italic[wdth,wght].ttf is missing an 'ital' axis.</p>
 [code: missing-ital-axis]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 1 | 0 | 7 | 27 | 185 | 15 | 249 | 0 | 
| 0% | 0% | 1% | 6% | 38% | 3% | 51% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
