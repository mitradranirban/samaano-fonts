## FontBakery report

fontbakery version: 0.12.10





## Check results



<details><summary>[13] Samaano[wdth,wght].ttf</summary>
<div>
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
<td align="left">U+1E0D: LATIN SMALL LETTER D WITH DOT BELOW</td>
<td align="left">U+1E0C: LATIN CAPITAL LETTER D WITH DOT BELOW</td>
</tr>
<tr>
<td align="left">U+1E35: LATIN SMALL LETTER K WITH LINE BELOW</td>
<td align="left">U+1E34: LATIN CAPITAL LETTER K WITH LINE BELOW</td>
</tr>
<tr>
<td align="left">U+1E37: LATIN SMALL LETTER L WITH DOT BELOW</td>
<td align="left">U+1E36: LATIN CAPITAL LETTER L WITH DOT BELOW</td>
</tr>
<tr>
<td align="left">U+1E39: LATIN SMALL LETTER L WITH DOT BELOW AND MACRON</td>
<td align="left">U+1E38: LATIN CAPITAL LETTER L WITH DOT BELOW AND MACRON</td>
</tr>
<tr>
<td align="left">U+1E3B: LATIN SMALL LETTER L WITH LINE BELOW</td>
<td align="left">U+1E3A: LATIN CAPITAL LETTER L WITH LINE BELOW</td>
</tr>
<tr>
<td align="left">U+1E43: LATIN SMALL LETTER M WITH DOT BELOW</td>
<td align="left">U+1E42: LATIN CAPITAL LETTER M WITH DOT BELOW</td>
</tr>
<tr>
<td align="left">U+1E45: LATIN SMALL LETTER N WITH DOT ABOVE</td>
<td align="left">U+1E44: LATIN CAPITAL LETTER N WITH DOT ABOVE</td>
</tr>
<tr>
<td align="left">U+1E47: LATIN SMALL LETTER N WITH DOT BELOW</td>
<td align="left">U+1E46: LATIN CAPITAL LETTER N WITH DOT BELOW</td>
</tr>
<tr>
<td align="left">U+1E49: LATIN SMALL LETTER N WITH LINE BELOW</td>
<td align="left">U+1E48: LATIN CAPITAL LETTER N WITH LINE BELOW</td>
</tr>
<tr>
<td align="left">U+1E4D: LATIN SMALL LETTER O WITH TILDE AND ACUTE</td>
<td align="left">U+1E4C: LATIN CAPITAL LETTER O WITH TILDE AND ACUTE</td>
</tr>
<tr>
<td align="left">U+1E5B: LATIN SMALL LETTER R WITH DOT BELOW</td>
<td align="left">U+1E5A: LATIN CAPITAL LETTER R WITH DOT BELOW</td>
</tr>
<tr>
<td align="left">U+1E5D: LATIN SMALL LETTER R WITH DOT BELOW AND MACRON</td>
<td align="left">U+1E5C: LATIN CAPITAL LETTER R WITH DOT BELOW AND MACRON</td>
</tr>
<tr>
<td align="left">U+1E5F: LATIN SMALL LETTER R WITH LINE BELOW</td>
<td align="left">U+1E5E: LATIN CAPITAL LETTER R WITH LINE BELOW</td>
</tr>
<tr>
<td align="left">U+1E63: LATIN SMALL LETTER S WITH DOT BELOW</td>
<td align="left">U+1E62: LATIN CAPITAL LETTER S WITH DOT BELOW</td>
</tr>
<tr>
<td align="left">U+1E6D: LATIN SMALL LETTER T WITH DOT BELOW</td>
<td align="left">U+1E6C: LATIN CAPITAL LETTER T WITH DOT BELOW</td>
</tr>
<tr>
<td align="left">U+1E8F: LATIN SMALL LETTER Y WITH DOT ABOVE</td>
<td align="left">U+1E8E: LATIN CAPITAL LETTER Y WITH DOT ABOVE</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Version format is correct in 'name' table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The NameID.VERSION_STRING (nameID=5) value must follow the pattern &quot;Version X.Y&quot; with X.Y greater than or equal to 1.000. Current version string is: &quot;Version 0.700&quot;</p>
 [code: bad-version-strings]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 60 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



* ⚠️ **WARN** <p>Font is monospaced but 1 glyphs (0.16%) have a different width. You should check the widths of: ['Ldot']</p>
 [code: mono-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check glyphs in mark glyph class are non-spacing. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following spacing glyphs may be in the GDEF mark glyph class by mistake:
acutecomb (U+0301), glyph094D (unencoded), gravecomb (U+0300), tildecomb (U+0303), uni0302 (U+0302), uni0304 (U+0304), uni0306 (U+0306), uni0307 (U+0307), uni0308 (U+0308), uni030A (U+030A), uni030B (U+030B), uni030C (U+030C), uni0326 (U+0326), uni0327 (U+0327), uni0328 (U+0328), uni0900 (U+0900), uni0901 (U+0901), uni0902 (U+0902), uni0930_uni094D.blwf (unencoded), uni0930_uni094D.rphf (unencoded), uni093A (U+093A), uni093C (U+093C), uni0941 (U+0941), uni0942 (U+0942), uni0943 (U+0943), uni0944 (U+0944), uni0945 (U+0945), uni0946 (U+0946), uni0947 (U+0947), uni0948 (U+0948), uni094D (U+094D), uni0951 (U+0951), uni0952 (U+0952), uni0953 (U+0953), uni0954 (U+0954), uni0955 (U+0955), uni0956 (U+0956), uni0957 (U+0957), uni0962 (U+0962) and uni0963 (U+0963)</p>
 [code: spacing-mark-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
dotbelowcomb (U+0323) and uni0331 (U+0331)</p>
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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, tifinagh, coptic, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: canadian-aboriginal, todhri, malayalam, tifinagh, syriac, coptic, tai-le, math, hebrew, old-permic, duployan</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: cherokee, thai, tifinagh, syriac, gothic, caucasian-albanian, sunuwar</li>
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
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̇ ǐ ị̇ ị̊ ị̋ ị̌ i̦̇ i̦̊ i̦̋ ǐ̦ i̧̇ i̧̊ i̧̋ ǐ̧ i̱̇ i̱̊ i̱̋ ǐ̱ j̆ j̇</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Ijo, Southeast (Latn, 2,471,000 speakers), Ebira (Latn, 2,200,000 speakers), Igbo (Latn, 27,823,640 speakers), Ekpeye (Latn, 226,000 speakers), Lithuanian (Latn, 2,357,094 speakers), Dutch (Latn, 31,709,104 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Avokaya (Latn, 100,000 speakers), Basaa (Latn, 332,940 speakers), Sar (Latn, 500,000 speakers), Dan (Latn, 1,099,244 speakers), Mango (Latn, 77,000 speakers), Koonzime (Latn, 40,000 speakers), Navajo (Latn, 166,319 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Ngbaka (Latn, 1,020,000 speakers), Southern Kisi (Latn, 360,000 speakers), Mfumte (Latn, 79,000 speakers), Makaa (Latn, 221,000 speakers), Mundani (Latn, 34,000 speakers), Fur (Latn, 1,230,163 speakers), Dii (Latn, 71,000 speakers), Yala (Latn, 200,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Ma’di (Latn, 584,000 speakers), Zapotec (Latn, 490,000 speakers), Belarusian (Cyrl, 10,064,517 speakers), South Central Banda (Latn, 244,000 speakers), Kom (Latn, 360,685 speakers), Vute (Latn, 21,000 speakers), Cicipu (Latn, 44,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Lugbara (Latn, 2,200,000 speakers), Gulay (Latn, 250,478 speakers), Nzakara (Latn, 50,000 speakers), Bafut (Latn, 158,146 speakers), Ejagham (Latn, 120,000 speakers), Nateni (Latn, 100,000 speakers), Aghem (Latn, 38,843 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* uni200D (U+200D) has a counter-clockwise outer contour
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




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 2 | 11 | 95 | 8 | 135 | 0 | 
| 0% | 0% | 1% | 4% | 38% | 3% | 54% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
