## FontBakery report

fontbakery version: 0.12.10





## Check results



<details><summary>[13] Samaano[slnt,wdth,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Validate STAT particle names and values match the fallback names in GFAxisRegistry. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.axisregistry.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>On the font variation axis 'slnt', the name 'Oblique' is not among the expected ones (Default) according to the Google Fonts Axis Registry.</p>
 [code: invalid-name]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 863 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
uni0945 (U+0945), uni0946 (U+0946), uni0947 (U+0947), uni0948 (U+0948) and uni0955 (U+0955)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>









* ⚠️ **WARN** <p>Lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>dcaron is decomposed and therefore could not be checked. Please check manually.</p>
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
<pre><code>- Contour 3 in glyph 'Dcroat': becomes underweight between wght=100,wdth=100,slnt=0 and wght=700,wdth=200,slnt=-20.

- Contour 7 in glyph 'uni20BF': becomes underweight between wght=100,wdth=100,slnt=0 and wght=700,wdth=200,slnt=-20.

- Contour 3 in glyph 'Eth': becomes underweight between wght=100,wdth=100,slnt=0 and wght=700,wdth=200,slnt=-20.
</code></pre>
 [code: interpolation-issues]



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
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, cherokee, math, tifinagh</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: gothic, elbasan, glagolitic, coptic, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: hebrew, old-permic, duployan, malayalam, tai-le, coptic, tifinagh, syriac, todhri, canadian-aboriginal, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+030F COMBINING DOUBLE GRAVE ACCENT: not included in any glyphset definition</li>
<li>U+0311 COMBINING INVERTED BREVE: try adding one of: coptic, todhri</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, cherokee, duployan</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: cherokee, thai, tifinagh, syriac, caucasian-albanian, gothic, sunuwar</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2052 COMMERCIAL MINUS SIGN: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2071 SUPERSCRIPT LATIN SMALL LETTER I: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207A SUPERSCRIPT PLUS SIGN: try adding math</li>
<li>U+207B SUPERSCRIPT MINUS: try adding math</li>
<li>U+207C SUPERSCRIPT EQUALS SIGN: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208A SUBSCRIPT PLUS SIGN: try adding math</li>
<li>U+208B SUBSCRIPT MINUS: try adding math</li>
<li>U+208C SUBSCRIPT EQUALS SIGN: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2116 NUMERO SIGN: try adding cyrillic</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+E0FC : not included in any glyphset definition</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>devanagari</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̅ i̇ ǐ i̒ i̛̅ i̛̇ i̛̊ i̛̋ ǐ̛ i̛̒ i̤̅ i̤̇ i̤̊ i̤̋ ǐ̤ i̤̒ i̦̅ i̦̇ i̦̊ i̦̋</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Lithuanian (Latn, 2,357,094 speakers), Dutch (Latn, 31,709,104 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Koonzime (Latn, 40,000 speakers), Belarusian (Cyrl, 10,064,517 speakers), Igbo (Latn, 27,823,640 speakers), Zapotec (Latn, 490,000 speakers), Ma’di (Latn, 584,000 speakers), Dan (Latn, 1,099,244 speakers), Southern Kisi (Latn, 360,000 speakers), Ngbaka (Latn, 1,020,000 speakers), Yala (Latn, 200,000 speakers), Nateni (Latn, 100,000 speakers), Makaa (Latn, 221,000 speakers), Sar (Latn, 500,000 speakers), Lugbara (Latn, 2,200,000 speakers), Mfumte (Latn, 79,000 speakers), Ekpeye (Latn, 226,000 speakers), Aghem (Latn, 38,843 speakers), Ebira (Latn, 2,200,000 speakers), Basaa (Latn, 332,940 speakers), Mundani (Latn, 34,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Navajo (Latn, 166,319 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Nzakara (Latn, 50,000 speakers), Ejagham (Latn, 120,000 speakers), South Central Banda (Latn, 244,000 speakers), Bafut (Latn, 158,146 speakers), Kom (Latn, 360,685 speakers), Dii (Latn, 71,000 speakers), Cicipu (Latn, 44,000 speakers), Avokaya (Latn, 100,000 speakers), Mango (Latn, 77,000 speakers), Vute (Latn, 21,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Gulay (Latn, 250,478 speakers), Bete-Bendi (Latn, 100,000 speakers), Fur (Latn, 1,230,163 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have on-curve points which have potentially incorrect y coordinates:</p>
<pre><code>* peseta (U+20A7): X=596.0,Y=1550.0 (should be at cap-height 1548?)

* peseta (U+20A7): X=662.0,Y=1550.0 (should be at cap-height 1548?)

* peseta (U+20A7): X=662.0,Y=1.0 (should be at baseline 0?)

* peseta (U+20A7): X=596.0,Y=1.0 (should be at baseline 0?)

* peseta (U+20A7): X=728.0,Y=1.0 (should be at baseline 0?)

* peseta (U+20A7): X=599.0,Y=1.0 (should be at baseline 0?)

* uni0930_uni094D.blwf: X=-160.0,Y=-614.0 (should be at descender -615?)

* uni0930_uni094D.blwf: X=-381.0,Y=-614.0 (should be at descender -615?)

* uni2116 (U+2116): X=501.0,Y=1549.0 (should be at cap-height 1548?)

* uni2116 (U+2116): X=601.0,Y=1549.0 (should be at cap-height 1548?)

* uni2116 (U+2116): X=810.0,Y=1549.0 (should be at cap-height 1548?)

* uni2116 (U+2116): X=910.0,Y=1549.0 (should be at cap-height 1548?)

* uni2116 (U+2116): X=532.0,Y=1549.0 (should be at cap-height 1548?)

* uni2116 (U+2116): X=882.0,Y=1549.0 (should be at cap-height 1548?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font lacks caret positioning values for these ligature glyphs:
- i_uni030A
- i_uni030B
- j_gravecomb
- j_uni0303
- j_uni0304
- j_uni0308
- j_uni0311
- jacute
- uni012F_uni0300
- uni012F_uni0301
- uni012F_uni0302
- uni012F_uni0303
- uni012F_uni0304
- uni012F_uni030C
- uni1ECB_uni0300
- uni1ECB_uni0301
- uni1ECB_uni0302
- uni1ECB_uni0303
- uni1ECB_uni0304</p>
 [code: incomplete-caret-pos-data]



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




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 12 | 91 | 8 | 139 | 0 | 
| 0% | 0% | 0% | 5% | 36% | 3% | 55% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
