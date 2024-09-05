## FontBakery report

fontbakery version: 0.12.10



## Experimental checks

These won't break the CI job for now, but will become effective after some time if nobody raises any concern.


<details><summary>[1] Samaano[wdth,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking that the typoAscender exceeds the yMax of the /Agrave. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.metrics.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.sTypoAscender value should be greater than 1947, but got 1638 instead</p>
 [code: typoAscender]



</div>
</details>
</div>
</details>




## All other checks



<details><summary>[22] Samaano[wdth,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking font version fields (head and name table). <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.head.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>head version is &quot;0.00200&quot; while name version string (for platform 3, encoding 1) is &quot;Version 0.001&quot;.</p>
 [code: mismatch]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>On non-monospaced fonts, the OS/2.panose.bProportion value can be set to any value except 9 (proportion: monospaced) which is the bad value we got in this font.</p>
 [code: bad-panose]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+010E: LATIN CAPITAL LETTER D WITH CARON</td>
<td align="left">U+010F: LATIN SMALL LETTER D WITH CARON</td>
</tr>
<tr>
<td align="left">U+0122: LATIN CAPITAL LETTER G WITH CEDILLA</td>
<td align="left">U+0123: LATIN SMALL LETTER G WITH CEDILLA</td>
</tr>
<tr>
<td align="left">U+0164: LATIN CAPITAL LETTER T WITH CARON</td>
<td align="left">U+0165: LATIN SMALL LETTER T WITH CARON</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.metrics.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.usWinAscent value should be equal or greater than 2476, but got 1800 instead</p>
 [code: ascent]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Name table records must not have trailing spaces. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Name table record with key = (3, 1, 1033, 10) has trailing spaces that must be removed: 'A Monspace[...]ents only '</p>
 [code: trailing-space]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure indic fonts have the Indian Rupee Sign glyph. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Please add a glyph for Indian Rupee Sign (₹) at codepoint U+20B9.</p>
 [code: missing-rupee]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Font contains glyphs for whitespace characters? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Whitespace glyph missing for codepoint 0x00A0.</p>
 [code: missing-whitespace-glyph-0x00A0]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>No GF glyphset was found to be supported &gt;80%, so language shaping support couldn't get checked.</p>
 [code: no-glyphset-supported]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Copyright notices match canonical pattern in fonts <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.copyright.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Name Table entry: Copyright notices should match a pattern similar to:</p>
<p>&quot;Copyright 2020 The Familyname Project Authors (git url)&quot;</p>
<p>But instead we have got:</p>
<p>&quot;Copyright 2024, Samaano Font Authors (<a href="https://github.com/mitradranirban/samaano-fonts">https://github.com/mitradranirban/samaano-fonts</a>)&quot;</p>
 [code: bad-notice-format]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check Google Fonts glyph coverage. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Missing required codepoints:</p>
<pre><code>- 0x00A0 (NO-BREAK SPACE)


- 0x00A1 (INVERTED EXCLAMATION MARK)


- 0x00A2 (CENT SIGN)


- 0x00A3 (POUND SIGN)


- 0x00A5 (YEN SIGN)


- 0x00A7 (SECTION SIGN)


- 0x00A8 (DIAERESIS)


- 0x00A9 (COPYRIGHT SIGN)


- 0x00AA (FEMININE ORDINAL INDICATOR)


- 0x00AB (LEFT-POINTING DOUBLE ANGLE QUOTATION MARK)


- 0x00AE (REGISTERED SIGN)


- 0x00AF (MACRON)


- 0x00B0 (DEGREE SIGN)


- 0x00B4 (ACUTE ACCENT)


- 0x00B6 (PILCROW SIGN)


- 0x00B7 (MIDDLE DOT)


- 0x00B8 (CEDILLA)


- 0x00BA (MASCULINE ORDINAL INDICATOR)


- 0x00BB (RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK)


- 0x00BF (INVERTED QUESTION MARK)


- 0x00C6 (LATIN CAPITAL LETTER AE)


- 0x00D0 (LATIN CAPITAL LETTER ETH)


- 0x00D7 (MULTIPLICATION SIGN)


- 0x00D8 (LATIN CAPITAL LETTER O WITH STROKE)


- 0x00DE (LATIN CAPITAL LETTER THORN)


- 0x00DF (LATIN SMALL LETTER SHARP S)


- 0x00E6 (LATIN SMALL LETTER AE)


- 0x00F0 (LATIN SMALL LETTER ETH)


- 0x00F7 (DIVISION SIGN)


- 0x00F8 (LATIN SMALL LETTER O WITH STROKE)


- 0x00FE (LATIN SMALL LETTER THORN)


- 0x010F (LATIN SMALL LETTER D WITH CARON)


- 0x0110 (LATIN CAPITAL LETTER D WITH STROKE)


- 0x0111 (LATIN SMALL LETTER D WITH STROKE)


- 0x0123 (LATIN SMALL LETTER G WITH CEDILLA)


- 0x0126 (LATIN CAPITAL LETTER H WITH STROKE)


- 0x0127 (LATIN SMALL LETTER H WITH STROKE)


- 0x013D (LATIN CAPITAL LETTER L WITH CARON)


- 0x013E (LATIN SMALL LETTER L WITH CARON)


- 0x0141 (LATIN CAPITAL LETTER L WITH STROKE)


- 0x0142 (LATIN SMALL LETTER L WITH STROKE)


- 0x0152 (LATIN CAPITAL LIGATURE OE)


- 0x0153 (LATIN SMALL LIGATURE OE)


- 0x0165 (LATIN SMALL LETTER T WITH CARON)


- 0x0218 (LATIN CAPITAL LETTER S WITH COMMA BELOW)


- 0x0219 (LATIN SMALL LETTER S WITH COMMA BELOW)


- 0x021A (LATIN CAPITAL LETTER T WITH COMMA BELOW)


- 0x021B (LATIN SMALL LETTER T WITH COMMA BELOW)


- 0x02C6 (MODIFIER LETTER CIRCUMFLEX ACCENT)


- 0x02C7 (CARON)


- 0x02D8 (BREVE)


- 0x02D9 (DOT ABOVE)


- 0x02DA (RING ABOVE)


- 0x02DB (OGONEK)


- 0x02DC (SMALL TILDE)


- 0x02DD (DOUBLE ACUTE ACCENT)


- 0x1E80 (LATIN CAPITAL LETTER W WITH GRAVE)


- 0x1E81 (LATIN SMALL LETTER W WITH GRAVE)


- 0x1E82 (LATIN CAPITAL LETTER W WITH ACUTE)


- 0x1E83 (LATIN SMALL LETTER W WITH ACUTE)


- 0x1E84 (LATIN CAPITAL LETTER W WITH DIAERESIS)


- 0x1E85 (LATIN SMALL LETTER W WITH DIAERESIS)


- 0x1E9E (LATIN CAPITAL LETTER SHARP S)


- 0x1EF2 (LATIN CAPITAL LETTER Y WITH GRAVE)


- 0x1EF3 (LATIN SMALL LETTER Y WITH GRAVE)


- 0x2013 (EN DASH)


- 0x2014 (EM DASH)


- 0x2018 (LEFT SINGLE QUOTATION MARK)


- 0x2019 (RIGHT SINGLE QUOTATION MARK)


- 0x201A (SINGLE LOW-9 QUOTATION MARK)


- 0x201C (LEFT DOUBLE QUOTATION MARK)


- 0x201D (RIGHT DOUBLE QUOTATION MARK)


- 0x201E (DOUBLE LOW-9 QUOTATION MARK)


- 0x2022 (BULLET)


- 0x2026 (HORIZONTAL ELLIPSIS)


- 0x2039 (SINGLE LEFT-POINTING ANGLE QUOTATION MARK)


- 0x203A (SINGLE RIGHT-POINTING ANGLE QUOTATION MARK)


- 0x20AC (EURO SIGN)


- 0x2122 (TRADE MARK SIGN)


- 0x2212 (MINUS SIGN)
</code></pre>
 [code: missing-codepoints]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Version format is correct in 'name' table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The NameID.VERSION_STRING (nameID=5) value must follow the pattern &quot;Version X.Y&quot; with X.Y greater than or equal to 1.000. Current version string is: &quot;Version 0.001&quot;</p>
 [code: bad-version-strings]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check font follows the Google Fonts vertical metric schema <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.vmetrics.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 2048 when it should be at least 2457</p>
 [code: bad-hhea-range]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check glyphs in mark glyph class are non-spacing. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following spacing glyphs may be in the GDEF mark glyph class by mistake:
acutecomb (U+0301), gravecomb (U+0300), tildecomb (U+0303), uni0302 (U+0302), uni0304 (U+0304), uni0306 (U+0306), uni0307 (U+0307), uni0308 (U+0308), uni030A (U+030A), uni030B (U+030B), uni030C (U+030C), uni0326 (U+0326), uni0327 (U+0327), uni0328 (U+0328), uni0900 (U+0900), uni0901 (U+0901) and uni0902 (U+0902)</p>
 [code: spacing-mark-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gpos.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning information.</p>
 [code: lacks-kern-info]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Detect any interpolation issues in the font. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Interpolation issues were found in the font:</p>
<pre><code>- Contour order differs in glyph 'uni090E': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] in wght=100,wdth=200, [3, 4, 5, 6, 7, 8, 9, 0, 1, 2] in wght=900,wdth=100.

- Contour order differs in glyph 'uni090D': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] in wght=100,wdth=200, [3, 4, 5, 6, 7, 8, 9, 0, 1, 2] in wght=900,wdth=100.
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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, cherokee, tifinagh, coptic</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: malayalam, canadian-aboriginal, coptic, math, old-permic, syriac, tifinagh, tai-le</li>
<li>U+030A COMBINING RING ABOVE: try adding syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0326 COMBINING COMMA BELOW: not included in any glyphset definition</li>
<li>U+0327 COMBINING CEDILLA: not included in any glyphset definition</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0900 DEVANAGARI SIGN INVERTED CANDRABINDU: try adding devanagari</li>
<li>U+0901 DEVANAGARI SIGN CANDRABINDU: try adding devanagari</li>
<li>U+0902 DEVANAGARI SIGN ANUSVARA: try adding devanagari</li>
<li>U+0903 DEVANAGARI SIGN VISARGA: try adding devanagari</li>
<li>U+0904 DEVANAGARI LETTER SHORT A: try adding devanagari</li>
<li>U+0905 DEVANAGARI LETTER A: try adding devanagari</li>
<li>U+0906 DEVANAGARI LETTER AA: try adding devanagari</li>
<li>U+0907 DEVANAGARI LETTER I: try adding devanagari</li>
<li>U+0908 DEVANAGARI LETTER II: try adding devanagari</li>
<li>U+0909 DEVANAGARI LETTER U: try adding devanagari</li>
<li>U+090A DEVANAGARI LETTER UU: try adding devanagari</li>
<li>U+090B DEVANAGARI LETTER VOCALIC R: try adding devanagari</li>
<li>U+090C DEVANAGARI LETTER VOCALIC L: try adding devanagari</li>
<li>U+090D DEVANAGARI LETTER CANDRA E: try adding devanagari</li>
<li>U+090E DEVANAGARI LETTER SHORT E: try adding devanagari</li>
<li>U+090F DEVANAGARI LETTER E: try adding devanagari</li>
<li>U+0910 DEVANAGARI LETTER AI: try adding devanagari</li>
<li>U+0911 DEVANAGARI LETTER CANDRA O: try adding devanagari</li>
<li>U+0912 DEVANAGARI LETTER SHORT O: try adding devanagari</li>
<li>U+0913 DEVANAGARI LETTER O: try adding devanagari</li>
<li>U+0914 DEVANAGARI LETTER AU: try adding devanagari</li>
<li>U+0915 DEVANAGARI LETTER KA: try adding devanagari</li>
<li>U+0916 DEVANAGARI LETTER KHA: try adding devanagari</li>
<li>U+0917 DEVANAGARI LETTER GA: try adding devanagari</li>
<li>U+0918 DEVANAGARI LETTER GHA: try adding devanagari</li>
<li>U+0919 DEVANAGARI LETTER NGA: try adding devanagari</li>
<li>U+091A DEVANAGARI LETTER CA: try adding devanagari</li>
<li>U+091B DEVANAGARI LETTER CHA: try adding devanagari</li>
<li>U+091C DEVANAGARI LETTER JA: try adding devanagari</li>
<li>U+091D DEVANAGARI LETTER JHA: try adding devanagari</li>
<li>U+091E DEVANAGARI LETTER NYA: try adding devanagari</li>
<li>U+091F DEVANAGARI LETTER TTA: try adding devanagari</li>
<li>U+0920 DEVANAGARI LETTER TTHA: try adding devanagari</li>
<li>U+0921 DEVANAGARI LETTER DDA: try adding devanagari</li>
<li>U+0922 DEVANAGARI LETTER DDHA: try adding devanagari</li>
<li>U+0923 DEVANAGARI LETTER NNA: try adding devanagari</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>latin</code>, <code>latin-ext</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̇ ǐ i̦̇ i̦̊ i̦̋ ǐ̦ i̧̇ i̧̊ i̧̋ ǐ̧ j̆ j̇ j̊ j̋ ǰ j̦̀ j̦́ j̦̃ j̦̄ j̦̆</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Lithuanian (Latn, 2,357,094 speakers), Dutch (Latn, 31,709,104 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Koonzime (Latn, 40,000 speakers), Bafut (Latn, 158,146 speakers), Zapotec (Latn, 490,000 speakers), Cicipu (Latn, 44,000 speakers), Basaa (Latn, 332,940 speakers), Navajo (Latn, 166,319 speakers), Gulay (Latn, 250,478 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Ma’di (Latn, 584,000 speakers), Vute (Latn, 21,000 speakers), Southern Kisi (Latn, 360,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Nateni (Latn, 100,000 speakers), Fur (Latn, 1,230,163 speakers), Ngbaka (Latn, 1,020,000 speakers), Ejagham (Latn, 120,000 speakers), Yala (Latn, 200,000 speakers), Ekpeye (Latn, 226,000 speakers), Sar (Latn, 500,000 speakers), Lugbara (Latn, 2,200,000 speakers), Mundani (Latn, 34,000 speakers), Dan (Latn, 1,099,244 speakers), Nzakara (Latn, 50,000 speakers), Igbo (Latn, 27,823,640 speakers), Dii (Latn, 71,000 speakers), Makaa (Latn, 221,000 speakers), Mfumte (Latn, 79,000 speakers), Kom (Latn, 360,685 speakers), South Central Banda (Latn, 244,000 speakers), Belarusian (Cyrl, 10,064,517 speakers), Mango (Latn, 77,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Ebira (Latn, 2,200,000 speakers), Aghem (Latn, 38,843 speakers), Avokaya (Latn, 100,000 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* .notdef has a counter-clockwise outer contour

* Abreve (U+0102) has a counter-clockwise outer contour

* Abreve (U+0102) has a counter-clockwise outer contour

* Abreve (U+0102) has a counter-clockwise outer contour

* Adieresis (U+00C4) has a counter-clockwise outer contour

* Adieresis (U+00C4) has a counter-clockwise outer contour

* Amacron (U+0100) has a counter-clockwise outer contour

* Aogonek (U+0104) has a counter-clockwise outer contour

* Aogonek (U+0104) has a counter-clockwise outer contour

* Aogonek (U+0104) has a counter-clockwise outer contour

* C (U+0043) has a counter-clockwise outer contour

* C (U+0043) has a counter-clockwise outer contour

* C (U+0043) has a counter-clockwise outer contour

* Cacute (U+0106) has a counter-clockwise outer contour

* Cacute (U+0106) has a counter-clockwise outer contour

* Cacute (U+0106) has a counter-clockwise outer contour

* Ccaron (U+010C) has a counter-clockwise outer contour

* Ccaron (U+010C) has a counter-clockwise outer contour

* Ccaron (U+010C) has a counter-clockwise outer contour

* Ccedilla (U+00C7) has a counter-clockwise outer contour

* Ccedilla (U+00C7) has a counter-clockwise outer contour

* Ccedilla (U+00C7) has a counter-clockwise outer contour

* Ccedilla (U+00C7) has a counter-clockwise outer contour

* Ccedilla (U+00C7) has a counter-clockwise outer contour

* Ccedilla (U+00C7) has a counter-clockwise outer contour

* Ccedilla (U+00C7) has a counter-clockwise outer contour

* Ccircumflex (U+0108) has a counter-clockwise outer contour

* Ccircumflex (U+0108) has a counter-clockwise outer contour

* Ccircumflex (U+0108) has a counter-clockwise outer contour

* Cdotaccent (U+010A) has a counter-clockwise outer contour

* Cdotaccent (U+010A) has a counter-clockwise outer contour

* Cdotaccent (U+010A) has a counter-clockwise outer contour

* Cdotaccent (U+010A) has a counter-clockwise outer contour

* Ebreve (U+0114) has a counter-clockwise outer contour

* Ebreve (U+0114) has a counter-clockwise outer contour

* Ebreve (U+0114) has a counter-clockwise outer contour

* Edieresis (U+00CB) has a counter-clockwise outer contour

* Edieresis (U+00CB) has a counter-clockwise outer contour

* Edotaccent (U+0116) has a counter-clockwise outer contour

* Emacron (U+0112) has a counter-clockwise outer contour

* Eogonek (U+0118) has a counter-clockwise outer contour

* Eogonek (U+0118) has a counter-clockwise outer contour

* Eogonek (U+0118) has a counter-clockwise outer contour

* Gbreve (U+011E) has a counter-clockwise outer contour

* Gbreve (U+011E) has a counter-clockwise outer contour

* Gbreve (U+011E) has a counter-clockwise outer contour

* Gdotaccent (U+0120) has a counter-clockwise outer contour

* Ibreve (U+012C) has a counter-clockwise outer contour

* Ibreve (U+012C) has a counter-clockwise outer contour

* Ibreve (U+012C) has a counter-clockwise outer contour

* Idieresis (U+00CF) has a counter-clockwise outer contour

* Idieresis (U+00CF) has a counter-clockwise outer contour

* Idotaccent (U+0130) has a counter-clockwise outer contour

* Imacron (U+012A) has a counter-clockwise outer contour

* Iogonek (U+012E) has a counter-clockwise outer contour

* Iogonek (U+012E) has a counter-clockwise outer contour

* Iogonek (U+012E) has a counter-clockwise outer contour

* Obreve (U+014E) has a counter-clockwise outer contour

* Obreve (U+014E) has a counter-clockwise outer contour

* Obreve (U+014E) has a counter-clockwise outer contour

* Odieresis (U+00D6) has a counter-clockwise outer contour

* Odieresis (U+00D6) has a counter-clockwise outer contour

* Omacron (U+014C) has a counter-clockwise outer contour

* Scedilla (U+015E) has a counter-clockwise outer contour

* Scedilla (U+015E) has a counter-clockwise outer contour

* Scedilla (U+015E) has a counter-clockwise outer contour

* Scedilla (U+015E) has a counter-clockwise outer contour

* Ubreve (U+016C) has a counter-clockwise outer contour

* Ubreve (U+016C) has a counter-clockwise outer contour

* Ubreve (U+016C) has a counter-clockwise outer contour

* Udieresis (U+00DC) has a counter-clockwise outer contour

* Udieresis (U+00DC) has a counter-clockwise outer contour

* Umacron (U+016A) has a counter-clockwise outer contour

* Uogonek (U+0172) has a counter-clockwise outer contour

* Uogonek (U+0172) has a counter-clockwise outer contour

* Uogonek (U+0172) has a counter-clockwise outer contour

* X (U+0058) has a counter-clockwise outer contour

* Ydieresis (U+0178) has a counter-clockwise outer contour

* Ydieresis (U+0178) has a counter-clockwise outer contour

* Zdotaccent (U+017B) has a counter-clockwise outer contour

* abreve (U+0103) has a counter-clockwise outer contour

* abreve (U+0103) has a counter-clockwise outer contour

* abreve (U+0103) has a counter-clockwise outer contour

* adieresis (U+00E4) has a counter-clockwise outer contour

* adieresis (U+00E4) has a counter-clockwise outer contour

* amacron (U+0101) has a counter-clockwise outer contour

* aogonek (U+0105) has a counter-clockwise outer contour

* aogonek (U+0105) has a counter-clockwise outer contour

* aogonek (U+0105) has a counter-clockwise outer contour

* braceright (U+007D) has a counter-clockwise outer contour

* braceright (U+007D) has a counter-clockwise outer contour

* braceright (U+007D) has a counter-clockwise outer contour

* braceright (U+007D) has a counter-clockwise outer contour

* braceright (U+007D) has a counter-clockwise outer contour

* braceright (U+007D) has a counter-clockwise outer contour

* ccedilla (U+00E7) has a counter-clockwise outer contour

* ccedilla (U+00E7) has a counter-clockwise outer contour

* ccedilla (U+00E7) has a counter-clockwise outer contour

* ccedilla (U+00E7) has a counter-clockwise outer contour

* cdotaccent (U+010B) has a counter-clockwise outer contour

* ebreve (U+0115) has a counter-clockwise outer contour

* ebreve (U+0115) has a counter-clockwise outer contour

* ebreve (U+0115) has a counter-clockwise outer contour

* edieresis (U+00EB) has a counter-clockwise outer contour

* edieresis (U+00EB) has a counter-clockwise outer contour

* edotaccent (U+0117) has a counter-clockwise outer contour

* eight (U+0038) has a counter-clockwise outer contour

* eight (U+0038) has a counter-clockwise outer contour

* eight (U+0038) has a counter-clockwise outer contour

* eight (U+0038) has a counter-clockwise outer contour

* eight (U+0038) has a counter-clockwise outer contour

* eight (U+0038) has a counter-clockwise outer contour

* eight (U+0038) has a counter-clockwise outer contour

* emacron (U+0113) has a counter-clockwise outer contour

* eogonek (U+0119) has a counter-clockwise outer contour

* eogonek (U+0119) has a counter-clockwise outer contour

* eogonek (U+0119) has a counter-clockwise outer contour

* five (U+0035) has a counter-clockwise outer contour

* five (U+0035) has a counter-clockwise outer contour

* five (U+0035) has a counter-clockwise outer contour

* five (U+0035) has a counter-clockwise outer contour

* five (U+0035) has a counter-clockwise outer contour

* four (U+0034) has a counter-clockwise outer contour

* four (U+0034) has a counter-clockwise outer contour

* four (U+0034) has a counter-clockwise outer contour

* four (U+0034) has a counter-clockwise outer contour

* gbreve (U+011F) has a counter-clockwise outer contour

* gbreve (U+011F) has a counter-clockwise outer contour

* gbreve (U+011F) has a counter-clockwise outer contour

* gdotaccent (U+0121) has a counter-clockwise outer contour

* ibreve (U+012D) has a counter-clockwise outer contour

* ibreve (U+012D) has a counter-clockwise outer contour

* ibreve (U+012D) has a counter-clockwise outer contour

* idieresis (U+00EF) has a counter-clockwise outer contour

* idieresis (U+00EF) has a counter-clockwise outer contour

* imacron (U+012B) has a counter-clockwise outer contour

* iogonek (U+012F) has a counter-clockwise outer contour

* iogonek (U+012F) has a counter-clockwise outer contour

* iogonek (U+012F) has a counter-clockwise outer contour

* nine (U+0039) has a counter-clockwise outer contour

* nine (U+0039) has a counter-clockwise outer contour

* nine (U+0039) has a counter-clockwise outer contour

* nine (U+0039) has a counter-clockwise outer contour

* nine (U+0039) has a counter-clockwise outer contour

* nine (U+0039) has a counter-clockwise outer contour

* obreve (U+014F) has a counter-clockwise outer contour

* obreve (U+014F) has a counter-clockwise outer contour

* obreve (U+014F) has a counter-clockwise outer contour

* odieresis (U+00F6) has a counter-clockwise outer contour

* odieresis (U+00F6) has a counter-clockwise outer contour

* omacron (U+014D) has a counter-clockwise outer contour

* one (U+0031) has a counter-clockwise outer contour

* one (U+0031) has a counter-clockwise outer contour

* parenright (U+0029) has a counter-clockwise outer contour

* parenright (U+0029) has a counter-clockwise outer contour

* parenright (U+0029) has a counter-clockwise outer contour

* scedilla (U+015F) has a counter-clockwise outer contour

* scedilla (U+015F) has a counter-clockwise outer contour

* scedilla (U+015F) has a counter-clockwise outer contour

* scedilla (U+015F) has a counter-clockwise outer contour

* seven (U+0037) has a counter-clockwise outer contour

* seven (U+0037) has a counter-clockwise outer contour

* seven (U+0037) has a counter-clockwise outer contour

* six (U+0036) has a counter-clockwise outer contour

* six (U+0036) has a counter-clockwise outer contour

* six (U+0036) has a counter-clockwise outer contour

* six (U+0036) has a counter-clockwise outer contour

* six (U+0036) has a counter-clockwise outer contour

* six (U+0036) has a counter-clockwise outer contour

* three (U+0033) has a counter-clockwise outer contour

* three (U+0033) has a counter-clockwise outer contour

* three (U+0033) has a counter-clockwise outer contour

* three (U+0033) has a counter-clockwise outer contour

* three (U+0033) has a counter-clockwise outer contour

* two (U+0032) has a counter-clockwise outer contour

* two (U+0032) has a counter-clockwise outer contour

* two (U+0032) has a counter-clockwise outer contour

* two (U+0032) has a counter-clockwise outer contour

* two (U+0032) has a counter-clockwise outer contour

* ubreve (U+016D) has a counter-clockwise outer contour

* ubreve (U+016D) has a counter-clockwise outer contour

* ubreve (U+016D) has a counter-clockwise outer contour

* udieresis (U+00FC) has a counter-clockwise outer contour

* udieresis (U+00FC) has a counter-clockwise outer contour

* umacron (U+016B) has a counter-clockwise outer contour

* uni0162 (U+0162) has a counter-clockwise outer contour

* uni0162 (U+0162) has a counter-clockwise outer contour

* uni0162 (U+0162) has a counter-clockwise outer contour

* uni0162 (U+0162) has a counter-clockwise outer contour

* uni0163 (U+0163) has a counter-clockwise outer contour

* uni0163 (U+0163) has a counter-clockwise outer contour

* uni0163 (U+0163) has a counter-clockwise outer contour

* uni0163 (U+0163) has a counter-clockwise outer contour

* uni0304 (U+0304) has a counter-clockwise outer contour

* uni0306 (U+0306) has a counter-clockwise outer contour

* uni0306 (U+0306) has a counter-clockwise outer contour

* uni0306 (U+0306) has a counter-clockwise outer contour

* uni0307 (U+0307) has a counter-clockwise outer contour

* uni0308 (U+0308) has a counter-clockwise outer contour

* uni0308 (U+0308) has a counter-clockwise outer contour

* uni0327 (U+0327) has a counter-clockwise outer contour

* uni0327 (U+0327) has a counter-clockwise outer contour

* uni0327 (U+0327) has a counter-clockwise outer contour

* uni0327 (U+0327) has a counter-clockwise outer contour

* uni0328 (U+0328) has a counter-clockwise outer contour

* uni0328 (U+0328) has a counter-clockwise outer contour

* uni0328 (U+0328) has a counter-clockwise outer contour

* uni0917 (U+0917) has a counter-clockwise outer contour

* uni0917 (U+0917) has a counter-clockwise outer contour

* uni0917 (U+0917) has a counter-clockwise outer contour

* uni0917 (U+0917) has a counter-clockwise outer contour

* uni0917 (U+0917) has a counter-clockwise outer contour

* uogonek (U+0173) has a counter-clockwise outer contour

* uogonek (U+0173) has a counter-clockwise outer contour

* uogonek (U+0173) has a counter-clockwise outer contour

* x (U+0078) has a counter-clockwise outer contour

* x (U+0078) has a counter-clockwise outer contour

* ydieresis (U+00FF) has a counter-clockwise outer contour

* ydieresis (U+00FF) has a counter-clockwise outer contour

* zdotaccent (U+017C) has a counter-clockwise outer contour

* zero (U+0030) has a counter-clockwise outer contour

* zero (U+0030) has a counter-clockwise outer contour

* zero (U+0030) has a counter-clockwise outer contour

* zero (U+0030) has a counter-clockwise outer contour

* zero (U+0030) has a counter-clockwise outer contour

* zero (U+0030) has a counter-clockwise outer contour
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
    <summary>🔥 <b>FAIL</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.os2.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.fsSelection bit 7 (USE_TYPO_METRICS) wasNOT set in the following fonts: ['fonts/variable/Samaano[wdth,wght].ttf'].</p>
 [code: missing-os2-fsselection-bit7]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 14 | 10 | 97 | 8 | 122 | 0 | 
| 0% | 0% | 6% | 4% | 39% | 3% | 49% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
