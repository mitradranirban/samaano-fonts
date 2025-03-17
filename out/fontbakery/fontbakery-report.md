## FontBakery report

fontbakery version: 0.13.1





## Experimental checks

These won't break the CI job for now, but will become effective after some time if nobody raises any concern.


<details><summary>[1] Samaano-Italic[wdth,wght].ttf</summary>
<div>
<details>
    <summary>✅ <b>PASS</b> Check base characters have non-zero advance width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#base-has-width">base_has_width</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>
</div>
</details>

<details><summary>[1] Samaano[wdth,wght].ttf</summary>
<div>
<details>
    <summary>✅ <b>PASS</b> Check base characters have non-zero advance width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#base-has-width">base_has_width</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>
</div>
</details>




## All other checks



<details><summary>[218] Samaano-Italic[wdth,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Do we have the latest version of FontBakery installed? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontbakery-version">fontbakery_version</a></summary>
    <div>







* 🔥 **FAIL** <p>Current FontBakery version is 0.13.1, while a newer 0.13.2 is already available. Please upgrade it with 'pip install -U fontbakery'</p>
 [code: outdated-fontbakery]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check correctness of STAT table strings <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#STAT-strings">STAT_strings</a></summary>
    <div>







* 🔥 **FAIL** <p>The following AxisValue entries on the STAT table should not contain &quot;Italic&quot;:
['nameID 2: Bold Italic']</p>
 [code: bad-italic]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">FAIL messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1ECA</td>
<td align="left">ig_Latn (Igbo)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1ECA</td>
<td align="left">ig_Latn (Igbo)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1ECD</td>
<td align="left">ig_Latn (Igbo) and yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1ECC</td>
<td align="left">ig_Latn (Igbo) and yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1ECD</td>
<td align="left">ig_Latn (Igbo) and yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1ECC</td>
<td align="left">ig_Latn (Igbo) and yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1EE5</td>
<td align="left">ig_Latn (Igbo)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1EE4</td>
<td align="left">ig_Latn (Igbo)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1EE5</td>
<td align="left">ig_Latn (Igbo)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1EE4</td>
<td align="left">ig_Latn (Igbo)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1EB9</td>
<td align="left">yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1EB8</td>
<td align="left">yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1EB9</td>
<td align="left">yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1EB8</td>
<td align="left">yo_Latn (Yoruba)</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* ⚠️ **WARN** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">WARN messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Some auxiliary glyphs were missing: ἀ, ἁ, ἂ, ἃ, ἄ, ἅ, ἆ, ἇ, ἐ, ἑ, ἒ, ἓ, ἔ, ἕ, ἠ, ἡ, ἢ, ἣ, ἤ, ἥ, ἦ, ἧ, ἰ, ἱ, ἲ, ἳ, ἴ, ἵ, ἶ, ἷ, ὂ, ὃ, ὄ, ὐ, ὑ, ὒ, ὓ, ὔ, ὕ, ὖ, ὗ, ὢ, ὣ, ὤ, ὥ, ὦ, ὧ, ᾶ, ῆ, ῖ, ῗ, ῦ, ῧ, ῶ</td>
<td align="left">el_Grek (Greek)</td>
</tr>
<tr>
<td align="left">No variant glyphs were found for Eng</td>
<td align="left">bm_Latn (Bambara), dyu_Latn (Dyula), ig_Latn (Igbo) and lg_Latn (Ganda)</td>
</tr>
<tr>
<td align="left">Some auxiliary glyphs were missing: Ɵ, ɵ</td>
<td align="left">ig_Latn (Igbo)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Validate STAT particle names and values match the fallback names in GFAxisRegistry. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-STAT-axisregistry">googlefonts/STAT/axisregistry</a></summary>
    <div>







* 🔥 **FAIL** <p>On the font variation axis 'slnt', the name 'Oblique' is not among the expected ones (Default) according to the Google Fonts Axis Registry.</p>
 [code: invalid-name]



* 🔥 **FAIL** <p>On the font variation axis 'wght', the name 'Bold Italic' is not among the expected ones (Thin, ExtraLight, Light, Regular, Medium, SemiBold, Bold, ExtraBold, Black) according to the Google Fonts Axis Registry.</p>
 [code: invalid-name]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-mark-chars">opentype/gdef_mark_chars</a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
uni0955 (U+0955)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check GDEF mark glyph class doesn't have characters that are not marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-non-mark-chars">opentype/gdef_non_mark_chars</a></summary>
    <div>







* ⚠️ **WARN** <p>The following non-mark characters should not be in the GDEF mark glyph class:
U+0384</p>
 [code: non-mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check glyphs in mark glyph class are non-spacing. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-spacing-marks">opentype/gdef_spacing_marks</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs seem to be spacing (because they have width &gt; 0 on the hmtx table) so they may be in the GDEF mark glyph class by mistake, or they should have zero width instead:
tonos (U+0384)</p>
 [code: spacing-mark-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>







* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1188 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#alt-caron">alt_caron</a></summary>
    <div>







* ✅ **PASS** <p>Looks good!</p>
 



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
    <summary>⚠️ <b>WARN</b> Detect any interpolation issues in the font. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#interpolation-issues">interpolation_issues</a></summary>
    <div>







* ⚠️ **WARN** <p>Interpolation issues were found in the font:</p>
<pre><code>- Contour 4 start point differs in glyph 'hryvnia' between location wdth=100,wght=700 and location wdth=200,wght=700

- Contour 5 start point differs in glyph 'hryvnia' between location wdth=100,wght=700 and location wdth=200,wght=700

- Contour 6 start point differs in glyph 'hryvnia' between location wdth=100,wght=700 and location wdth=200,wght=700
</code></pre>
 [code: interpolation-issues]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#ligature-carets">ligature_carets</a></summary>
    <div>







* ⚠️ **WARN** <p>This font lacks caret positioning values for these ligature glyphs:
- Ldot</p>
<pre><code>- j_uni0308

- j_uni0311

- ldot

- uni1ECB_uni0301
</code></pre>
 [code: incomplete-caret-pos-data]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure variable fonts include an avar table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#mandatory-avar-table">mandatory_avar_table</a></summary>
    <div>







* ⚠️ **WARN** <p>This variable font does not have an avar table. Most variable fonts should include an avar table to correctly define axes progression rates.</p>
 [code: missing-avar]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* Abreve (U+0102): L&lt;&lt;1231.0,1714.0&gt;--&lt;1206.0,1646.0&gt;&gt; has the same coordinates as a previous segment.

* Abreve (U+0102): L&lt;&lt;907.0,1714.0&gt;--&lt;882.0,1646.0&gt;&gt; has the same coordinates as a previous segment.

* Atilde (U+00C3): L&lt;&lt;883.0,1851.0&gt;--&lt;847.0,1752.0&gt;&gt; has the same coordinates as a previous segment.

* Atilde (U+00C3): L&lt;&lt;1175.0,1691.0&gt;--&lt;1211.0,1790.0&gt;&gt; has the same coordinates as a previous segment.

* B (U+0042): L&lt;&lt;788.0,1023.0&gt;--&lt;714.0,820.0&gt;&gt; has the same coordinates as a previous segment.

* B (U+0042): L&lt;&lt;704.0,766.0&gt;--&lt;631.0,567.0&gt;&gt; has the same coordinates as a previous segment.

* Bdotbelow (U+1E04): L&lt;&lt;788.0,1023.0&gt;--&lt;714.0,820.0&gt;&gt; has the same coordinates as a previous segment.

* Bdotbelow (U+1E04): L&lt;&lt;704.0,766.0&gt;--&lt;631.0,567.0&gt;&gt; has the same coordinates as a previous segment.

* Beta (U+0392): L&lt;&lt;788.0,1023.0&gt;--&lt;714.0,820.0&gt;&gt; has the same coordinates as a previous segment.

* Beta (U+0392): L&lt;&lt;704.0,766.0&gt;--&lt;631.0,567.0&gt;&gt; has the same coordinates as a previous segment.

* Bhook (U+0181): L&lt;&lt;788.0,1023.0&gt;--&lt;714.0,820.0&gt;&gt; has the same coordinates as a previous segment.

* Bhook (U+0181): L&lt;&lt;704.0,766.0&gt;--&lt;631.0,567.0&gt;&gt; has the same coordinates as a previous segment.

* Blinebelow (U+1E06): L&lt;&lt;788.0,1023.0&gt;--&lt;714.0,820.0&gt;&gt; has the same coordinates as a previous segment.

* Blinebelow (U+1E06): L&lt;&lt;704.0,766.0&gt;--&lt;631.0,567.0&gt;&gt; has the same coordinates as a previous segment.

* Ebreve (U+0114): L&lt;&lt;1289.0,1718.0&gt;--&lt;1264.0,1650.0&gt;&gt; has the same coordinates as a previous segment.

* Ebreve (U+0114): L&lt;&lt;965.0,1718.0&gt;--&lt;940.0,1650.0&gt;&gt; has the same coordinates as a previous segment.

* Ecedillabreve (U+1E1C): L&lt;&lt;1289.0,1718.0&gt;--&lt;1264.0,1650.0&gt;&gt; has the same coordinates as a previous segment.

* Ecedillabreve (U+1E1C): L&lt;&lt;965.0,1718.0&gt;--&lt;940.0,1650.0&gt;&gt; has the same coordinates as a previous segment.

* Euro (U+20AC): L&lt;&lt;447.0,179.0&gt;--&lt;637.0,179.0&gt;&gt; has the same coordinates as a previous segment.

* Gbreve (U+011E): L&lt;&lt;1285.0,1710.0&gt;--&lt;1260.0,1642.0&gt;&gt; has the same coordinates as a previous segment.

* Gbreve (U+011E): L&lt;&lt;961.0,1710.0&gt;--&lt;936.0,1642.0&gt;&gt; has the same coordinates as a previous segment.

* Ibreve (U+012C): L&lt;&lt;1248.0,1718.0&gt;--&lt;1223.0,1650.0&gt;&gt; has the same coordinates as a previous segment.

* Ibreve (U+012C): L&lt;&lt;924.0,1718.0&gt;--&lt;899.0,1650.0&gt;&gt; has the same coordinates as a previous segment.

* Itilde (U+0128): L&lt;&lt;900.0,1855.0&gt;--&lt;864.0,1756.0&gt;&gt; has the same coordinates as a previous segment.

* Itilde (U+0128): L&lt;&lt;1192.0,1695.0&gt;--&lt;1228.0,1794.0&gt;&gt; has the same coordinates as a previous segment.

* N (U+004E): L&lt;&lt;928.0,0.0&gt;--&lt;725.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* Nacute (U+0143): L&lt;&lt;928.0,0.0&gt;--&lt;725.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* Ncaron (U+0147): L&lt;&lt;928.0,0.0&gt;--&lt;725.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* Nhookleft (U+019D): L&lt;&lt;928.0,0.0&gt;--&lt;725.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* Nlinebelow (U+1E48): L&lt;&lt;928.0,0.0&gt;--&lt;725.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* Ntilde (U+00D1): L&lt;&lt;948.0,1827.0&gt;--&lt;912.0,1728.0&gt;&gt; has the same coordinates as a previous segment.

* Ntilde (U+00D1): L&lt;&lt;1240.0,1667.0&gt;--&lt;1276.0,1766.0&gt;&gt; has the same coordinates as a previous segment.

* Ntilde (U+00D1): L&lt;&lt;928.0,0.0&gt;--&lt;725.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* Nu (U+039D): L&lt;&lt;928.0,0.0&gt;--&lt;725.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* Obreve (U+014E): L&lt;&lt;1332.0,1703.0&gt;--&lt;1307.0,1635.0&gt;&gt; has the same coordinates as a previous segment.

* Obreve (U+014E): L&lt;&lt;1008.0,1703.0&gt;--&lt;983.0,1635.0&gt;&gt; has the same coordinates as a previous segment.

* Otilde (U+00D5): L&lt;&lt;984.0,1840.0&gt;--&lt;948.0,1741.0&gt;&gt; has the same coordinates as a previous segment.

* Otilde (U+00D5): L&lt;&lt;1276.0,1680.0&gt;--&lt;1312.0,1779.0&gt;&gt; has the same coordinates as a previous segment.

* S (U+0053): L&lt;&lt;500.0,1028.0&gt;--&lt;702.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* S (U+0053): L&lt;&lt;1027.0,355.0&gt;--&lt;826.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* Sacute (U+015A): L&lt;&lt;500.0,1028.0&gt;--&lt;702.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* Sacute (U+015A): L&lt;&lt;1027.0,355.0&gt;--&lt;826.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* Scaron (U+0160): L&lt;&lt;500.0,1028.0&gt;--&lt;702.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* Scaron (U+0160): L&lt;&lt;1027.0,355.0&gt;--&lt;826.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* Scedilla (U+015E): L&lt;&lt;500.0,1028.0&gt;--&lt;702.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* Scedilla (U+015E): L&lt;&lt;1027.0,355.0&gt;--&lt;826.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* Scircumflex (U+015C): L&lt;&lt;500.0,1028.0&gt;--&lt;702.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* Scircumflex (U+015C): L&lt;&lt;1027.0,355.0&gt;--&lt;826.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* Ubreve (U+016C): L&lt;&lt;1253.0,1715.0&gt;--&lt;1228.0,1647.0&gt;&gt; has the same coordinates as a previous segment.

* Ubreve (U+016C): L&lt;&lt;929.0,1715.0&gt;--&lt;904.0,1647.0&gt;&gt; has the same coordinates as a previous segment.

* Utilde (U+0168): L&lt;&lt;905.0,1852.0&gt;--&lt;869.0,1753.0&gt;&gt; has the same coordinates as a previous segment.

* Utilde (U+0168): L&lt;&lt;1197.0,1692.0&gt;--&lt;1233.0,1791.0&gt;&gt; has the same coordinates as a previous segment.

* abreve (U+0103): L&lt;&lt;1039.0,1217.0&gt;--&lt;1014.0,1149.0&gt;&gt; has the same coordinates as a previous segment.

* abreve (U+0103): L&lt;&lt;715.0,1217.0&gt;--&lt;690.0,1149.0&gt;&gt; has the same coordinates as a previous segment.

* approxequal (U+2248): L&lt;&lt;533.0,559.0&gt;--&lt;497.0,395.0&gt;&gt; has the same coordinates as a previous segment.

* approxequal (U+2248): L&lt;&lt;825.0,334.0&gt;--&lt;861.0,498.0&gt;&gt; has the same coordinates as a previous segment.

* approxequal (U+2248): L&lt;&lt;627.0,898.0&gt;--&lt;591.0,716.0&gt;&gt; has the same coordinates as a previous segment.

* approxequal (U+2248): L&lt;&lt;918.0,655.0&gt;--&lt;954.0,837.0&gt;&gt; has the same coordinates as a previous segment.

* asciitilde (U+007E): L&lt;&lt;384.0,815.0&gt;--&lt;348.0,656.0&gt;&gt; has the same coordinates as a previous segment.

* asciitilde (U+007E): L&lt;&lt;676.0,595.0&gt;--&lt;712.0,754.0&gt;&gt; has the same coordinates as a previous segment.

* atilde (U+00E3): L&lt;&lt;691.0,1354.0&gt;--&lt;655.0,1255.0&gt;&gt; has the same coordinates as a previous segment.

* atilde (U+00E3): L&lt;&lt;983.0,1194.0&gt;--&lt;1019.0,1293.0&gt;&gt; has the same coordinates as a previous segment.

* baht (U+0E3F): L&lt;&lt;788.0,1023.0&gt;--&lt;714.0,820.0&gt;&gt; has the same coordinates as a previous segment.

* baht (U+0E3F): L&lt;&lt;704.0,766.0&gt;--&lt;631.0,567.0&gt;&gt; has the same coordinates as a previous segment.

* braceleft (U+007B): L&lt;&lt;817.0,838.0&gt;--&lt;963.0,838.0&gt;&gt; has the same coordinates as a previous segment.

* braceleft (U+007B): L&lt;&lt;452.0,630.0&gt;--&lt;474.0,690.0&gt;&gt; has the same coordinates as a previous segment.

* braceright (U+007D): L&lt;&lt;1052.0,690.0&gt;--&lt;1030.0,630.0&gt;&gt; has the same coordinates as a previous segment.

* braceright (U+007D): L&lt;&lt;668.0,424.0&gt;--&lt;508.0,424.0&gt;&gt; has the same coordinates as a previous segment.

* breve (U+02D8): L&lt;&lt;1240.0,1548.0&gt;--&lt;1216.0,1480.0&gt;&gt; has the same coordinates as a previous segment.

* breve (U+02D8): L&lt;&lt;916.0,1548.0&gt;--&lt;892.0,1480.0&gt;&gt; has the same coordinates as a previous segment.

* brevecomb_acutecomb: L&lt;&lt;192.0,1209.0&gt;--&lt;167.0,1141.0&gt;&gt; has the same coordinates as a previous segment.

* brevecomb_acutecomb: L&lt;&lt;-132.0,1209.0&gt;--&lt;-157.0,1141.0&gt;&gt; has the same coordinates as a previous segment.

* brevecomb_gravecomb: L&lt;&lt;192.0,1209.0&gt;--&lt;167.0,1141.0&gt;&gt; has the same coordinates as a previous segment.

* brevecomb_gravecomb: L&lt;&lt;-132.0,1209.0&gt;--&lt;-157.0,1141.0&gt;&gt; has the same coordinates as a previous segment.

* brevecomb_hookabovecomb: L&lt;&lt;174.0,1136.0&gt;--&lt;149.0,1068.0&gt;&gt; has the same coordinates as a previous segment.

* brevecomb_hookabovecomb: L&lt;&lt;-150.0,1136.0&gt;--&lt;-175.0,1068.0&gt;&gt; has the same coordinates as a previous segment.

* brevecomb_tildecomb: L&lt;&lt;183.0,899.0&gt;--&lt;158.0,831.0&gt;&gt; has the same coordinates as a previous segment.

* brevecomb_tildecomb: L&lt;&lt;-141.0,899.0&gt;--&lt;-166.0,831.0&gt;&gt; has the same coordinates as a previous segment.

* brevecomb_tildecomb: L&lt;&lt;-124.0,1216.0&gt;--&lt;-160.0,1117.0&gt;&gt; has the same coordinates as a previous segment.

* brevecomb_tildecomb: L&lt;&lt;168.0,1056.0&gt;--&lt;204.0,1155.0&gt;&gt; has the same coordinates as a previous segment.

* circumflexcomb_tildecomb: L&lt;&lt;-128.0,1184.0&gt;--&lt;-164.0,1085.0&gt;&gt; has the same coordinates as a previous segment.

* circumflexcomb_tildecomb: L&lt;&lt;164.0,1024.0&gt;--&lt;200.0,1123.0&gt;&gt; has the same coordinates as a previous segment.

* dollar (U+0024): L&lt;&lt;293.0,1028.0&gt;--&lt;498.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* dollar (U+0024): L&lt;&lt;820.0,355.0&gt;--&lt;614.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* ebreve (U+0115): L&lt;&lt;1111.0,1229.0&gt;--&lt;1086.0,1161.0&gt;&gt; has the same coordinates as a previous segment.

* ebreve (U+0115): L&lt;&lt;787.0,1229.0&gt;--&lt;762.0,1161.0&gt;&gt; has the same coordinates as a previous segment.

* ecedillabreve (U+1E1D): L&lt;&lt;1111.0,1229.0&gt;--&lt;1086.0,1161.0&gt;&gt; has the same coordinates as a previous segment.

* ecedillabreve (U+1E1D): L&lt;&lt;787.0,1229.0&gt;--&lt;762.0,1161.0&gt;&gt; has the same coordinates as a previous segment.

* gbreve (U+011F): L&lt;&lt;1064.0,1207.0&gt;--&lt;1039.0,1139.0&gt;&gt; has the same coordinates as a previous segment.

* gbreve (U+011F): L&lt;&lt;740.0,1207.0&gt;--&lt;715.0,1139.0&gt;&gt; has the same coordinates as a previous segment.

* greater (U+003E): L&lt;&lt;1041.0,777.0&gt;--&lt;967.0,568.0&gt;&gt; has the same coordinates as a previous segment.

* greaterequal (U+2265): L&lt;&lt;1205.0,777.0&gt;--&lt;1131.0,568.0&gt;&gt; has the same coordinates as a previous segment.

* guillemotleft (U+00AB): L&lt;&lt;286.0,454.0&gt;--&lt;342.0,609.0&gt;&gt; has the same coordinates as a previous segment.

* guillemotleft (U+00AB): L&lt;&lt;701.0,454.0&gt;--&lt;757.0,609.0&gt;&gt; has the same coordinates as a previous segment.

* guillemotright (U+00BB): L&lt;&lt;1125.0,609.0&gt;--&lt;1069.0,454.0&gt;&gt; has the same coordinates as a previous segment.

* guillemotright (U+00BB): L&lt;&lt;710.0,609.0&gt;--&lt;654.0,454.0&gt;&gt; has the same coordinates as a previous segment.

* guilsinglleft (U+2039): L&lt;&lt;22.0,569.0&gt;--&lt;98.0,777.0&gt;&gt; has the same coordinates as a previous segment.

* guilsinglright (U+203A): L&lt;&lt;1041.0,777.0&gt;--&lt;967.0,568.0&gt;&gt; has the same coordinates as a previous segment.

* hryvnia (U+20B4): L&lt;&lt;1292.0,1028.0&gt;--&lt;1090.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* hryvnia (U+20B4): L&lt;&lt;275.0,355.0&gt;--&lt;476.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* ibreve (U+012D): L&lt;&lt;1120.0,1264.0&gt;--&lt;1095.0,1196.0&gt;&gt; has the same coordinates as a previous segment.

* ibreve (U+012D): L&lt;&lt;796.0,1264.0&gt;--&lt;771.0,1196.0&gt;&gt; has the same coordinates as a previous segment.

* itilde (U+0129): L&lt;&lt;772.0,1401.0&gt;--&lt;736.0,1302.0&gt;&gt; has the same coordinates as a previous segment.

* itilde (U+0129): L&lt;&lt;1064.0,1241.0&gt;--&lt;1100.0,1340.0&gt;&gt; has the same coordinates as a previous segment.

* j_uni0303: L&lt;&lt;919.0,1234.0&gt;--&lt;883.0,1135.0&gt;&gt; has the same coordinates as a previous segment.

* j_uni0303: L&lt;&lt;1211.0,1074.0&gt;--&lt;1247.0,1173.0&gt;&gt; has the same coordinates as a previous segment.

* j_uni0311: L&lt;&lt;892.0,1063.0&gt;--&lt;916.0,1131.0&gt;&gt; has the same coordinates as a previous segment.

* j_uni0311: L&lt;&lt;1216.0,1063.0&gt;--&lt;1240.0,1131.0&gt;&gt; has the same coordinates as a previous segment.

* less (U+003C): L&lt;&lt;22.0,569.0&gt;--&lt;98.0,777.0&gt;&gt; has the same coordinates as a previous segment.

* lessequal (U+2264): L&lt;&lt;310.0,569.0&gt;--&lt;386.0,777.0&gt;&gt; has the same coordinates as a previous segment.

* ntilde (U+00F1): L&lt;&lt;846.0,1337.0&gt;--&lt;810.0,1238.0&gt;&gt; has the same coordinates as a previous segment.

* ntilde (U+00F1): L&lt;&lt;1138.0,1177.0&gt;--&lt;1174.0,1276.0&gt;&gt; has the same coordinates as a previous segment.

* obreve (U+014F): L&lt;&lt;1076.0,1200.0&gt;--&lt;1051.0,1132.0&gt;&gt; has the same coordinates as a previous segment.

* obreve (U+014F): L&lt;&lt;752.0,1200.0&gt;--&lt;727.0,1132.0&gt;&gt; has the same coordinates as a previous segment.

* otilde (U+00F5): L&lt;&lt;728.0,1337.0&gt;--&lt;692.0,1238.0&gt;&gt; has the same coordinates as a previous segment.

* otilde (U+00F5): L&lt;&lt;1020.0,1177.0&gt;--&lt;1056.0,1276.0&gt;&gt; has the same coordinates as a previous segment.

* parenleft (U+0028): L&lt;&lt;72.0,179.0&gt;--&lt;262.0,179.0&gt;&gt; has the same coordinates as a previous segment.

* parenright (U+0029): L&lt;&lt;938.0,1023.0&gt;--&lt;748.0,1023.0&gt;&gt; has the same coordinates as a previous segment.

* parenright (U+0029): L&lt;&lt;441.0,179.0&gt;--&lt;631.0,179.0&gt;&gt; has the same coordinates as a previous segment.

* peseta (U+20A7): L&lt;&lt;938.0,438.0&gt;--&lt;989.0,438.0&gt;&gt; has the same coordinates as a previous segment.

* peseta (U+20A7): L&lt;&lt;995.0,173.0&gt;--&lt;944.0,173.0&gt;&gt; has the same coordinates as a previous segment.

* ringhalfleft (U+02BF): L&lt;&lt;503.0,1199.0&gt;--&lt;435.0,1223.0&gt;&gt; has the same coordinates as a previous segment.

* ringhalfleft (U+02BF): L&lt;&lt;503.0,1523.0&gt;--&lt;435.0,1547.0&gt;&gt; has the same coordinates as a previous segment.

* ringhalfright (U+02BE): L&lt;&lt;541.0,1495.0&gt;--&lt;609.0,1471.0&gt;&gt; has the same coordinates as a previous segment.

* ringhalfright (U+02BE): L&lt;&lt;541.0,1171.0&gt;--&lt;609.0,1147.0&gt;&gt; has the same coordinates as a previous segment.

* rupee (U+20A8): L&lt;&lt;695.0,736.0&gt;--&lt;795.0,736.0&gt;&gt; has the same coordinates as a previous segment.

* rupee (U+20A8): L&lt;&lt;916.0,293.0&gt;--&lt;816.0,293.0&gt;&gt; has the same coordinates as a previous segment.

* s (U+0073): L&lt;&lt;919.0,293.0&gt;--&lt;719.0,293.0&gt;&gt; has the same coordinates as a previous segment.

* sacute (U+015B): L&lt;&lt;919.0,293.0&gt;--&lt;719.0,293.0&gt;&gt; has the same coordinates as a previous segment.

* scaron (U+0161): L&lt;&lt;919.0,293.0&gt;--&lt;719.0,293.0&gt;&gt; has the same coordinates as a previous segment.

* scedilla (U+015F): L&lt;&lt;919.0,293.0&gt;--&lt;719.0,293.0&gt;&gt; has the same coordinates as a previous segment.

* scircumflex (U+015D): L&lt;&lt;919.0,293.0&gt;--&lt;719.0,293.0&gt;&gt; has the same coordinates as a previous segment.

* section (U+00A7): L&lt;&lt;341.0,605.0&gt;--&lt;543.0,605.0&gt;&gt; has the same coordinates as a previous segment.

* section (U+00A7): L&lt;&lt;936.0,95.0&gt;--&lt;735.0,95.0&gt;&gt; has the same coordinates as a previous segment.

* section (U+00A7): L&lt;&lt;571.0,1237.0&gt;--&lt;773.0,1237.0&gt;&gt; has the same coordinates as a previous segment.

* section (U+00A7): L&lt;&lt;1054.0,442.0&gt;--&lt;853.0,442.0&gt;&gt; has the same coordinates as a previous segment.

* sheqel (U+20AA): L&lt;&lt;1084.0,1278.0&gt;--&lt;1231.0,1277.0&gt;&gt; has the same coordinates as a previous segment.

* sheqel (U+20AA): L&lt;&lt;560.0,264.0&gt;--&lt;412.0,265.0&gt;&gt; has the same coordinates as a previous segment.

* tilde (U+02DC): L&lt;&lt;410.0,1607.0&gt;--&lt;381.0,1528.0&gt;&gt; has the same coordinates as a previous segment.

* tilde (U+02DC): L&lt;&lt;643.0,1479.0&gt;--&lt;672.0,1558.0&gt;&gt; has the same coordinates as a previous segment.

* tildecomb (U+0303): L&lt;&lt;-164.0,969.0&gt;--&lt;-200.0,870.0&gt;&gt; has the same coordinates as a previous segment.

* tildecomb (U+0303): L&lt;&lt;128.0,809.0&gt;--&lt;164.0,908.0&gt;&gt; has the same coordinates as a previous segment.

* ubreve (U+016D): L&lt;&lt;1026.0,1195.0&gt;--&lt;1001.0,1127.0&gt;&gt; has the same coordinates as a previous segment.

* ubreve (U+016D): L&lt;&lt;702.0,1195.0&gt;--&lt;677.0,1127.0&gt;&gt; has the same coordinates as a previous segment.

* uni012F_uni0303: L&lt;&lt;718.0,1257.0&gt;--&lt;682.0,1158.0&gt;&gt; has the same coordinates as a previous segment.

* uni012F_uni0303: L&lt;&lt;1010.0,1097.0&gt;--&lt;1046.0,1196.0&gt;&gt; has the same coordinates as a previous segment.

* uni0145 (U+0145): L&lt;&lt;928.0,0.0&gt;--&lt;725.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni01C4 (U+01C4): L&lt;&lt;535.0,374.0&gt;--&lt;499.0,200.0&gt;&gt; has the same coordinates as a previous segment.

* uni01CA (U+01CA): L&lt;&lt;749.0,0.0&gt;--&lt;648.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni01CB (U+01CB): L&lt;&lt;670.0,0.0&gt;--&lt;569.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni01F8 (U+01F8): L&lt;&lt;928.0,0.0&gt;--&lt;725.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0202 (U+0202): L&lt;&lt;834.0,1686.0&gt;--&lt;858.0,1754.0&gt;&gt; has the same coordinates as a previous segment.

* uni0202 (U+0202): L&lt;&lt;1158.0,1686.0&gt;--&lt;1182.0,1754.0&gt;&gt; has the same coordinates as a previous segment.

* uni0203 (U+0203): L&lt;&lt;642.0,1189.0&gt;--&lt;666.0,1257.0&gt;&gt; has the same coordinates as a previous segment.

* uni0203 (U+0203): L&lt;&lt;966.0,1189.0&gt;--&lt;990.0,1257.0&gt;&gt; has the same coordinates as a previous segment.

* uni0206 (U+0206): L&lt;&lt;892.0,1690.0&gt;--&lt;916.0,1758.0&gt;&gt; has the same coordinates as a previous segment.

* uni0206 (U+0206): L&lt;&lt;1216.0,1690.0&gt;--&lt;1240.0,1758.0&gt;&gt; has the same coordinates as a previous segment.

* uni0207 (U+0207): L&lt;&lt;714.0,1201.0&gt;--&lt;738.0,1269.0&gt;&gt; has the same coordinates as a previous segment.

* uni0207 (U+0207): L&lt;&lt;1038.0,1201.0&gt;--&lt;1062.0,1269.0&gt;&gt; has the same coordinates as a previous segment.

* uni020A (U+020A): L&lt;&lt;851.0,1690.0&gt;--&lt;875.0,1758.0&gt;&gt; has the same coordinates as a previous segment.

* uni020A (U+020A): L&lt;&lt;1175.0,1690.0&gt;--&lt;1199.0,1758.0&gt;&gt; has the same coordinates as a previous segment.

* uni020B (U+020B): L&lt;&lt;723.0,1236.0&gt;--&lt;747.0,1304.0&gt;&gt; has the same coordinates as a previous segment.

* uni020B (U+020B): L&lt;&lt;1047.0,1236.0&gt;--&lt;1071.0,1304.0&gt;&gt; has the same coordinates as a previous segment.

* uni020E (U+020E): L&lt;&lt;935.0,1675.0&gt;--&lt;959.0,1743.0&gt;&gt; has the same coordinates as a previous segment.

* uni020E (U+020E): L&lt;&lt;1259.0,1675.0&gt;--&lt;1283.0,1743.0&gt;&gt; has the same coordinates as a previous segment.

* uni020F (U+020F): L&lt;&lt;679.0,1172.0&gt;--&lt;703.0,1240.0&gt;&gt; has the same coordinates as a previous segment.

* uni020F (U+020F): L&lt;&lt;1003.0,1172.0&gt;--&lt;1027.0,1240.0&gt;&gt; has the same coordinates as a previous segment.

* uni0212 (U+0212): L&lt;&lt;840.0,1681.0&gt;--&lt;864.0,1749.0&gt;&gt; has the same coordinates as a previous segment.

* uni0212 (U+0212): L&lt;&lt;1164.0,1681.0&gt;--&lt;1188.0,1749.0&gt;&gt; has the same coordinates as a previous segment.

* uni0213 (U+0213): L&lt;&lt;596.0,1219.0&gt;--&lt;620.0,1287.0&gt;&gt; has the same coordinates as a previous segment.

* uni0213 (U+0213): L&lt;&lt;920.0,1219.0&gt;--&lt;944.0,1287.0&gt;&gt; has the same coordinates as a previous segment.

* uni0216 (U+0216): L&lt;&lt;856.0,1687.0&gt;--&lt;880.0,1755.0&gt;&gt; has the same coordinates as a previous segment.

* uni0216 (U+0216): L&lt;&lt;1180.0,1687.0&gt;--&lt;1204.0,1755.0&gt;&gt; has the same coordinates as a previous segment.

* uni0217 (U+0217): L&lt;&lt;629.0,1167.0&gt;--&lt;653.0,1235.0&gt;&gt; has the same coordinates as a previous segment.

* uni0217 (U+0217): L&lt;&lt;953.0,1167.0&gt;--&lt;977.0,1235.0&gt;&gt; has the same coordinates as a previous segment.

* uni0218 (U+0218): L&lt;&lt;500.0,1028.0&gt;--&lt;702.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* uni0218 (U+0218): L&lt;&lt;1027.0,355.0&gt;--&lt;826.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* uni0219 (U+0219): L&lt;&lt;919.0,293.0&gt;--&lt;719.0,293.0&gt;&gt; has the same coordinates as a previous segment.

* uni022C (U+022C): L&lt;&lt;984.0,1840.0&gt;--&lt;948.0,1741.0&gt;&gt; has the same coordinates as a previous segment.

* uni022C (U+022C): L&lt;&lt;1276.0,1680.0&gt;--&lt;1312.0,1779.0&gt;&gt; has the same coordinates as a previous segment.

* uni022D (U+022D): L&lt;&lt;728.0,1337.0&gt;--&lt;692.0,1238.0&gt;&gt; has the same coordinates as a previous segment.

* uni022D (U+022D): L&lt;&lt;1020.0,1177.0&gt;--&lt;1056.0,1276.0&gt;&gt; has the same coordinates as a previous segment.

* uni0306 (U+0306): L&lt;&lt;183.0,899.0&gt;--&lt;158.0,831.0&gt;&gt; has the same coordinates as a previous segment.

* uni0306 (U+0306): L&lt;&lt;-141.0,899.0&gt;--&lt;-166.0,831.0&gt;&gt; has the same coordinates as a previous segment.

* uni0311 (U+0311): L&lt;&lt;-202.0,831.0&gt;--&lt;-178.0,899.0&gt;&gt; has the same coordinates as a previous segment.

* uni0311 (U+0311): L&lt;&lt;122.0,831.0&gt;--&lt;146.0,899.0&gt;&gt; has the same coordinates as a previous segment.

* uni032E (U+032E): L&lt;&lt;134.0,-173.0&gt;--&lt;109.0,-241.0&gt;&gt; has the same coordinates as a previous segment.

* uni032E (U+032E): L&lt;&lt;-190.0,-173.0&gt;--&lt;-215.0,-241.0&gt;&gt; has the same coordinates as a previous segment.

* uni0926_uni094D_uni092F.pres: L&lt;&lt;830.0,428.0&gt;--&lt;757.0,229.0&gt;&gt; has the same coordinates as a previous segment.

* uni092F (U+092F): L&lt;&lt;626.0,846.0&gt;--&lt;836.0,846.0&gt;&gt; has the same coordinates as a previous segment.

* uni092F_uni0930_uni094D.vatu: L&lt;&lt;626.0,846.0&gt;--&lt;836.0,846.0&gt;&gt; has the same coordinates as a previous segment.

* uni092F_uni094D.half: L&lt;&lt;876.0,846.0&gt;--&lt;1086.0,846.0&gt;&gt; has the same coordinates as a previous segment.

* uni092F_uni094D.haln: L&lt;&lt;638.0,846.0&gt;--&lt;848.0,846.0&gt;&gt; has the same coordinates as a previous segment.

* uni0930_uni094D.half: L&lt;&lt;988.0,802.0&gt;--&lt;915.0,603.0&gt;&gt; has the same coordinates as a previous segment.

* uni0930_uni094D.rphf: L&lt;&lt;378.0,2152.0&gt;--&lt;305.0,1952.0&gt;&gt; has the same coordinates as a previous segment.

* uni0930_uni094D_uni0902.abvs: L&lt;&lt;398.0,2099.0&gt;--&lt;325.0,1899.0&gt;&gt; has the same coordinates as a previous segment.

* uni095F (U+095F): L&lt;&lt;626.0,846.0&gt;--&lt;836.0,846.0&gt;&gt; has the same coordinates as a previous segment.

* uni095F_uni0930_uni094D.vatu: L&lt;&lt;626.0,846.0&gt;--&lt;836.0,846.0&gt;&gt; has the same coordinates as a previous segment.

* uni095F_uni094D.half: L&lt;&lt;626.0,846.0&gt;--&lt;836.0,846.0&gt;&gt; has the same coordinates as a previous segment.

* uni095F_uni094D.haln: L&lt;&lt;646.0,846.0&gt;--&lt;856.0,846.0&gt;&gt; has the same coordinates as a previous segment.

* uni096A (U+096A): L&lt;&lt;273.0,317.0&gt;--&lt;473.0,317.0&gt;&gt; has the same coordinates as a previous segment.

* uni097A (U+097A): L&lt;&lt;626.0,846.0&gt;--&lt;836.0,846.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E02 (U+1E02): L&lt;&lt;788.0,1023.0&gt;--&lt;714.0,820.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E02 (U+1E02): L&lt;&lt;704.0,766.0&gt;--&lt;631.0,567.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E2A (U+1E2A): L&lt;&lt;638.0,-203.0&gt;--&lt;613.0,-271.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E2A (U+1E2A): L&lt;&lt;314.0,-203.0&gt;--&lt;289.0,-271.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E2B (U+1E2B): L&lt;&lt;654.0,-215.0&gt;--&lt;629.0,-283.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E2B (U+1E2B): L&lt;&lt;330.0,-215.0&gt;--&lt;305.0,-283.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E44 (U+1E44): L&lt;&lt;928.0,0.0&gt;--&lt;725.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E46 (U+1E46): L&lt;&lt;928.0,0.0&gt;--&lt;725.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E4C (U+1E4C): L&lt;&lt;984.0,1840.0&gt;--&lt;948.0,1741.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E4C (U+1E4C): L&lt;&lt;1276.0,1680.0&gt;--&lt;1312.0,1779.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E4D (U+1E4D): L&lt;&lt;728.0,1337.0&gt;--&lt;692.0,1238.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E4D (U+1E4D): L&lt;&lt;1020.0,1177.0&gt;--&lt;1056.0,1276.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E4E (U+1E4E): L&lt;&lt;984.0,1840.0&gt;--&lt;948.0,1741.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E4E (U+1E4E): L&lt;&lt;1276.0,1680.0&gt;--&lt;1312.0,1779.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E4F (U+1E4F): L&lt;&lt;728.0,1337.0&gt;--&lt;692.0,1238.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E4F (U+1E4F): L&lt;&lt;1020.0,1177.0&gt;--&lt;1056.0,1276.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E60 (U+1E60): L&lt;&lt;500.0,1028.0&gt;--&lt;702.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E60 (U+1E60): L&lt;&lt;1027.0,355.0&gt;--&lt;826.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E61 (U+1E61): L&lt;&lt;919.0,293.0&gt;--&lt;719.0,293.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E62 (U+1E62): L&lt;&lt;500.0,1028.0&gt;--&lt;702.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E62 (U+1E62): L&lt;&lt;1027.0,355.0&gt;--&lt;826.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E63 (U+1E63): L&lt;&lt;919.0,293.0&gt;--&lt;719.0,293.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E64 (U+1E64): L&lt;&lt;500.0,1028.0&gt;--&lt;702.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E64 (U+1E64): L&lt;&lt;1027.0,355.0&gt;--&lt;826.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E65 (U+1E65): L&lt;&lt;919.0,293.0&gt;--&lt;719.0,293.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E66 (U+1E66): L&lt;&lt;500.0,1028.0&gt;--&lt;702.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E66 (U+1E66): L&lt;&lt;1027.0,355.0&gt;--&lt;826.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E67 (U+1E67): L&lt;&lt;919.0,293.0&gt;--&lt;719.0,293.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E68 (U+1E68): L&lt;&lt;500.0,1028.0&gt;--&lt;702.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E68 (U+1E68): L&lt;&lt;1027.0,355.0&gt;--&lt;826.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E69 (U+1E69): L&lt;&lt;919.0,293.0&gt;--&lt;719.0,293.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E78 (U+1E78): L&lt;&lt;905.0,1852.0&gt;--&lt;869.0,1753.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E78 (U+1E78): L&lt;&lt;1197.0,1692.0&gt;--&lt;1233.0,1791.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E79 (U+1E79): L&lt;&lt;678.0,1332.0&gt;--&lt;642.0,1233.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E79 (U+1E79): L&lt;&lt;970.0,1172.0&gt;--&lt;1006.0,1271.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E7C (U+1E7C): L&lt;&lt;972.0,1803.0&gt;--&lt;936.0,1704.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E7C (U+1E7C): L&lt;&lt;1264.0,1643.0&gt;--&lt;1300.0,1742.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E7D (U+1E7D): L&lt;&lt;758.0,1290.0&gt;--&lt;722.0,1191.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E7D (U+1E7D): L&lt;&lt;1050.0,1130.0&gt;--&lt;1086.0,1229.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EAA (U+1EAA): L&lt;&lt;1090.0,2216.0&gt;--&lt;1054.0,2117.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EAA (U+1EAA): L&lt;&lt;1382.0,2056.0&gt;--&lt;1418.0,2155.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EAB (U+1EAB): L&lt;&lt;898.0,1719.0&gt;--&lt;862.0,1620.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EAB (U+1EAB): L&lt;&lt;1190.0,1559.0&gt;--&lt;1226.0,1658.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EAE (U+1EAE): L&lt;&lt;1231.0,1714.0&gt;--&lt;1206.0,1646.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EAE (U+1EAE): L&lt;&lt;907.0,1714.0&gt;--&lt;882.0,1646.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EAF (U+1EAF): L&lt;&lt;1039.0,1217.0&gt;--&lt;1014.0,1149.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EAF (U+1EAF): L&lt;&lt;715.0,1217.0&gt;--&lt;690.0,1149.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB0 (U+1EB0): L&lt;&lt;1231.0,1714.0&gt;--&lt;1206.0,1646.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB0 (U+1EB0): L&lt;&lt;907.0,1714.0&gt;--&lt;882.0,1646.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB1 (U+1EB1): L&lt;&lt;1039.0,1217.0&gt;--&lt;1014.0,1149.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB1 (U+1EB1): L&lt;&lt;715.0,1217.0&gt;--&lt;690.0,1149.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB2 (U+1EB2): L&lt;&lt;1231.0,1714.0&gt;--&lt;1206.0,1646.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB2 (U+1EB2): L&lt;&lt;907.0,1714.0&gt;--&lt;882.0,1646.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB3 (U+1EB3): L&lt;&lt;1039.0,1217.0&gt;--&lt;1014.0,1149.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB3 (U+1EB3): L&lt;&lt;715.0,1217.0&gt;--&lt;690.0,1149.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB4 (U+1EB4): L&lt;&lt;1387.0,2093.0&gt;--&lt;1351.0,1994.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB4 (U+1EB4): L&lt;&lt;1679.0,1933.0&gt;--&lt;1715.0,2032.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB4 (U+1EB4): L&lt;&lt;1231.0,1714.0&gt;--&lt;1206.0,1646.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB4 (U+1EB4): L&lt;&lt;907.0,1714.0&gt;--&lt;882.0,1646.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB5 (U+1EB5): L&lt;&lt;1195.0,1596.0&gt;--&lt;1159.0,1497.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB5 (U+1EB5): L&lt;&lt;1487.0,1436.0&gt;--&lt;1523.0,1535.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB5 (U+1EB5): L&lt;&lt;1039.0,1217.0&gt;--&lt;1014.0,1149.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB5 (U+1EB5): L&lt;&lt;715.0,1217.0&gt;--&lt;690.0,1149.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB6 (U+1EB6): L&lt;&lt;1255.0,1738.0&gt;--&lt;1230.0,1670.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB6 (U+1EB6): L&lt;&lt;931.0,1738.0&gt;--&lt;906.0,1670.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB7 (U+1EB7): L&lt;&lt;1117.0,1213.0&gt;--&lt;1092.0,1145.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB7 (U+1EB7): L&lt;&lt;793.0,1213.0&gt;--&lt;768.0,1145.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EBC (U+1EBC): L&lt;&lt;941.0,1855.0&gt;--&lt;905.0,1756.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EBC (U+1EBC): L&lt;&lt;1233.0,1695.0&gt;--&lt;1269.0,1794.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EBD (U+1EBD): L&lt;&lt;763.0,1366.0&gt;--&lt;727.0,1267.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EBD (U+1EBD): L&lt;&lt;1055.0,1206.0&gt;--&lt;1091.0,1305.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EC4 (U+1EC4): L&lt;&lt;1148.0,2220.0&gt;--&lt;1112.0,2121.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EC4 (U+1EC4): L&lt;&lt;1440.0,2060.0&gt;--&lt;1476.0,2159.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EC5 (U+1EC5): L&lt;&lt;970.0,1731.0&gt;--&lt;934.0,1632.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EC5 (U+1EC5): L&lt;&lt;1262.0,1571.0&gt;--&lt;1298.0,1670.0&gt;&gt; has the same coordinates as a previous segment.

* uni1ECB_uni0303: L&lt;&lt;709.0,1242.0&gt;--&lt;673.0,1143.0&gt;&gt; has the same coordinates as a previous segment.

* uni1ECB_uni0303: L&lt;&lt;1001.0,1082.0&gt;--&lt;1037.0,1181.0&gt;&gt; has the same coordinates as a previous segment.

* uni1ED6 (U+1ED6): L&lt;&lt;1191.0,2205.0&gt;--&lt;1155.0,2106.0&gt;&gt; has the same coordinates as a previous segment.

* uni1ED6 (U+1ED6): L&lt;&lt;1483.0,2045.0&gt;--&lt;1519.0,2144.0&gt;&gt; has the same coordinates as a previous segment.

* uni1ED7 (U+1ED7): L&lt;&lt;933.0,1597.0&gt;--&lt;897.0,1498.0&gt;&gt; has the same coordinates as a previous segment.

* uni1ED7 (U+1ED7): L&lt;&lt;1225.0,1437.0&gt;--&lt;1261.0,1536.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EE0 (U+1EE0): L&lt;&lt;855.0,1847.0&gt;--&lt;819.0,1748.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EE0 (U+1EE0): L&lt;&lt;1147.0,1687.0&gt;--&lt;1183.0,1786.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EE1 (U+1EE1): L&lt;&lt;715.0,1347.0&gt;--&lt;679.0,1248.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EE1 (U+1EE1): L&lt;&lt;1007.0,1187.0&gt;--&lt;1043.0,1286.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EEE (U+1EEE): L&lt;&lt;1176.0,1855.0&gt;--&lt;1140.0,1756.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EEE (U+1EEE): L&lt;&lt;1468.0,1695.0&gt;--&lt;1504.0,1794.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EEF (U+1EEF): L&lt;&lt;691.0,1404.0&gt;--&lt;655.0,1305.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EEF (U+1EEF): L&lt;&lt;983.0,1244.0&gt;--&lt;1019.0,1343.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EF8 (U+1EF8): L&lt;&lt;917.0,1848.0&gt;--&lt;881.0,1749.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EF8 (U+1EF8): L&lt;&lt;1209.0,1688.0&gt;--&lt;1245.0,1787.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EF9 (U+1EF9): L&lt;&lt;742.0,1355.0&gt;--&lt;706.0,1256.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EF9 (U+1EF9): L&lt;&lt;1034.0,1195.0&gt;--&lt;1070.0,1294.0&gt;&gt; has the same coordinates as a previous segment.

* uni207D (U+207D): L&lt;&lt;687.0,771.0&gt;--&lt;794.0,771.0&gt;&gt; has the same coordinates as a previous segment.

* uni207E (U+207E): L&lt;&lt;1058.0,1243.0&gt;--&lt;951.0,1243.0&gt;&gt; has the same coordinates as a previous segment.

* uni207E (U+207E): L&lt;&lt;778.0,769.0&gt;--&lt;885.0,769.0&gt;&gt; has the same coordinates as a previous segment.

* uni208D (U+208D): L&lt;&lt;323.0,-229.0&gt;--&lt;430.0,-229.0&gt;&gt; has the same coordinates as a previous segment.

* uni208E (U+208E): L&lt;&lt;694.0,243.0&gt;--&lt;587.0,243.0&gt;&gt; has the same coordinates as a previous segment.

* uni208E (U+208E): L&lt;&lt;414.0,-231.0&gt;--&lt;521.0,-231.0&gt;&gt; has the same coordinates as a previous segment.

* uni20BF (U+20BF): L&lt;&lt;1119.0,1023.0&gt;--&lt;1045.0,820.0&gt;&gt; has the same coordinates as a previous segment.

* uni20BF (U+20BF): L&lt;&lt;1035.0,766.0&gt;--&lt;962.0,567.0&gt;&gt; has the same coordinates as a previous segment.

* uni20BF (U+20BF): L&lt;&lt;1306.0,1537.0&gt;--&lt;1232.0,1331.0&gt;&gt; has the same coordinates as a previous segment.

* uni2116 (U+2116): L&lt;&lt;562.0,0.0&gt;--&lt;461.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni27E9 (U+27E9): L&lt;&lt;902.0,741.0&gt;--&lt;902.0,569.0&gt;&gt; has the same coordinates as a previous segment.

* utilde (U+0169): L&lt;&lt;678.0,1332.0&gt;--&lt;642.0,1233.0&gt;&gt; has the same coordinates as a previous segment.

* utilde (U+0169): L&lt;&lt;970.0,1172.0&gt;--&lt;1006.0,1271.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- L_periodcentered.loclCAT

- brevecomb_acutecomb

- brevecomb_gravecomb

- brevecomb_hookabovecomb

- brevecomb_tildecomb

- circumflexcomb_acutecomb

- circumflexcomb_gravecomb

- circumflexcomb_hookabovecomb

- circumflexcomb_tildecomb

- idotaccent

- l_periodcentered.loclCAT
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, coptic, cherokee, tifinagh</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: gothic, glagolitic, elbasan, math, coptic</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: duployan, canadian-aboriginal, math, malayalam, hebrew, old-permic, syriac, coptic, todhri, tai-le, tifinagh</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+030D COMBINING VERTICAL LINE ABOVE: try adding sunuwar</li>
<li>U+030F COMBINING DOUBLE GRAVE ACCENT: not included in any glyphset definition</li>
<li>U+0310 COMBINING CANDRABINDU: try adding one of: math, sunuwar</li>
<li>U+0311 COMBINING INVERTED BREVE: try adding one of: coptic, todhri</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: duployan, cherokee, syriac</li>
<li>U+0325 COMBINING RING BELOW: try adding syriac</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: gothic, thai, cherokee, syriac, caucasian-albanian, sunuwar, tifinagh</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+035F COMBINING DOUBLE MACRON BELOW: not included in any glyphset definition</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
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
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: yi, math, symbols, tai-tham</li>
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
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>devanagari</code>, <code>greek</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-dotted">soft_dotted</a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: i̍ i̐ ɨ̀ ɨ́ ɨ̂ ɨ̃ ɨ̄ ɨ̈ ɨ̋ ɨ̌ ɨ̏ ɨ̧̀ ɨ̧́ ɨ̧̂ ɨ̧̌ ɨ̱̀ ɨ̱́ ɨ̱̈</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̅ i̇ i̒ i̛̅ i̛̇ i̛̊ i̛̋ i̛̍ i̛̐ i̛̒ i̤̅ i̤̇ i̤̊ i̤̋ i̤̍ i̤̐ i̤̒ i̥̅ i̥̇ i̥̊</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Bafut (Latn, 158,146 speakers), Northern Tutchone (Latn, 85 speakers), Heiltsuk (Latn, 300 speakers), Makaa (Latn, 221,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Ekpeye (Latn, 226,000 speakers), Dan (Latn, 1,099,244 speakers), Mundani (Latn, 34,000 speakers), Avokaya (Latn, 100,000 speakers), Ebira (Latn, 2,200,000 speakers), Western Krahn (Latn, 97,800 speakers), Aghem (Latn, 38,843 speakers), Kom (Latn, 360,685 speakers), Longto (Latn, 5,000 speakers), Abua (Latn, 25,000 speakers), Keliko (Latn, 63,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Southern Kisi (Latn, 360,000 speakers), Dii (Latn, 71,000 speakers), Han (Latn, 6 speakers), Belarusian (Cyrl, 10,064,517 speakers), Zapotec (Latn, 490,000 speakers), Vute (Latn, 21,000 speakers), Ma’di (Latn, 584,000 speakers), Nateni (Latn, 100,000 speakers), South Central Banda (Latn, 244,000 speakers), Ikwere (Latn, 717,000 speakers), Southern Tutchone (Latn, 65 speakers), Kaska (Latn, 125 speakers), Koonzime (Latn, 40,000 speakers), Yala (Latn, 200,000 speakers), Teke-Ebo (Latn, 260,000 speakers), Mango (Latn, 77,000 speakers), Cicipu (Latn, 44,000 speakers), Gulay (Latn, 250,478 speakers), Ngbaka (Latn, 1,020,000 speakers), Basaa (Latn, 332,940 speakers), Fur (Latn, 1,230,163 speakers), Lugbara (Latn, 2,200,000 speakers), Mfumte (Latn, 79,000 speakers), Sar (Latn, 500,000 speakers), Ejagham (Latn, 120,000 speakers), Navajo (Latn, 166,319 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Igbo (Latn, 27,823,640 speakers), Nzakara (Latn, 50,000 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-alignment-miss">outline_alignment_miss</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have on-curve points which have potentially incorrect y coordinates:</p>
<pre><code>* Ccedilla (U+00C7): X=268.0,Y=-2.0 (should be at baseline 0?)

* Ccedilla (U+00C7): X=68.0,Y=-2.0 (should be at baseline 0?)

* Ccedilla (U+00C7): X=948.0,Y=-2.0 (should be at baseline 0?)

* Ccedilla (U+00C7): X=153.0,Y=-2.0 (should be at baseline 0?)

* Chook (U+0187): X=622.0,Y=1550.0 (should be at cap-height 1548?)

* Chook (U+0187): X=822.0,Y=1550.0 (should be at cap-height 1548?)

* Chook (U+0187): X=622.0,Y=1550.0 (should be at cap-height 1548?)

* Chook (U+0187): X=721.0,Y=1550.0 (should be at cap-height 1548?)

* Chook (U+0187): X=1504.0,Y=1550.0 (should be at cap-height 1548?)

* Chook (U+0187): X=721.0,Y=1550.0 (should be at cap-height 1548?)

* Eopen (U+0190): X=296.0,Y=1.0 (should be at baseline 0?)

* Eopen (U+0190): X=97.0,Y=2.0 (should be at baseline 0?)

* beta (U+03B2): X=472.0,Y=1547.0 (should be at cap-height 1548?)

* beta (U+03B2): X=472.0,Y=1547.0 (should be at cap-height 1548?)

* beta (U+03B2): X=732.0,Y=2.0 (should be at baseline 0?)

* beta (U+03B2): X=532.0,Y=2.0 (should be at baseline 0?)

* beta (U+03B2): X=732.0,Y=2.0 (should be at baseline 0?)

* beta (U+03B2): X=201.0,Y=2.0 (should be at baseline 0?)

* dblverticalbar (U+2016): X=307.0,Y=-1.0 (should be at baseline 0?)

* dblverticalbar (U+2016): X=104.0,Y=-1.0 (should be at baseline 0?)

* eopen (U+025B): X=296.0,Y=1.0 (should be at baseline 0?)

* eopen (U+025B): X=97.0,Y=2.0 (should be at baseline 0?)

* epsilon (U+03B5): X=296.0,Y=1.0 (should be at baseline 0?)

* epsilon (U+03B5): X=97.0,Y=2.0 (should be at baseline 0?)

* epsilontonos (U+03AD): X=296.0,Y=1.0 (should be at baseline 0?)

* epsilontonos (U+03AD): X=97.0,Y=2.0 (should be at baseline 0?)

* iotadieresistonos (U+0390): X=805.0,Y=2.0 (should be at baseline 0?)

* kaiSymbol (U+03D7): X=970.0,Y=-2.0 (should be at baseline 0?)

* kappa (U+03BA): X=307.0,Y=1.0 (should be at baseline 0?)

* kappa (U+03BA): X=107.0,Y=1.0 (should be at baseline 0?)

* literSign (U+2113): X=835.0,Y=1549.0 (should be at cap-height 1548?)

* literSign (U+2113): X=835.0,Y=1549.0 (should be at cap-height 1548?)

* omega (U+03C9): X=153.0,Y=2.0 (should be at baseline 0?)

* omega (U+03C9): X=972.0,Y=2.0 (should be at baseline 0?)

* omegatonos (U+03CE): X=153.0,Y=2.0 (should be at baseline 0?)

* omegatonos (U+03CE): X=972.0,Y=2.0 (should be at baseline 0?)

* ringhalfleft (U+02BF): X=435.0,Y=1547.0 (should be at cap-height 1548?)

* ringhalfleft (U+02BF): X=435.0,Y=1547.0 (should be at cap-height 1548?)

* uni01C5 (U+01C5): X=563.0,Y=1547.0 (should be at cap-height 1548?)

* uni01C5 (U+01C5): X=664.0,Y=1547.0 (should be at cap-height 1548?)

* uni01C5 (U+01C5): X=382.0,Y=-1.0 (should be at baseline 0?)

* uni01C5 (U+01C5): X=281.0,Y=-1.0 (should be at baseline 0?)

* uni01C5 (U+01C5): X=563.0,Y=1547.0 (should be at cap-height 1548?)

* uni01C5 (U+01C5): X=726.0,Y=1547.0 (should be at cap-height 1548?)

* uni01C5 (U+01C5): X=726.0,Y=1547.0 (should be at cap-height 1548?)

* uni01C5 (U+01C5): X=448.0,Y=-1.0 (should be at baseline 0?)

* uni01C5 (U+01C5): X=645.0,Y=1547.0 (should be at cap-height 1548?)

* uni01C5 (U+01C5): X=726.0,Y=1547.0 (should be at cap-height 1548?)

* uni01C5 (U+01C5): X=645.0,Y=1547.0 (should be at cap-height 1548?)

* uni01C5 (U+01C5): X=448.0,Y=-1.0 (should be at baseline 0?)

* uni01C5 (U+01C5): X=367.0,Y=-1.0 (should be at baseline 0?)

* uni0930_uni094D.blwf: X=-384.0,Y=-614.0 (should be at descender -615?)

* uni0930_uni094D.blwf: X=-605.0,Y=-614.0 (should be at descender -615?)

* uni1E08 (U+1E08): X=268.0,Y=-2.0 (should be at baseline 0?)

* uni1E08 (U+1E08): X=68.0,Y=-2.0 (should be at baseline 0?)

* uni1E08 (U+1E08): X=948.0,Y=-2.0 (should be at baseline 0?)

* uni1E08 (U+1E08): X=153.0,Y=-2.0 (should be at baseline 0?)

* uniFB02 (U+FB02): X=520.0,Y=1547.0 (should be at cap-height 1548?)

* uniFB02 (U+FB02): X=720.0,Y=1547.0 (should be at cap-height 1548?)

* uniFB02 (U+FB02): X=520.0,Y=1547.0 (should be at cap-height 1548?)

* uniFB02 (U+FB02): X=521.0,Y=1547.0 (should be at cap-height 1548?)

* uniFB02 (U+FB02): X=948.0,Y=1547.0 (should be at cap-height 1548?)

* uniFB02 (U+FB02): X=521.0,Y=1547.0 (should be at cap-height 1548?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-direction">outline_direction</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* hryvnia (U+20B4) has a counter-clockwise outer contour

* hryvnia (U+20B4) has a counter-clockwise outer contour

* lambda (U+03BB) has a counter-clockwise outer contour

* lambda (U+03BB) has a counter-clockwise outer contour
</code></pre>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> List all superfamily filepaths <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#superfamily-list">superfamily/list</a></summary>
    <div>







* ℹ️ **INFO** <p>fonts/variable</p>
 [code: family-path]



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> Show hinting filesize impact. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#hinting-impact">hinting_impact</a></summary>
    <div>







* ℹ️ **INFO** <p>Hinting filesize impact:</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">fonts/variable/Samaano-Italic[wdth,wght].ttf</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Dehinted Size</td>
<td align="right">232.0kb</td>
</tr>
<tr>
<td align="left">Hinted Size</td>
<td align="right">232.0kb</td>
</tr>
<tr>
<td align="left">Increase</td>
<td align="right">24 bytes</td>
</tr>
<tr>
<td align="left">Change</td>
<td align="right">0.0 %</td>
</tr>
</tbody>
</table>
 [code: size-impact]



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> Font contains all required tables? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#required-tables">required_tables</a></summary>
    <div>







* ℹ️ **INFO** <p>This font contains the following optional tables:</p>
<pre><code>- loca

- prep

- GPOS

- GSUB

- gasp
</code></pre>
 [code: optional-tables]



* ✅ **PASS** <p>Font contains all required tables.</p>
 



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> Check for presence of an ARTICLE.en_us.html file <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-has-article">googlefonts/description/has_article</a></summary>
    <div>







* ℹ️ **INFO** <p>This font doesn't have an ARTICLE.en_us.html file.</p>
 [code: missing-article]



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-gasp">googlefonts/gasp</a></summary>
    <div>







* ℹ️ **INFO** <p>These are the ppm ranges declared on the gasp table:</p>
<p>PPM &lt;= 65535:
flag = 0x0F
- Use grid-fitting
- Use grayscale rendering
- Use gridfitting with ClearType symmetric smoothing
- Use smoothing along multiple axes with ClearType®</p>
 [code: ranges]



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-meta-script-lang-tags">googlefonts/meta/script_lang_tags</a></summary>
    <div>







* ℹ️ **INFO** <p>Latn</p>
 [code: dlng-tag]



* ℹ️ **INFO** <p>Latn,Deva,Grek</p>
 [code: slng-tag]



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> Font has old ttfautohint applied? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-old-ttfautohint">googlefonts/old_ttfautohint</a></summary>
    <div>







* ℹ️ **INFO** <p>Could not detect which version of ttfautohint was used in this font. It is typically specified as a comment in the font version entries of the 'name' table. Such font version strings are currently: ['Version 2.300']</p>
 [code: version-not-detected]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check hhea.caretSlopeRise and hhea.caretSlopeRun <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-caret-slope">opentype/caret_slope</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check code page character ranges <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-code-pages">opentype/code_pages</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Font follows the family naming recommendations? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-family-naming-recommendations">opentype/family_naming_recommendations</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking font version fields (head and name table). <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-font-version">opentype/font_version</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking OS/2 fsSelection value. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-fsselection">opentype/fsselection</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Axes and named instances fall within correct ranges? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-fvar-axis-ranges-correct">opentype/fvar/axis_ranges_correct</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Axes and named instances fall within correct ranges? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-fvar-regular-coords-correct">opentype/fvar/regular_coords_correct</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check glyphs do not have duplicate components which have the same x,y coordinates. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-glyf-non-transformed-duplicate-components">opentype/glyf_non_transformed_duplicate_components</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Is there any unused data at the end of the glyf table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-glyf-unused-data">opentype/glyf_unused_data</a></summary>
    <div>







* ✅ **PASS** <p>There is no unused data at the end of the glyf table.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking post.italicAngle value. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-italic-angle">opentype/italic_angle</a></summary>
    <div>







* ✅ **PASS** <p>Value of post.italicAngle is -19.989837646484375 with style=&quot;BoldItalic&quot;.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Is there a usable "kern" table declared in the font? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-kern-table">opentype/kern_table</a></summary>
    <div>







* ✅ **PASS** <p>Font does not declare an optional &quot;kern&quot; table.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does the font have any invalid feature tags? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-layout-valid-feature-tags">opentype/layout_valid_feature_tags</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does the font have any invalid language tags? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-layout-valid-language-tags">opentype/layout_valid_language_tags</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does the font have any invalid script tags? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-layout-valid-script-tags">opentype/layout_valid_script_tags</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does the number of glyphs in the loca table match the maxp table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-loca-maxp-num-glyphs">opentype/loca/maxp_num_glyphs</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking head.macStyle value. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-mac-style">opentype/mac_style</a></summary>
    <div>







* ✅ **PASS** <p>head macStyle ITALIC bit is properly set.</p>
 



* ✅ **PASS** <p>head macStyle BOLD bit is properly set.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> MaxAdvanceWidth is consistent with values in the Hmtx and Hhea tables? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-maxadvancewidth">opentype/maxadvancewidth</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check name table for empty records. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-name-empty-records">opentype/name/empty_records</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does full font name begin with the font family name? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-name-match-familyname-fullfont">opentype/name/match_familyname_fullfont</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Name table ID 6 (PostScript name) must be consistent across platforms. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-name-postscript-name-consistency">opentype/name/postscript_name_consistency</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check for points out of bounds. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-points-out-of-bounds">opentype/points_out_of_bounds</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> PostScript name follows OpenType specification requirements? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-postscript-name">opentype/postscript_name</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Font has correct post table version? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-post-table-version">opentype/post_table_version</a></summary>
    <div>







* ✅ **PASS** <p>Font has an acceptable post format 2.0 table version.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking direction of slnt axis angles. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-slant-direction">opentype/slant_direction</a></summary>
    <div>







* ✅ **PASS** <p>Font has no slnt axis</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking unitsPerEm value is reasonable. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-unitsperem">opentype/unitsperem</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Validates that all of the instance records in a given font have distinct data. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-varfont-distinct-instance-records">opentype/varfont/distinct_instance_records</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Validate foundry-defined design-variation axis tag names. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-varfont-foundry-defined-tag-name">opentype/varfont/foundry_defined_tag_name</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Validates that all of the instance records in a given font have the same size. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-varfont-same-size-instance-records">opentype/varfont/same_size_instance_records</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> All fvar axes have a correspondent Axis Record on STAT table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-varfont-STAT-axis-record-for-each-axis">opentype/varfont/STAT_axis_record_for_each_axis</a></summary>
    <div>







* ✅ **PASS** <p>STAT table has all necessary Axis Records.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Validates subfamilyNameID and postScriptNameID for the default instance record <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-varfont-valid-default-instance-nameids">opentype/varfont/valid_default_instance_nameids</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Validates that all of the name IDs in an instance record are within the correct range <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-varfont-valid-nameids">opentype/varfont/valid_nameids</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking if OS/2 usWeightClass matches fvar. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-weight-class-fvar">opentype/weight_class_fvar</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check if OS/2 xAvgCharWidth is correct. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-xavgcharwidth">opentype/xavgcharwidth</a></summary>
    <div>







* ✅ **PASS** <p>OS/2 xAvgCharWidth value is correct.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check that Arabic spacing symbols U+FBB2–FBC1 aren't classified as marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#arabic-spacing-symbols">arabic_spacing_symbols</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check if uppercase glyphs are vertically centered. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#caps-vertically-centered">caps_vertically_centered</a></summary>
    <div>







* ✅ **PASS** <p>Uppercase glyphs are vertically centered in the em box.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#case-mapping">case_mapping</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Color layers should have a minimum brightness. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#color-cpal-brightness">color_cpal_brightness</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does font file include unacceptable control character glyphs? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#control-chars">control_chars</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Put an empty glyph on GID 1 right after the .notdef glyph for COLRv0 fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#empty-glyph-on-gid1-for-colrv0">empty_glyph_on_gid1_for_colrv0</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#family-win-ascent-and-descent">family/win_ascent_and_descent</a></summary>
    <div>







* ✅ **PASS** <p>OS/2 usWinAscent &amp; usWinDescent values look good!</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> All name entries referenced by fvar instances exist on the name table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fvar-name-entries">fvar_name_entries</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure files are not too large. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#file-size">file_size</a></summary>
    <div>







* ✅ **PASS** <p>Font had a reasonable file size</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>







* ✅ **PASS** <p>Font familyname seems to be unique.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure that the font can be rasterized by FreeType. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#freetype-rasterizer">freetype_rasterizer</a></summary>
    <div>







* ✅ **PASS** <p>Font can be rasterized by FreeType.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure no GPOS7 lookups are present. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#gpos7">gpos7</a></summary>
    <div>







* ✅ **PASS** <p>Font has no GPOS7 lookups</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#gpos-kerning-info">gpos_kerning_info</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check that legacy accents aren't used in composite glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#legacy-accents">legacy_accents</a></summary>
    <div>







* ✅ **PASS** <p>Looks good!</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking Vertical Metric Linegaps. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#linegaps">linegaps</a></summary>
    <div>







* ✅ **PASS** <p>OS/2 sTypoLineGap and hhea lineGap are both 0.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Font contains '.notdef' as its first glyph? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#mandatory-glyphs">mandatory_glyphs</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>







* ✅ **PASS** <p>Looks good.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure small caps glyphs are available. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#missing-small-caps-glyphs">missing_small_caps_glyphs</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Are there disallowed characters in the NAME table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#name-char-restrictions">name/char_restrictions</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Combined length of family and style must not exceed 32 characters. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#name-family-and-style-max-length">name/family_and_style_max_length</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Name table records must not have trailing spaces. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#name-trailing-spaces">name/trailing_spaces</a></summary>
    <div>







* ✅ **PASS** <p>No trailing spaces on name table entries.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Description strings in the name table must not contain copyright info. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#name-no-copyright-on-description">name/no_copyright_on_description</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check name table IDs 1, 2, 16, 17 to conform to Italic style. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#name-italic-names">name/italic_names</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure glyphs do not have components which are themselves components. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#nested-components">nested_components</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking OS/2 Metrics match hhea Metrics. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#os2-metrics-match-hhea">os2_metrics_match_hhea</a></summary>
    <div>







* ✅ **PASS** <p>OS/2.sTypoAscender/Descender values match hhea.ascent/descent.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking with ots-sanitize. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#ots">ots</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure indic fonts have the Indian Rupee Sign glyph. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#rupee">rupee</a></summary>
    <div>







* ✅ **PASS** <p>Looks good!</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Font has the proper sfntVersion value? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#sfnt-version">sfnt_version</a></summary>
    <div>







* ✅ **PASS** <p>Font has the correct sfntVersion value.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure smart dropout control is enabled in "prep" table instructions. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#smart-dropout">smart_dropout</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>







* ✅ **PASS** <p>Looks good!</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure Stylistic Sets have description. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#stylisticset-description">stylisticset_description</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check tabular widths don't have kerning. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#tabular-kerning">tabular_kerning</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure component transforms do not perform scaling or rotation. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#transformed-components">transformed_components</a></summary>
    <div>







* ✅ **PASS** <p>No glyphs had components with scaling or rotation</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking with fontTools.ttx <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#ttx-roundtrip">ttx_roundtrip</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking that the typoAscender exceeds the yMax of the /Agrave. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#typoascender-exceeds-Agrave">typoascender_exceeds_Agrave</a></summary>
    <div>







* ✅ **PASS** <p>OS/2.sTypoAscender value is greater than the yMax of /Agrave.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Font contains unique glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unique-glyphnames">unique_glyphnames</a></summary>
    <div>







* ✅ **PASS** <p>Glyph names are all unique.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Are there unwanted Apple tables? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unwanted-aat-tables">unwanted_aat_tables</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Are there unwanted tables? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unwanted-tables">unwanted_tables</a></summary>
    <div>







* ✅ **PASS** <p>There are no unwanted tables.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#valid-glyphnames">valid_glyphnames</a></summary>
    <div>







* ✅ **PASS** <p>Glyph names are all valid.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> The variable font 'wght' (Weight) axis coordinate must be 700 on the 'Bold' instance. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#varfont-bold-wght-coord">varfont/bold_wght_coord</a></summary>
    <div>







* ✅ **PASS** <p>Bold:wght is 700.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check variable font instances don't have duplicate names <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#varfont-duplicate-instance-names">varfont/duplicate_instance_names</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure the font's instances are in the correct order. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#varfont-instances-in-order">varfont/instances_in_order</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure VFs do not contain (yet) the ital axis. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#varfont-unsupported-axes">varfont/unsupported_axes</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Font contains glyphs for whitespace characters? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#whitespace-glyphs">whitespace_glyphs</a></summary>
    <div>







* ✅ **PASS** <p>Font contains glyphs for whitespace characters.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Whitespace glyphs have ink? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#whitespace-ink">whitespace_ink</a></summary>
    <div>







* ✅ **PASS** <p>There is no whitespace glyph with ink.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Space and non-breaking space have the same width? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#whitespace-widths">whitespace_widths</a></summary>
    <div>







* ✅ **PASS** <p>Space and non-breaking space have the same width.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check name ID 25 to end with "Italic" for Italic VFs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-valid-nameid25">googlefonts/metadata/valid_nameid25</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check family name for GF Guide compliance. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-family-name-compliance">googlefonts/family_name_compliance</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Name table entries should not contain line-breaks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-line-breaks">googlefonts/name/line_breaks</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Copyright notices match canonical pattern in fonts <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-font-copyright">googlefonts/font_copyright</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check OFL body text is correct. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-license-OFL-body-text">googlefonts/license/OFL_body_text</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check license file has good copyright string. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-license-OFL-copyright">googlefonts/license/OFL_copyright</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check copyright namerecords match license file. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license">googlefonts/name/license</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> License URL matches License text on name table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license-url">googlefonts/name/license_url</a></summary>
    <div>







* ✅ **PASS** <p>Font has a valid license URL in NAME table.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Name table strings must not contain the string 'Reserved Font Name'. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-rfn">googlefonts/name/rfn</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> A font repository should not include FontBakery report files <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-repo-fb-report">googlefonts/repo/fb_report</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> A font repository should not include ZIP files <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-repo-zip-files">googlefonts/repo/zip_files</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#dotted-circle">dotted_circle</a></summary>
    <div>







* ✅ **PASS** <p>All marks were anchored to dotted circle</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Validate defaults on fvar table match registered fallback names in GFAxisRegistry. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-axisregistry-fvar-axis-defaults">googlefonts/axisregistry/fvar_axis_defaults</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking file is named canonically. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-canonical-filename">googlefonts/canonical_filename</a></summary>
    <div>







* ✅ **PASS** <p>Font filename is correct, &quot;Samaano-Italic[wdth,wght].ttf&quot;.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure font has the expected color font tables. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-colorfont-tables">googlefonts/colorfont_tables</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check font names are correct <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-font-names">googlefonts/font_names</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking OS/2 fsType does not impose restrictions. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-fstype">googlefonts/fstype</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check variable font instances <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-fvar-instances">googlefonts/fvar_instances</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check Google Fonts glyph coverage. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyph-coverage">googlefonts/glyph_coverage</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Description strings in the name table must not exceed 200 characters. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-description-max-length">googlefonts/name/description_max_length</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Make sure family name does not begin with a digit. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-familyname-first-char">googlefonts/name/familyname_first_char</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Font has all mandatory 'name' table entries? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-mandatory-entries">googlefonts/name/mandatory_entries</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Version format is correct in 'name' table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-version-format">googlefonts/name/version_format</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure font can render its own name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-render-own-name">googlefonts/render_own_name</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Stricter unitsPerEm criteria for Google Fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-unitsperem">googlefonts/unitsperem</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check a static ttf can be generated from a variable font. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-varfont-generate-static">googlefonts/varfont/generate_static</a></summary>
    <div>







* ✅ **PASS** <p>fontTools.varLib.mutator generated a static font instance</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check that variable fonts have an HVAR table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-varfont-has-HVAR">googlefonts/varfont/has_HVAR</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vendor-id">googlefonts/vendor_id</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check font follows the Google Fonts vertical metric schema <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vertical-metrics">googlefonts/vertical_metrics</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check the OS/2 usWeightClass is appropriate for the font's best SubFamily name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-weightclass">googlefonts/weightclass</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Is the CFF2 subr/gsubr call depth > 10? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-cff2-call-depth">opentype/cff2_call_depth</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_cff2</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Does the font's CFF table top dict strings fit into the ASCII range? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-cff-ascii-strings">opentype/cff_ascii_strings</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_cff</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Is the CFF subr/gsubr call depth > 10? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-cff-call-depth">opentype/cff_call_depth</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_cff</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Does the font use deprecated CFF operators or operations? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-cff-deprecated-operators">opentype/cff_deprecated_operators</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_cff</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> CFF table FontName must match name table ID 6 (PostScript name). <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-name-postscript-vs-cff">opentype/name/postscript_vs_cff</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_cff</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Checking OS/2 achVendID against configuration. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-vendor-id">opentype/vendor_id</a></summary>
    <div>







* ⏩ **SKIP** <p>Add the <code>vendor_id</code> key to a <code>fontbakery.yaml</code> file on your font project directory to enable this check.
You'll also need to use the <code>--configuration</code> flag when invoking fontbakery.</p>
 



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Each font in set of sibling families must have the same set of vertical metrics values. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#superfamily-vertical-metrics">superfamily/vertical_metrics</a></summary>
    <div>







* ⏩ **SKIP** <p>Sibling families were not detected.</p>
 



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check that glyph for U+0675 ARABIC LETTER HIGH HAMZA is not a mark. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#arabic-high-hamza">arabic_high_hamza</a></summary>
    <div>







* ⏩ **SKIP** <p>This check will only run on fonts that have both glyphs U+0621 and U+0675</p>
 [code: glyphs-missing]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Does the font contain chws and vchw features? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#cjk-chws-feature">cjk_chws_feature</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_cjk_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Any CJK font should contain at least a minimal set of 150 CJK characters. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#cjk-not-enough-glyphs">cjk_not_enough_glyphs</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_claiming_to_be_cjk_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: not is_variable_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> PPEM must be an integer on hinted fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#integer-ppem-if-hinted">integer_ppem_if_hinted</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_hinted</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Ensure 'smcp' (small caps) lookups are defined before ligature lookups in the 'GSUB' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#smallcaps-before-ligatures">smallcaps_before_ligatures</a></summary>
    <div>







* ⏩ **SKIP** <p>Font lacks 'smcp' or 'liga' features.</p>
 



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Checking STAT table entries in static fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#STAT-in-statics">STAT_in_statics</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: not is_variable_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Ensure VFs with duplexed axes do not vary horizontal advance. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#varfont-duplexed-axis-reflow">varfont/duplexed_axis_reflow</a></summary>
    <div>







* ⏩ **SKIP** <p>This font has no duplexed axes</p>
 [code: no-relevant-axes]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Validate METADATA.pb axes values are within gf_axisregistry bounds. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-axisregistry-bounds">googlefonts/metadata/axisregistry_bounds</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Validate METADATA.pb axes tags are defined in gf_axisregistry. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-axisregistry-valid-tags">googlefonts/metadata/axisregistry_valid_tags</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Does METADATA.pb copyright field contain broken links? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-broken-links">googlefonts/metadata/broken_links</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Font styles are named canonically? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-canonical-style-names">googlefonts/metadata/canonical_style_names</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Check that font weight has a canonical value. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-canonical-weight-value">googlefonts/metadata/canonical_weight_value</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check samples can be rendered. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-can-render-samples">googlefonts/metadata/can_render_samples</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Ensure METADATA.pb category field is valid. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-category">googlefonts/metadata/category</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check if category on METADATA.pb matches what can be inferred from the family name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-category-hints">googlefonts/metadata/category_hints</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Validate VF axes match the ones declared on METADATA.pb. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-consistent-axis-enumeration">googlefonts/metadata/consistent_axis_enumeration</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Check URL on copyright string is the same as in repository_url field. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-consistent-repo-urls">googlefonts/metadata/consistent_repo_urls</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Validate 'date_added' field on METADATA.pb. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-date-added">googlefonts/metadata/date_added</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Designers are listed correctly on the Google Fonts catalog? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-designer-profiles">googlefonts/metadata/designer_profiles</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Multiple values in font designer field in METADATA.pb must be separated by commas. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-designer-values">googlefonts/metadata/designer_values</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> At least one designer is declared in METADATA.pb <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-empty-designer">googlefonts/metadata/empty_designer</a></summary>
    <div>







* ⏩ **SKIP** <p>No applicable arguments</p>
 [code: no-arguments]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Ensure METADATA.pb does not use escaped strings. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-escaped-strings">googlefonts/metadata/escaped_strings</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: metadata_file</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check font family directory name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-family-directory-name">googlefonts/metadata/family_directory_name</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check that METADATA.pb family values are all the same. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-familyname">googlefonts/metadata/familyname</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Font filenames match font.filename entries? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-filenames">googlefonts/metadata/filenames</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Ensure there is a regular style defined in METADATA.pb. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-has-regular">googlefonts/metadata/has_regular</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check METADATA.pb includes production subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-includes-production-subsets">googlefonts/metadata/includes_production_subsets</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata, listed_on_gfonts_api</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb font.filename and font.post_script_name fields have equivalent values? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-match-filename-postscript">googlefonts/metadata/match_filename_postscript</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata, not is_variable_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb font.full_name and font.post_script_name fields have equivalent values ? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-match-fullname-postscript">googlefonts/metadata/match_fullname_postscript</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Check font name is the same as family name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-match-name-familyname">googlefonts/metadata/match_name_familyname</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata, font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb weight matches postScriptName for static fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-match-weight-postscript">googlefonts/metadata/match_weight_postscript</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata, not is_variable_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb should contain at least "menu" and "latin" subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-menu-and-latin">googlefonts/metadata/menu_and_latin</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Validate family.minisite_url field. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-minisite-url">googlefonts/metadata/minisite_url</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb font.name and font.full_name fields match the values declared on the name table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-nameid-family-and-full-names">googlefonts/metadata/nameid/family_and_full_names</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb font.name value should be same as the family name declared on the name table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-nameid-font-name">googlefonts/metadata/nameid/font_name</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Checks METADATA.pb font.post_script_name matches postscript name declared on the name table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-nameid-post-script-name">googlefonts/metadata/nameid/post_script_name</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check METADATA.pb parse correctly. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-parses">googlefonts/metadata/parses</a></summary>
    <div>







* ⏩ **SKIP** <p>Font family at 'fonts/variable' lacks a METADATA.pb file.</p>
 [code: file-not-found]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Check for primary_script <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-primary-script">googlefonts/metadata/primary_script</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Regular should be 400. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-regular-is-400">googlefonts/metadata/regular_is_400</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata, has_regular_style</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check METADATA.pb file only contains a single CJK subset. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-single-cjk-subset">googlefonts/metadata/single_cjk_subset</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb subsets should be alphabetically ordered. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-subsets-order">googlefonts/metadata/subsets_order</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Ensure METADATA.pb lists all font binaries. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-undeclared-fonts">googlefonts/metadata/undeclared_fonts</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: check if fonts field only has unique "full_name" values. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unique-full-name-values">googlefonts/metadata/unique_full_name_values</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: check if fonts field only contains unique style:weight pairs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unique-weight-style-pairs">googlefonts/metadata/unique_weight_style_pairs</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check for METADATA subsets with zero support. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unsupported-subsets">googlefonts/metadata/unsupported_subsets</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb font.filename field contains font name in right format? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-valid-filename-values">googlefonts/metadata/valid_filename_values</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb font.full_name field contains font name in right format? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-valid-full-name-values">googlefonts/metadata/valid_full_name_values</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb font.post_script_name field contains font name in right format? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-valid-post-script-name-values">googlefonts/metadata/valid_post_script_name_values</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check METADATA.pb font weights are correct. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-weightclass">googlefonts/metadata/weightclass</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Does DESCRIPTION file contain broken links? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-broken-links">googlefonts/description/broken_links</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: description_and_article_html</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> DESCRIPTION.en_us.html should end in a linebreak. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-eof-linebreak">googlefonts/description/eof_linebreak</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: description</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> On a family update, the DESCRIPTION.en_us.html file should ideally also be updated. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-family-update">googlefonts/description/family_update</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: description</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Does DESCRIPTION file contain a upstream Git repo URL? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-git-url">googlefonts/description/git_url</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: description_html</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check the description doesn't contain unsupported html elements <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-has-unsupported-elements">googlefonts/description/has_unsupported_elements</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: description_and_article</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> DESCRIPTION.en_us.html must have more than 200 bytes. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-min-length">googlefonts/description/min_length</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: description</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> URLs on DESCRIPTION file must not display http(s) prefix. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-urls">googlefonts/description/urls</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: description_and_article_html</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Is this a proper HTML snippet? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-valid-html">googlefonts/description/valid_html</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: description_and_article</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check font has a license. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-family-has-license">googlefonts/family/has_license</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: gfonts_repo_structure</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Copyright notice is the same in all fonts? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-copyright">googlefonts/metadata/copyright</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb license is "APACHE2", "UFL" or "OFL"? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-license">googlefonts/metadata/license</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Copyright notice on METADATA.pb should not contain 'Reserved Font Name'. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-reserved-font-name">googlefonts/metadata/reserved_font_name</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check upstream.yaml file contains all required fields <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-repo-upstream-yaml-has-required-fields">googlefonts/repo/upstream_yaml_has_required_fields</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: upstream_yaml</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> A static fonts directory, if present, must contain manually hinted fonts <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-repo-vf-has-static-fonts">googlefonts/repo/vf_has_static_fonts</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: gfonts_repo_structure</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check that no collisions are found while shaping <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#shaping-collides">shaping/collides</a></summary>
    <div>







* ⏩ **SKIP** <p>Shaping test directory not defined in configuration file</p>
 



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check that no forbidden glyphs are found while shaping <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#shaping-forbidden">shaping/forbidden</a></summary>
    <div>







* ⏩ **SKIP** <p>Shaping test directory not defined in configuration file</p>
 



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check that texts shape as per expectation <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#shaping-regression">shaping/regression</a></summary>
    <div>







* ⏩ **SKIP** <p>Shaping test directory not defined in configuration file</p>
 



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-colinear-vectors">outline_colinear_vectors</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: not is_variable_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-jaggy-segments">outline_jaggy_segments</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: not is_variable_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-semi-vertical">outline_semi_vertical</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: not is_variable_font, not is_italic</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Are any segments inordinately short? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-short-segments">outline_short_segments</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: not is_variable_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check if the axes match between the font and the Google Fonts version. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-axes-match">googlefonts/axes_match</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: remote_style</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check font follows the Google Fonts CJK vertical metric schema <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-cjk-vertical-metrics">googlefonts/cjk_vertical_metrics</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_cjk_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check if the vertical metrics of a CJK family are similar to the same family hosted on Google Fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-cjk-vertical-metrics-regressions">googlefonts/cjk_vertical_metrics_regressions</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_cjk_font, regular_remote_style</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Font has ttfautohint params? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-has-ttfautohint-params">googlefonts/has_ttfautohint_params</a></summary>
    <div>







* ⏩ **SKIP** <p>Font appears to our heuristic as not hinted using ttfautohint.</p>
 [code: not-hinted]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vertical-metrics-regressions">googlefonts/vertical_metrics_regressions</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: regular_remote_style</p>
 [code: unfulfilled-conditions]



</div>
</details>
</div>
</details>

<details><summary>[218] Samaano[wdth,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Do we have the latest version of FontBakery installed? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontbakery-version">fontbakery_version</a></summary>
    <div>







* 🔥 **FAIL** <p>Current FontBakery version is 0.13.1, while a newer 0.13.2 is already available. Please upgrade it with 'pip install -U fontbakery'</p>
 [code: outdated-fontbakery]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">FAIL messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1ECA</td>
<td align="left">ig_Latn (Igbo)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1ECA</td>
<td align="left">ig_Latn (Igbo)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1ECD</td>
<td align="left">ig_Latn (Igbo) and yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1ECC</td>
<td align="left">ig_Latn (Igbo) and yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1ECD</td>
<td align="left">ig_Latn (Igbo) and yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1ECC</td>
<td align="left">ig_Latn (Igbo) and yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1EE5</td>
<td align="left">ig_Latn (Igbo)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1EE4</td>
<td align="left">ig_Latn (Igbo)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1EE5</td>
<td align="left">ig_Latn (Igbo)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1EE4</td>
<td align="left">ig_Latn (Igbo)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1EB9</td>
<td align="left">yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1EB8</td>
<td align="left">yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1EB9</td>
<td align="left">yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1EB8</td>
<td align="left">yo_Latn (Yoruba)</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* ⚠️ **WARN** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">WARN messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Some auxiliary glyphs were missing: ἀ, ἁ, ἂ, ἃ, ἄ, ἅ, ἆ, ἇ, ἐ, ἑ, ἒ, ἓ, ἔ, ἕ, ἠ, ἡ, ἢ, ἣ, ἤ, ἥ, ἦ, ἧ, ἰ, ἱ, ἲ, ἳ, ἴ, ἵ, ἶ, ἷ, ὂ, ὃ, ὄ, ὐ, ὑ, ὒ, ὓ, ὔ, ὕ, ὖ, ὗ, ὢ, ὣ, ὤ, ὥ, ὦ, ὧ, ᾶ, ῆ, ῖ, ῗ, ῦ, ῧ, ῶ</td>
<td align="left">el_Grek (Greek)</td>
</tr>
<tr>
<td align="left">No variant glyphs were found for Eng</td>
<td align="left">bm_Latn (Bambara), dyu_Latn (Dyula), ig_Latn (Igbo) and lg_Latn (Ganda)</td>
</tr>
<tr>
<td align="left">Some auxiliary glyphs were missing: Ɵ, ɵ</td>
<td align="left">ig_Latn (Igbo)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-mark-chars">opentype/gdef_mark_chars</a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
uni0955 (U+0955)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check GDEF mark glyph class doesn't have characters that are not marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-non-mark-chars">opentype/gdef_non_mark_chars</a></summary>
    <div>







* ⚠️ **WARN** <p>The following non-mark characters should not be in the GDEF mark glyph class:
U+0384</p>
 [code: non-mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check glyphs in mark glyph class are non-spacing. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-spacing-marks">opentype/gdef_spacing_marks</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs seem to be spacing (because they have width &gt; 0 on the hmtx table) so they may be in the GDEF mark glyph class by mistake, or they should have zero width instead:
tonos (U+0384)</p>
 [code: spacing-mark-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>







* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1188 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#alt-caron">alt_caron</a></summary>
    <div>







* ✅ **PASS** <p>Looks good!</p>
 



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
    <summary>⚠️ <b>WARN</b> Detect any interpolation issues in the font. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#interpolation-issues">interpolation_issues</a></summary>
    <div>







* ⚠️ **WARN** <p>Interpolation issues were found in the font:</p>
<pre><code>- Contour 0 in glyph 'Uhorn': becomes underweight between wdth=100,wght=100 and wdth=200,wght=100.

- Contour 1 in glyph 'Uhorn': becomes underweight between wdth=100,wght=100 and wdth=200,wght=100.
</code></pre>
 [code: interpolation-issues]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#ligature-carets">ligature_carets</a></summary>
    <div>







* ⚠️ **WARN** <p>This font lacks caret positioning values for these ligature glyphs:
- Ldot</p>
<pre><code>- j_uni0308

- j_uni0311

- ldot

- uni1ECB_uni0301
</code></pre>
 [code: incomplete-caret-pos-data]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure variable fonts include an avar table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#mandatory-avar-table">mandatory_avar_table</a></summary>
    <div>







* ⚠️ **WARN** <p>This variable font does not have an avar table. Most variable fonts should include an avar table to correctly define axes progression rates.</p>
 [code: missing-avar]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* Abreve (U+0102): L&lt;&lt;710.0,1769.0&gt;--&lt;710.0,1656.0&gt;&gt; has the same coordinates as a previous segment.

* Abreve (U+0102): L&lt;&lt;386.0,1769.0&gt;--&lt;386.0,1656.0&gt;&gt; has the same coordinates as a previous segment.

* Atilde (U+00C3): L&lt;&lt;337.0,1857.0&gt;--&lt;337.0,1758.0&gt;&gt; has the same coordinates as a previous segment.

* Atilde (U+00C3): L&lt;&lt;687.0,1697.0&gt;--&lt;687.0,1796.0&gt;&gt; has the same coordinates as a previous segment.

* B (U+0042): L&lt;&lt;433.0,1023.0&gt;--&lt;433.0,820.0&gt;&gt; has the same coordinates as a previous segment.

* B (U+0042): L&lt;&lt;442.0,766.0&gt;--&lt;442.0,567.0&gt;&gt; has the same coordinates as a previous segment.

* B (U+0042): L&lt;&lt;433.0,1537.0&gt;--&lt;433.0,1331.0&gt;&gt; has the same coordinates as a previous segment.

* Bdotbelow (U+1E04): L&lt;&lt;433.0,1023.0&gt;--&lt;433.0,820.0&gt;&gt; has the same coordinates as a previous segment.

* Bdotbelow (U+1E04): L&lt;&lt;442.0,766.0&gt;--&lt;442.0,567.0&gt;&gt; has the same coordinates as a previous segment.

* Bdotbelow (U+1E04): L&lt;&lt;433.0,1537.0&gt;--&lt;433.0,1331.0&gt;&gt; has the same coordinates as a previous segment.

* Beta (U+0392): L&lt;&lt;433.0,1023.0&gt;--&lt;433.0,820.0&gt;&gt; has the same coordinates as a previous segment.

* Beta (U+0392): L&lt;&lt;442.0,766.0&gt;--&lt;442.0,567.0&gt;&gt; has the same coordinates as a previous segment.

* Beta (U+0392): L&lt;&lt;433.0,1537.0&gt;--&lt;433.0,1331.0&gt;&gt; has the same coordinates as a previous segment.

* Bhook (U+0181): L&lt;&lt;433.0,1023.0&gt;--&lt;433.0,820.0&gt;&gt; has the same coordinates as a previous segment.

* Bhook (U+0181): L&lt;&lt;442.0,766.0&gt;--&lt;442.0,567.0&gt;&gt; has the same coordinates as a previous segment.

* Bhook (U+0181): L&lt;&lt;433.0,1537.0&gt;--&lt;433.0,1331.0&gt;&gt; has the same coordinates as a previous segment.

* Blinebelow (U+1E06): L&lt;&lt;433.0,1023.0&gt;--&lt;433.0,820.0&gt;&gt; has the same coordinates as a previous segment.

* Blinebelow (U+1E06): L&lt;&lt;442.0,766.0&gt;--&lt;442.0,567.0&gt;&gt; has the same coordinates as a previous segment.

* Blinebelow (U+1E06): L&lt;&lt;433.0,1537.0&gt;--&lt;433.0,1331.0&gt;&gt; has the same coordinates as a previous segment.

* Ebreve (U+0114): L&lt;&lt;655.0,1769.0&gt;--&lt;655.0,1656.0&gt;&gt; has the same coordinates as a previous segment.

* Ebreve (U+0114): L&lt;&lt;331.0,1769.0&gt;--&lt;331.0,1656.0&gt;&gt; has the same coordinates as a previous segment.

* Ecedillabreve (U+1E1C): L&lt;&lt;655.0,1769.0&gt;--&lt;655.0,1656.0&gt;&gt; has the same coordinates as a previous segment.

* Ecedillabreve (U+1E1C): L&lt;&lt;331.0,1769.0&gt;--&lt;331.0,1656.0&gt;&gt; has the same coordinates as a previous segment.

* Euro (U+20AC): L&lt;&lt;324.0,179.0&gt;--&lt;514.0,179.0&gt;&gt; has the same coordinates as a previous segment.

* Gbreve (U+011E): L&lt;&lt;687.0,1777.0&gt;--&lt;687.0,1664.0&gt;&gt; has the same coordinates as a previous segment.

* Gbreve (U+011E): L&lt;&lt;363.0,1777.0&gt;--&lt;363.0,1664.0&gt;&gt; has the same coordinates as a previous segment.

* Ibreve (U+012C): L&lt;&lt;655.0,1769.0&gt;--&lt;655.0,1656.0&gt;&gt; has the same coordinates as a previous segment.

* Ibreve (U+012C): L&lt;&lt;331.0,1769.0&gt;--&lt;331.0,1656.0&gt;&gt; has the same coordinates as a previous segment.

* Itilde (U+0128): L&lt;&lt;282.0,1857.0&gt;--&lt;282.0,1758.0&gt;&gt; has the same coordinates as a previous segment.

* Itilde (U+0128): L&lt;&lt;632.0,1697.0&gt;--&lt;632.0,1796.0&gt;&gt; has the same coordinates as a previous segment.

* Ntilde (U+00D1): L&lt;&lt;300.0,1858.0&gt;--&lt;300.0,1759.0&gt;&gt; has the same coordinates as a previous segment.

* Ntilde (U+00D1): L&lt;&lt;650.0,1698.0&gt;--&lt;650.0,1797.0&gt;&gt; has the same coordinates as a previous segment.

* Obreve (U+014E): L&lt;&lt;641.0,1774.0&gt;--&lt;641.0,1661.0&gt;&gt; has the same coordinates as a previous segment.

* Obreve (U+014E): L&lt;&lt;317.0,1774.0&gt;--&lt;317.0,1661.0&gt;&gt; has the same coordinates as a previous segment.

* Otilde (U+00D5): L&lt;&lt;366.0,1846.0&gt;--&lt;366.0,1747.0&gt;&gt; has the same coordinates as a previous segment.

* Otilde (U+00D5): L&lt;&lt;716.0,1686.0&gt;--&lt;716.0,1785.0&gt;&gt; has the same coordinates as a previous segment.

* S (U+0053): L&lt;&lt;146.0,1028.0&gt;--&lt;348.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* S (U+0053): L&lt;&lt;918.0,355.0&gt;--&lt;717.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* Sacute (U+015A): L&lt;&lt;146.0,1028.0&gt;--&lt;348.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* Sacute (U+015A): L&lt;&lt;918.0,355.0&gt;--&lt;717.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* Scaron (U+0160): L&lt;&lt;146.0,1028.0&gt;--&lt;348.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* Scaron (U+0160): L&lt;&lt;918.0,355.0&gt;--&lt;717.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* Scedilla (U+015E): L&lt;&lt;146.0,1028.0&gt;--&lt;348.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* Scedilla (U+015E): L&lt;&lt;918.0,355.0&gt;--&lt;717.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* Scircumflex (U+015C): L&lt;&lt;146.0,1028.0&gt;--&lt;348.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* Scircumflex (U+015C): L&lt;&lt;918.0,355.0&gt;--&lt;717.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* Ubreve (U+016C): L&lt;&lt;693.0,1770.0&gt;--&lt;693.0,1657.0&gt;&gt; has the same coordinates as a previous segment.

* Ubreve (U+016C): L&lt;&lt;369.0,1770.0&gt;--&lt;369.0,1657.0&gt;&gt; has the same coordinates as a previous segment.

* Utilde (U+0168): L&lt;&lt;320.0,1858.0&gt;--&lt;320.0,1759.0&gt;&gt; has the same coordinates as a previous segment.

* Utilde (U+0168): L&lt;&lt;670.0,1698.0&gt;--&lt;670.0,1797.0&gt;&gt; has the same coordinates as a previous segment.

* abreve (U+0103): L&lt;&lt;685.0,1262.0&gt;--&lt;685.0,1149.0&gt;&gt; has the same coordinates as a previous segment.

* abreve (U+0103): L&lt;&lt;361.0,1262.0&gt;--&lt;361.0,1149.0&gt;&gt; has the same coordinates as a previous segment.

* approxequal (U+2248): L&lt;&lt;330.0,559.0&gt;--&lt;330.0,395.0&gt;&gt; has the same coordinates as a previous segment.

* approxequal (U+2248): L&lt;&lt;680.0,334.0&gt;--&lt;680.0,498.0&gt;&gt; has the same coordinates as a previous segment.

* approxequal (U+2248): L&lt;&lt;330.0,898.0&gt;--&lt;330.0,716.0&gt;&gt; has the same coordinates as a previous segment.

* approxequal (U+2248): L&lt;&lt;680.0,655.0&gt;--&lt;680.0,837.0&gt;&gt; has the same coordinates as a previous segment.

* asciitilde (U+007E): L&lt;&lt;330.0,815.0&gt;--&lt;330.0,663.0&gt;&gt; has the same coordinates as a previous segment.

* asciitilde (U+007E): L&lt;&lt;680.0,602.0&gt;--&lt;680.0,754.0&gt;&gt; has the same coordinates as a previous segment.

* atilde (U+00E3): L&lt;&lt;312.0,1350.0&gt;--&lt;312.0,1251.0&gt;&gt; has the same coordinates as a previous segment.

* atilde (U+00E3): L&lt;&lt;662.0,1190.0&gt;--&lt;662.0,1289.0&gt;&gt; has the same coordinates as a previous segment.

* baht (U+0E3F): L&lt;&lt;433.0,1023.0&gt;--&lt;433.0,820.0&gt;&gt; has the same coordinates as a previous segment.

* baht (U+0E3F): L&lt;&lt;442.0,766.0&gt;--&lt;442.0,567.0&gt;&gt; has the same coordinates as a previous segment.

* baht (U+0E3F): L&lt;&lt;433.0,1537.0&gt;--&lt;433.0,1331.0&gt;&gt; has the same coordinates as a previous segment.

* braceleft (U+007B): L&lt;&lt;421.0,838.0&gt;--&lt;567.0,838.0&gt;&gt; has the same coordinates as a previous segment.

* braceleft (U+007B): L&lt;&lt;132.0,630.0&gt;--&lt;132.0,690.0&gt;&gt; has the same coordinates as a previous segment.

* braceright (U+007D): L&lt;&lt;710.0,690.0&gt;--&lt;710.0,630.0&gt;&gt; has the same coordinates as a previous segment.

* braceright (U+007D): L&lt;&lt;423.0,424.0&gt;--&lt;263.0,424.0&gt;&gt; has the same coordinates as a previous segment.

* breve (U+02D8): L&lt;&lt;656.0,1548.0&gt;--&lt;656.0,1480.0&gt;&gt; has the same coordinates as a previous segment.

* breve (U+02D8): L&lt;&lt;332.0,1548.0&gt;--&lt;332.0,1480.0&gt;&gt; has the same coordinates as a previous segment.

* brevecomb_acutecomb: L&lt;&lt;191.0,1214.0&gt;--&lt;191.0,1101.0&gt;&gt; has the same coordinates as a previous segment.

* brevecomb_acutecomb: L&lt;&lt;-133.0,1214.0&gt;--&lt;-133.0,1101.0&gt;&gt; has the same coordinates as a previous segment.

* brevecomb_gravecomb: L&lt;&lt;191.0,1214.0&gt;--&lt;191.0,1101.0&gt;&gt; has the same coordinates as a previous segment.

* brevecomb_gravecomb: L&lt;&lt;-133.0,1214.0&gt;--&lt;-133.0,1101.0&gt;&gt; has the same coordinates as a previous segment.

* brevecomb_hookabovecomb: L&lt;&lt;173.0,1141.0&gt;--&lt;173.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* brevecomb_hookabovecomb: L&lt;&lt;-151.0,1141.0&gt;--&lt;-151.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* brevecomb_tildecomb: L&lt;&lt;182.0,904.0&gt;--&lt;182.0,791.0&gt;&gt; has the same coordinates as a previous segment.

* brevecomb_tildecomb: L&lt;&lt;-142.0,904.0&gt;--&lt;-142.0,791.0&gt;&gt; has the same coordinates as a previous segment.

* brevecomb_tildecomb: L&lt;&lt;-154.0,1241.0&gt;--&lt;-154.0,1142.0&gt;&gt; has the same coordinates as a previous segment.

* brevecomb_tildecomb: L&lt;&lt;196.0,1081.0&gt;--&lt;196.0,1180.0&gt;&gt; has the same coordinates as a previous segment.

* circumflexcomb_tildecomb: L&lt;&lt;-158.0,1209.0&gt;--&lt;-158.0,1110.0&gt;&gt; has the same coordinates as a previous segment.

* circumflexcomb_tildecomb: L&lt;&lt;192.0,1049.0&gt;--&lt;192.0,1148.0&gt;&gt; has the same coordinates as a previous segment.

* dollar (U+0024): L&lt;&lt;126.0,1028.0&gt;--&lt;331.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* dollar (U+0024): L&lt;&lt;898.0,355.0&gt;--&lt;692.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* ebreve (U+0115): L&lt;&lt;697.0,1294.0&gt;--&lt;697.0,1181.0&gt;&gt; has the same coordinates as a previous segment.

* ebreve (U+0115): L&lt;&lt;373.0,1294.0&gt;--&lt;373.0,1181.0&gt;&gt; has the same coordinates as a previous segment.

* ecedillabreve (U+1E1D): L&lt;&lt;697.0,1294.0&gt;--&lt;697.0,1181.0&gt;&gt; has the same coordinates as a previous segment.

* ecedillabreve (U+1E1D): L&lt;&lt;373.0,1294.0&gt;--&lt;373.0,1181.0&gt;&gt; has the same coordinates as a previous segment.

* gbreve (U+011F): L&lt;&lt;763.0,1304.0&gt;--&lt;763.0,1191.0&gt;&gt; has the same coordinates as a previous segment.

* gbreve (U+011F): L&lt;&lt;439.0,1304.0&gt;--&lt;439.0,1191.0&gt;&gt; has the same coordinates as a previous segment.

* greater (U+003E): L&lt;&lt;922.0,777.0&gt;--&lt;924.0,568.0&gt;&gt; has the same coordinates as a previous segment.

* greaterequal (U+2265): L&lt;&lt;922.0,777.0&gt;--&lt;924.0,568.0&gt;&gt; has the same coordinates as a previous segment.

* guillemotleft (U+00AB): L&lt;&lt;134.0,454.0&gt;--&lt;134.0,609.0&gt;&gt; has the same coordinates as a previous segment.

* guillemotleft (U+00AB): L&lt;&lt;549.0,454.0&gt;--&lt;549.0,609.0&gt;&gt; has the same coordinates as a previous segment.

* guillemotright (U+00BB): L&lt;&lt;920.0,609.0&gt;--&lt;920.0,454.0&gt;&gt; has the same coordinates as a previous segment.

* guillemotright (U+00BB): L&lt;&lt;505.0,609.0&gt;--&lt;505.0,454.0&gt;&gt; has the same coordinates as a previous segment.

* guilsinglleft (U+2039): L&lt;&lt;103.0,569.0&gt;--&lt;103.0,777.0&gt;&gt; has the same coordinates as a previous segment.

* guilsinglright (U+203A): L&lt;&lt;922.0,777.0&gt;--&lt;924.0,568.0&gt;&gt; has the same coordinates as a previous segment.

* hryvnia (U+20B4): L&lt;&lt;347.0,355.0&gt;--&lt;146.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* hryvnia (U+20B4): L&lt;&lt;716.0,1028.0&gt;--&lt;918.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* ibreve (U+012D): L&lt;&lt;677.0,1319.0&gt;--&lt;677.0,1206.0&gt;&gt; has the same coordinates as a previous segment.

* ibreve (U+012D): L&lt;&lt;353.0,1319.0&gt;--&lt;353.0,1206.0&gt;&gt; has the same coordinates as a previous segment.

* itilde (U+0129): L&lt;&lt;304.0,1407.0&gt;--&lt;304.0,1308.0&gt;&gt; has the same coordinates as a previous segment.

* itilde (U+0129): L&lt;&lt;654.0,1247.0&gt;--&lt;654.0,1346.0&gt;&gt; has the same coordinates as a previous segment.

* j_uni0303: L&lt;&lt;538.0,1181.0&gt;--&lt;538.0,1082.0&gt;&gt; has the same coordinates as a previous segment.

* j_uni0303: L&lt;&lt;888.0,1021.0&gt;--&lt;888.0,1120.0&gt;&gt; has the same coordinates as a previous segment.

* j_uni0311: L&lt;&lt;541.0,1099.0&gt;--&lt;541.0,1167.0&gt;&gt; has the same coordinates as a previous segment.

* j_uni0311: L&lt;&lt;865.0,1099.0&gt;--&lt;865.0,1167.0&gt;&gt; has the same coordinates as a previous segment.

* less (U+003C): L&lt;&lt;103.0,569.0&gt;--&lt;103.0,777.0&gt;&gt; has the same coordinates as a previous segment.

* lessequal (U+2264): L&lt;&lt;103.0,569.0&gt;--&lt;103.0,777.0&gt;&gt; has the same coordinates as a previous segment.

* ntilde (U+00F1): L&lt;&lt;304.0,1374.0&gt;--&lt;304.0,1275.0&gt;&gt; has the same coordinates as a previous segment.

* ntilde (U+00F1): L&lt;&lt;654.0,1214.0&gt;--&lt;654.0,1313.0&gt;&gt; has the same coordinates as a previous segment.

* obreve (U+014F): L&lt;&lt;689.0,1286.0&gt;--&lt;689.0,1173.0&gt;&gt; has the same coordinates as a previous segment.

* obreve (U+014F): L&lt;&lt;365.0,1286.0&gt;--&lt;365.0,1173.0&gt;&gt; has the same coordinates as a previous segment.

* otilde (U+00F5): L&lt;&lt;316.0,1374.0&gt;--&lt;316.0,1275.0&gt;&gt; has the same coordinates as a previous segment.

* otilde (U+00F5): L&lt;&lt;666.0,1214.0&gt;--&lt;666.0,1313.0&gt;&gt; has the same coordinates as a previous segment.

* parenleft (U+0028): L&lt;&lt;324.0,179.0&gt;--&lt;514.0,179.0&gt;&gt; has the same coordinates as a previous segment.

* parenright (U+0029): L&lt;&lt;678.0,1023.0&gt;--&lt;488.0,1023.0&gt;&gt; has the same coordinates as a previous segment.

* parenright (U+0029): L&lt;&lt;488.0,179.0&gt;--&lt;678.0,179.0&gt;&gt; has the same coordinates as a previous segment.

* peseta (U+20A7): L&lt;&lt;932.0,173.0&gt;--&lt;881.0,173.0&gt;&gt; has the same coordinates as a previous segment.

* ringhalfleft (U+02BF): L&lt;&lt;472.0,1200.0&gt;--&lt;404.0,1200.0&gt;&gt; has the same coordinates as a previous segment.

* ringhalfleft (U+02BF): L&lt;&lt;472.0,1524.0&gt;--&lt;404.0,1524.0&gt;&gt; has the same coordinates as a previous segment.

* ringhalfright (U+02BE): L&lt;&lt;523.0,1530.0&gt;--&lt;591.0,1530.0&gt;&gt; has the same coordinates as a previous segment.

* ringhalfright (U+02BE): L&lt;&lt;523.0,1206.0&gt;--&lt;591.0,1206.0&gt;&gt; has the same coordinates as a previous segment.

* rupee (U+20A8): L&lt;&lt;853.0,293.0&gt;--&lt;753.0,293.0&gt;&gt; has the same coordinates as a previous segment.

* s (U+0073): L&lt;&lt;791.0,293.0&gt;--&lt;591.0,293.0&gt;&gt; has the same coordinates as a previous segment.

* sacute (U+015B): L&lt;&lt;791.0,293.0&gt;--&lt;591.0,293.0&gt;&gt; has the same coordinates as a previous segment.

* scaron (U+0161): L&lt;&lt;791.0,293.0&gt;--&lt;591.0,293.0&gt;&gt; has the same coordinates as a previous segment.

* scedilla (U+015F): L&lt;&lt;791.0,293.0&gt;--&lt;591.0,293.0&gt;&gt; has the same coordinates as a previous segment.

* scircumflex (U+015D): L&lt;&lt;791.0,293.0&gt;--&lt;591.0,293.0&gt;&gt; has the same coordinates as a previous segment.

* section (U+00A7): L&lt;&lt;146.0,605.0&gt;--&lt;348.0,605.0&gt;&gt; has the same coordinates as a previous segment.

* section (U+00A7): L&lt;&lt;927.0,95.0&gt;--&lt;726.0,95.0&gt;&gt; has the same coordinates as a previous segment.

* section (U+00A7): L&lt;&lt;146.0,1237.0&gt;--&lt;348.0,1237.0&gt;&gt; has the same coordinates as a previous segment.

* section (U+00A7): L&lt;&lt;918.0,442.0&gt;--&lt;717.0,442.0&gt;&gt; has the same coordinates as a previous segment.

* sheqel (U+20AA): L&lt;&lt;620.0,1278.0&gt;--&lt;768.0,1277.0&gt;&gt; has the same coordinates as a previous segment.

* sheqel (U+20AA): L&lt;&lt;465.0,264.0&gt;--&lt;317.0,265.0&gt;&gt; has the same coordinates as a previous segment.

* tilde (U+02DC): L&lt;&lt;359.0,1607.0&gt;--&lt;359.0,1528.0&gt;&gt; has the same coordinates as a previous segment.

* tilde (U+02DC): L&lt;&lt;639.0,1479.0&gt;--&lt;639.0,1558.0&gt;&gt; has the same coordinates as a previous segment.

* tildecomb (U+0303): L&lt;&lt;-194.0,994.0&gt;--&lt;-194.0,895.0&gt;&gt; has the same coordinates as a previous segment.

* tildecomb (U+0303): L&lt;&lt;156.0,834.0&gt;--&lt;156.0,933.0&gt;&gt; has the same coordinates as a previous segment.

* ubreve (U+016D): L&lt;&lt;625.0,1274.0&gt;--&lt;625.0,1161.0&gt;&gt; has the same coordinates as a previous segment.

* ubreve (U+016D): L&lt;&lt;301.0,1274.0&gt;--&lt;301.0,1161.0&gt;&gt; has the same coordinates as a previous segment.

* uni012F_uni0303: L&lt;&lt;313.0,1258.0&gt;--&lt;313.0,1159.0&gt;&gt; has the same coordinates as a previous segment.

* uni012F_uni0303: L&lt;&lt;663.0,1098.0&gt;--&lt;663.0,1197.0&gt;&gt; has the same coordinates as a previous segment.

* uni0202 (U+0202): L&lt;&lt;330.0,1695.0&gt;--&lt;330.0,1763.0&gt;&gt; has the same coordinates as a previous segment.

* uni0202 (U+0202): L&lt;&lt;654.0,1695.0&gt;--&lt;654.0,1763.0&gt;&gt; has the same coordinates as a previous segment.

* uni0203 (U+0203): L&lt;&lt;305.0,1188.0&gt;--&lt;305.0,1256.0&gt;&gt; has the same coordinates as a previous segment.

* uni0203 (U+0203): L&lt;&lt;629.0,1188.0&gt;--&lt;629.0,1256.0&gt;&gt; has the same coordinates as a previous segment.

* uni0206 (U+0206): L&lt;&lt;275.0,1695.0&gt;--&lt;275.0,1763.0&gt;&gt; has the same coordinates as a previous segment.

* uni0206 (U+0206): L&lt;&lt;599.0,1695.0&gt;--&lt;599.0,1763.0&gt;&gt; has the same coordinates as a previous segment.

* uni0207 (U+0207): L&lt;&lt;317.0,1220.0&gt;--&lt;317.0,1288.0&gt;&gt; has the same coordinates as a previous segment.

* uni0207 (U+0207): L&lt;&lt;641.0,1220.0&gt;--&lt;641.0,1288.0&gt;&gt; has the same coordinates as a previous segment.

* uni020A (U+020A): L&lt;&lt;275.0,1695.0&gt;--&lt;275.0,1763.0&gt;&gt; has the same coordinates as a previous segment.

* uni020A (U+020A): L&lt;&lt;599.0,1695.0&gt;--&lt;599.0,1763.0&gt;&gt; has the same coordinates as a previous segment.

* uni020B (U+020B): L&lt;&lt;297.0,1245.0&gt;--&lt;297.0,1313.0&gt;&gt; has the same coordinates as a previous segment.

* uni020B (U+020B): L&lt;&lt;621.0,1245.0&gt;--&lt;621.0,1313.0&gt;&gt; has the same coordinates as a previous segment.

* uni020E (U+020E): L&lt;&lt;261.0,1700.0&gt;--&lt;261.0,1768.0&gt;&gt; has the same coordinates as a previous segment.

* uni020E (U+020E): L&lt;&lt;585.0,1700.0&gt;--&lt;585.0,1768.0&gt;&gt; has the same coordinates as a previous segment.

* uni020F (U+020F): L&lt;&lt;309.0,1212.0&gt;--&lt;309.0,1280.0&gt;&gt; has the same coordinates as a previous segment.

* uni020F (U+020F): L&lt;&lt;633.0,1212.0&gt;--&lt;633.0,1280.0&gt;&gt; has the same coordinates as a previous segment.

* uni0212 (U+0212): L&lt;&lt;285.0,1696.0&gt;--&lt;285.0,1764.0&gt;&gt; has the same coordinates as a previous segment.

* uni0212 (U+0212): L&lt;&lt;609.0,1696.0&gt;--&lt;609.0,1764.0&gt;&gt; has the same coordinates as a previous segment.

* uni0213 (U+0213): L&lt;&lt;309.0,1228.0&gt;--&lt;309.0,1296.0&gt;&gt; has the same coordinates as a previous segment.

* uni0213 (U+0213): L&lt;&lt;633.0,1228.0&gt;--&lt;633.0,1296.0&gt;&gt; has the same coordinates as a previous segment.

* uni0216 (U+0216): L&lt;&lt;313.0,1696.0&gt;--&lt;313.0,1764.0&gt;&gt; has the same coordinates as a previous segment.

* uni0216 (U+0216): L&lt;&lt;637.0,1696.0&gt;--&lt;637.0,1764.0&gt;&gt; has the same coordinates as a previous segment.

* uni0217 (U+0217): L&lt;&lt;245.0,1200.0&gt;--&lt;245.0,1268.0&gt;&gt; has the same coordinates as a previous segment.

* uni0217 (U+0217): L&lt;&lt;569.0,1200.0&gt;--&lt;569.0,1268.0&gt;&gt; has the same coordinates as a previous segment.

* uni0218 (U+0218): L&lt;&lt;146.0,1028.0&gt;--&lt;348.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* uni0218 (U+0218): L&lt;&lt;918.0,355.0&gt;--&lt;717.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* uni0219 (U+0219): L&lt;&lt;791.0,293.0&gt;--&lt;591.0,293.0&gt;&gt; has the same coordinates as a previous segment.

* uni022C (U+022C): L&lt;&lt;366.0,1846.0&gt;--&lt;366.0,1747.0&gt;&gt; has the same coordinates as a previous segment.

* uni022C (U+022C): L&lt;&lt;716.0,1686.0&gt;--&lt;716.0,1785.0&gt;&gt; has the same coordinates as a previous segment.

* uni022D (U+022D): L&lt;&lt;316.0,1374.0&gt;--&lt;316.0,1275.0&gt;&gt; has the same coordinates as a previous segment.

* uni022D (U+022D): L&lt;&lt;666.0,1214.0&gt;--&lt;666.0,1313.0&gt;&gt; has the same coordinates as a previous segment.

* uni0306 (U+0306): L&lt;&lt;182.0,904.0&gt;--&lt;182.0,791.0&gt;&gt; has the same coordinates as a previous segment.

* uni0306 (U+0306): L&lt;&lt;-142.0,904.0&gt;--&lt;-142.0,791.0&gt;&gt; has the same coordinates as a previous segment.

* uni0311 (U+0311): L&lt;&lt;-193.0,834.0&gt;--&lt;-193.0,902.0&gt;&gt; has the same coordinates as a previous segment.

* uni0311 (U+0311): L&lt;&lt;131.0,834.0&gt;--&lt;131.0,902.0&gt;&gt; has the same coordinates as a previous segment.

* uni032E (U+032E): L&lt;&lt;197.0,-173.0&gt;--&lt;197.0,-241.0&gt;&gt; has the same coordinates as a previous segment.

* uni032E (U+032E): L&lt;&lt;-127.0,-173.0&gt;--&lt;-127.0,-241.0&gt;&gt; has the same coordinates as a previous segment.

* uni0926_uni094D_uni092F.pres: L&lt;&lt;674.0,428.0&gt;--&lt;674.0,229.0&gt;&gt; has the same coordinates as a previous segment.

* uni092F (U+092F): L&lt;&lt;318.0,846.0&gt;--&lt;528.0,846.0&gt;&gt; has the same coordinates as a previous segment.

* uni092F_uni0930_uni094D.vatu: L&lt;&lt;318.0,846.0&gt;--&lt;528.0,846.0&gt;&gt; has the same coordinates as a previous segment.

* uni092F_uni094D.half: L&lt;&lt;568.0,846.0&gt;--&lt;778.0,846.0&gt;&gt; has the same coordinates as a previous segment.

* uni092F_uni094D.haln: L&lt;&lt;330.0,846.0&gt;--&lt;540.0,846.0&gt;&gt; has the same coordinates as a previous segment.

* uni0930_uni094D.half: L&lt;&lt;696.0,802.0&gt;--&lt;696.0,603.0&gt;&gt; has the same coordinates as a previous segment.

* uni0930_uni094D.rphf: L&lt;&lt;163.0,2162.0&gt;--&lt;163.0,1962.0&gt;&gt; has the same coordinates as a previous segment.

* uni0930_uni094D_uni0902.abvs: L&lt;&lt;163.0,2162.0&gt;--&lt;163.0,1962.0&gt;&gt; has the same coordinates as a previous segment.

* uni095F (U+095F): L&lt;&lt;318.0,846.0&gt;--&lt;528.0,846.0&gt;&gt; has the same coordinates as a previous segment.

* uni095F_uni0930_uni094D.vatu: L&lt;&lt;318.0,846.0&gt;--&lt;528.0,846.0&gt;&gt; has the same coordinates as a previous segment.

* uni095F_uni094D.half: L&lt;&lt;318.0,846.0&gt;--&lt;528.0,846.0&gt;&gt; has the same coordinates as a previous segment.

* uni095F_uni094D.haln: L&lt;&lt;338.0,846.0&gt;--&lt;548.0,846.0&gt;&gt; has the same coordinates as a previous segment.

* uni096A (U+096A): L&lt;&lt;158.0,317.0&gt;--&lt;358.0,317.0&gt;&gt; has the same coordinates as a previous segment.

* uni097A (U+097A): L&lt;&lt;318.0,846.0&gt;--&lt;528.0,846.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E02 (U+1E02): L&lt;&lt;433.0,1023.0&gt;--&lt;433.0,820.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E02 (U+1E02): L&lt;&lt;442.0,766.0&gt;--&lt;442.0,567.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E02 (U+1E02): L&lt;&lt;433.0,1537.0&gt;--&lt;433.0,1331.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E2A (U+1E2A): L&lt;&lt;701.0,-203.0&gt;--&lt;701.0,-271.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E2A (U+1E2A): L&lt;&lt;377.0,-203.0&gt;--&lt;377.0,-271.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E2B (U+1E2B): L&lt;&lt;717.0,-215.0&gt;--&lt;717.0,-283.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E2B (U+1E2B): L&lt;&lt;393.0,-215.0&gt;--&lt;393.0,-283.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E4C (U+1E4C): L&lt;&lt;366.0,1846.0&gt;--&lt;366.0,1747.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E4C (U+1E4C): L&lt;&lt;716.0,1686.0&gt;--&lt;716.0,1785.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E4D (U+1E4D): L&lt;&lt;316.0,1374.0&gt;--&lt;316.0,1275.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E4D (U+1E4D): L&lt;&lt;666.0,1214.0&gt;--&lt;666.0,1313.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E4E (U+1E4E): L&lt;&lt;366.0,1846.0&gt;--&lt;366.0,1747.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E4E (U+1E4E): L&lt;&lt;716.0,1686.0&gt;--&lt;716.0,1785.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E4F (U+1E4F): L&lt;&lt;316.0,1374.0&gt;--&lt;316.0,1275.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E4F (U+1E4F): L&lt;&lt;666.0,1214.0&gt;--&lt;666.0,1313.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E60 (U+1E60): L&lt;&lt;146.0,1028.0&gt;--&lt;348.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E60 (U+1E60): L&lt;&lt;918.0,355.0&gt;--&lt;717.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E61 (U+1E61): L&lt;&lt;791.0,293.0&gt;--&lt;591.0,293.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E62 (U+1E62): L&lt;&lt;146.0,1028.0&gt;--&lt;348.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E62 (U+1E62): L&lt;&lt;918.0,355.0&gt;--&lt;717.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E63 (U+1E63): L&lt;&lt;791.0,293.0&gt;--&lt;591.0,293.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E64 (U+1E64): L&lt;&lt;146.0,1028.0&gt;--&lt;348.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E64 (U+1E64): L&lt;&lt;918.0,355.0&gt;--&lt;717.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E65 (U+1E65): L&lt;&lt;791.0,293.0&gt;--&lt;591.0,293.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E66 (U+1E66): L&lt;&lt;146.0,1028.0&gt;--&lt;348.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E66 (U+1E66): L&lt;&lt;918.0,355.0&gt;--&lt;717.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E67 (U+1E67): L&lt;&lt;791.0,293.0&gt;--&lt;591.0,293.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E68 (U+1E68): L&lt;&lt;146.0,1028.0&gt;--&lt;348.0,1028.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E68 (U+1E68): L&lt;&lt;918.0,355.0&gt;--&lt;717.0,355.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E69 (U+1E69): L&lt;&lt;791.0,293.0&gt;--&lt;591.0,293.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E78 (U+1E78): L&lt;&lt;320.0,1858.0&gt;--&lt;320.0,1759.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E78 (U+1E78): L&lt;&lt;670.0,1698.0&gt;--&lt;670.0,1797.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E79 (U+1E79): L&lt;&lt;252.0,1362.0&gt;--&lt;252.0,1263.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E79 (U+1E79): L&lt;&lt;602.0,1202.0&gt;--&lt;602.0,1301.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E7C (U+1E7C): L&lt;&lt;373.0,1828.0&gt;--&lt;373.0,1729.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E7C (U+1E7C): L&lt;&lt;723.0,1668.0&gt;--&lt;723.0,1767.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E7D (U+1E7D): L&lt;&lt;344.0,1338.0&gt;--&lt;344.0,1239.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E7D (U+1E7D): L&lt;&lt;694.0,1178.0&gt;--&lt;694.0,1277.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EAA (U+1EAA): L&lt;&lt;399.0,2109.0&gt;--&lt;399.0,2010.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EAA (U+1EAA): L&lt;&lt;749.0,1949.0&gt;--&lt;749.0,2048.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EAB (U+1EAB): L&lt;&lt;373.0,1577.0&gt;--&lt;373.0,1478.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EAB (U+1EAB): L&lt;&lt;723.0,1417.0&gt;--&lt;723.0,1516.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EAE (U+1EAE): L&lt;&lt;710.0,1769.0&gt;--&lt;710.0,1656.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EAE (U+1EAE): L&lt;&lt;386.0,1769.0&gt;--&lt;386.0,1656.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EAF (U+1EAF): L&lt;&lt;685.0,1262.0&gt;--&lt;685.0,1149.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EAF (U+1EAF): L&lt;&lt;361.0,1262.0&gt;--&lt;361.0,1149.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB0 (U+1EB0): L&lt;&lt;710.0,1769.0&gt;--&lt;710.0,1656.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB0 (U+1EB0): L&lt;&lt;386.0,1769.0&gt;--&lt;386.0,1656.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB1 (U+1EB1): L&lt;&lt;685.0,1262.0&gt;--&lt;685.0,1149.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB1 (U+1EB1): L&lt;&lt;361.0,1262.0&gt;--&lt;361.0,1149.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB2 (U+1EB2): L&lt;&lt;710.0,1769.0&gt;--&lt;710.0,1656.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB2 (U+1EB2): L&lt;&lt;386.0,1769.0&gt;--&lt;386.0,1656.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB3 (U+1EB3): L&lt;&lt;685.0,1262.0&gt;--&lt;685.0,1149.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB3 (U+1EB3): L&lt;&lt;361.0,1262.0&gt;--&lt;361.0,1149.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB4 (U+1EB4): L&lt;&lt;428.0,2077.0&gt;--&lt;428.0,1978.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB4 (U+1EB4): L&lt;&lt;778.0,1917.0&gt;--&lt;778.0,2016.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB4 (U+1EB4): L&lt;&lt;710.0,1769.0&gt;--&lt;710.0,1656.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB4 (U+1EB4): L&lt;&lt;386.0,1769.0&gt;--&lt;386.0,1656.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB5 (U+1EB5): L&lt;&lt;399.0,1521.0&gt;--&lt;399.0,1422.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB5 (U+1EB5): L&lt;&lt;749.0,1361.0&gt;--&lt;749.0,1460.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB5 (U+1EB5): L&lt;&lt;685.0,1262.0&gt;--&lt;685.0,1149.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB5 (U+1EB5): L&lt;&lt;361.0,1262.0&gt;--&lt;361.0,1149.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB6 (U+1EB6): L&lt;&lt;688.0,1783.0&gt;--&lt;688.0,1670.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB6 (U+1EB6): L&lt;&lt;364.0,1783.0&gt;--&lt;364.0,1670.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB7 (U+1EB7): L&lt;&lt;676.0,1258.0&gt;--&lt;676.0,1145.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EB7 (U+1EB7): L&lt;&lt;352.0,1258.0&gt;--&lt;352.0,1145.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EBC (U+1EBC): L&lt;&lt;282.0,1857.0&gt;--&lt;282.0,1758.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EBC (U+1EBC): L&lt;&lt;632.0,1697.0&gt;--&lt;632.0,1796.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EBD (U+1EBD): L&lt;&lt;324.0,1382.0&gt;--&lt;324.0,1283.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EBD (U+1EBD): L&lt;&lt;674.0,1222.0&gt;--&lt;674.0,1321.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EC4 (U+1EC4): L&lt;&lt;338.0,2089.0&gt;--&lt;338.0,1990.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EC4 (U+1EC4): L&lt;&lt;688.0,1929.0&gt;--&lt;688.0,2028.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EC5 (U+1EC5): L&lt;&lt;360.0,1660.0&gt;--&lt;360.0,1561.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EC5 (U+1EC5): L&lt;&lt;710.0,1500.0&gt;--&lt;710.0,1599.0&gt;&gt; has the same coordinates as a previous segment.

* uni1ECB_uni0303: L&lt;&lt;337.0,1282.0&gt;--&lt;337.0,1183.0&gt;&gt; has the same coordinates as a previous segment.

* uni1ECB_uni0303: L&lt;&lt;687.0,1122.0&gt;--&lt;687.0,1221.0&gt;&gt; has the same coordinates as a previous segment.

* uni1ED6 (U+1ED6): L&lt;&lt;304.0,2204.0&gt;--&lt;304.0,2105.0&gt;&gt; has the same coordinates as a previous segment.

* uni1ED6 (U+1ED6): L&lt;&lt;654.0,2044.0&gt;--&lt;654.0,2143.0&gt;&gt; has the same coordinates as a previous segment.

* uni1ED7 (U+1ED7): L&lt;&lt;355.0,1578.0&gt;--&lt;355.0,1479.0&gt;&gt; has the same coordinates as a previous segment.

* uni1ED7 (U+1ED7): L&lt;&lt;705.0,1418.0&gt;--&lt;705.0,1517.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EE0 (U+1EE0): L&lt;&lt;297.0,1996.0&gt;--&lt;297.0,1897.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EE0 (U+1EE0): L&lt;&lt;647.0,1836.0&gt;--&lt;647.0,1935.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EE1 (U+1EE1): L&lt;&lt;255.0,1479.0&gt;--&lt;255.0,1380.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EE1 (U+1EE1): L&lt;&lt;605.0,1319.0&gt;--&lt;605.0,1418.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EEE (U+1EEE): L&lt;&lt;320.0,1903.0&gt;--&lt;320.0,1804.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EEE (U+1EEE): L&lt;&lt;670.0,1743.0&gt;--&lt;670.0,1842.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EEF (U+1EEF): L&lt;&lt;237.0,1395.0&gt;--&lt;237.0,1296.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EEF (U+1EEF): L&lt;&lt;587.0,1235.0&gt;--&lt;587.0,1334.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EF8 (U+1EF8): L&lt;&lt;336.0,1854.0&gt;--&lt;336.0,1755.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EF8 (U+1EF8): L&lt;&lt;686.0,1694.0&gt;--&lt;686.0,1793.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EF9 (U+1EF9): L&lt;&lt;340.0,1358.0&gt;--&lt;340.0,1259.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EF9 (U+1EF9): L&lt;&lt;690.0,1198.0&gt;--&lt;690.0,1297.0&gt;&gt; has the same coordinates as a previous segment.

* uni207D (U+207D): L&lt;&lt;406.0,771.0&gt;--&lt;513.0,771.0&gt;&gt; has the same coordinates as a previous segment.

* uni207E (U+207E): L&lt;&lt;605.0,1243.0&gt;--&lt;499.0,1243.0&gt;&gt; has the same coordinates as a previous segment.

* uni207E (U+207E): L&lt;&lt;499.0,769.0&gt;--&lt;605.0,769.0&gt;&gt; has the same coordinates as a previous segment.

* uni208D (U+208D): L&lt;&lt;406.0,-229.0&gt;--&lt;513.0,-229.0&gt;&gt; has the same coordinates as a previous segment.

* uni208E (U+208E): L&lt;&lt;605.0,243.0&gt;--&lt;499.0,243.0&gt;&gt; has the same coordinates as a previous segment.

* uni208E (U+208E): L&lt;&lt;499.0,-231.0&gt;--&lt;605.0,-231.0&gt;&gt; has the same coordinates as a previous segment.

* uni20BF (U+20BF): L&lt;&lt;747.0,1023.0&gt;--&lt;747.0,820.0&gt;&gt; has the same coordinates as a previous segment.

* uni20BF (U+20BF): L&lt;&lt;756.0,766.0&gt;--&lt;756.0,567.0&gt;&gt; has the same coordinates as a previous segment.

* uni20BF (U+20BF): L&lt;&lt;747.0,1537.0&gt;--&lt;747.0,1331.0&gt;&gt; has the same coordinates as a previous segment.

* uni27E9 (U+27E9): L&lt;&lt;902.0,741.0&gt;--&lt;902.0,569.0&gt;&gt; has the same coordinates as a previous segment.

* utilde (U+0169): L&lt;&lt;252.0,1362.0&gt;--&lt;252.0,1263.0&gt;&gt; has the same coordinates as a previous segment.

* utilde (U+0169): L&lt;&lt;602.0,1202.0&gt;--&lt;602.0,1301.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- L_periodcentered.loclCAT

- brevecomb_acutecomb

- brevecomb_gravecomb

- brevecomb_hookabovecomb

- brevecomb_tildecomb

- circumflexcomb_acutecomb

- circumflexcomb_gravecomb

- circumflexcomb_hookabovecomb

- circumflexcomb_tildecomb

- idotaccent

- l_periodcentered.loclCAT
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, coptic, cherokee, tifinagh</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: gothic, glagolitic, elbasan, math, coptic</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: duployan, canadian-aboriginal, math, malayalam, hebrew, old-permic, syriac, coptic, todhri, tai-le, tifinagh</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+030D COMBINING VERTICAL LINE ABOVE: try adding sunuwar</li>
<li>U+030F COMBINING DOUBLE GRAVE ACCENT: not included in any glyphset definition</li>
<li>U+0310 COMBINING CANDRABINDU: try adding one of: math, sunuwar</li>
<li>U+0311 COMBINING INVERTED BREVE: try adding one of: coptic, todhri</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: duployan, cherokee, syriac</li>
<li>U+0325 COMBINING RING BELOW: try adding syriac</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: gothic, thai, cherokee, syriac, caucasian-albanian, sunuwar, tifinagh</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+035F COMBINING DOUBLE MACRON BELOW: not included in any glyphset definition</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
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
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: yi, math, symbols, tai-tham</li>
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
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>devanagari</code>, <code>greek</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-dotted">soft_dotted</a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: i̍ i̐ ɨ̀ ɨ́ ɨ̂ ɨ̃ ɨ̄ ɨ̈ ɨ̋ ɨ̌ ɨ̏ ɨ̧̀ ɨ̧́ ɨ̧̂ ɨ̧̌ ɨ̱̀ ɨ̱́ ɨ̱̈</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̅ i̇ i̒ i̛̅ i̛̇ i̛̊ i̛̋ i̛̍ i̛̐ i̛̒ i̤̅ i̤̇ i̤̊ i̤̋ i̤̍ i̤̐ i̤̒ i̥̅ i̥̇ i̥̊</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Bafut (Latn, 158,146 speakers), Northern Tutchone (Latn, 85 speakers), Heiltsuk (Latn, 300 speakers), Makaa (Latn, 221,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Ekpeye (Latn, 226,000 speakers), Dan (Latn, 1,099,244 speakers), Mundani (Latn, 34,000 speakers), Avokaya (Latn, 100,000 speakers), Ebira (Latn, 2,200,000 speakers), Western Krahn (Latn, 97,800 speakers), Aghem (Latn, 38,843 speakers), Kom (Latn, 360,685 speakers), Longto (Latn, 5,000 speakers), Abua (Latn, 25,000 speakers), Keliko (Latn, 63,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Southern Kisi (Latn, 360,000 speakers), Dii (Latn, 71,000 speakers), Han (Latn, 6 speakers), Belarusian (Cyrl, 10,064,517 speakers), Zapotec (Latn, 490,000 speakers), Vute (Latn, 21,000 speakers), Ma’di (Latn, 584,000 speakers), Nateni (Latn, 100,000 speakers), South Central Banda (Latn, 244,000 speakers), Ikwere (Latn, 717,000 speakers), Southern Tutchone (Latn, 65 speakers), Kaska (Latn, 125 speakers), Koonzime (Latn, 40,000 speakers), Yala (Latn, 200,000 speakers), Teke-Ebo (Latn, 260,000 speakers), Mango (Latn, 77,000 speakers), Cicipu (Latn, 44,000 speakers), Gulay (Latn, 250,478 speakers), Ngbaka (Latn, 1,020,000 speakers), Basaa (Latn, 332,940 speakers), Fur (Latn, 1,230,163 speakers), Lugbara (Latn, 2,200,000 speakers), Mfumte (Latn, 79,000 speakers), Sar (Latn, 500,000 speakers), Ejagham (Latn, 120,000 speakers), Navajo (Latn, 166,319 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Igbo (Latn, 27,823,640 speakers), Nzakara (Latn, 50,000 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-alignment-miss">outline_alignment_miss</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have on-curve points which have potentially incorrect y coordinates:</p>
<pre><code>* Chook (U+0187): X=62.0,Y=1550.0 (should be at cap-height 1548?)

* Chook (U+0187): X=262.0,Y=1550.0 (should be at cap-height 1548?)

* Chook (U+0187): X=62.0,Y=1550.0 (should be at cap-height 1548?)

* Chook (U+0187): X=161.0,Y=1550.0 (should be at cap-height 1548?)

* Chook (U+0187): X=944.0,Y=1550.0 (should be at cap-height 1548?)

* Chook (U+0187): X=161.0,Y=1550.0 (should be at cap-height 1548?)

* Eogonek (U+0118): X=477.0,Y=-1.0 (should be at baseline 0?)

* Eogonek (U+0118): X=595.0,Y=-1.0 (should be at baseline 0?)

* Eogonek (U+0118): X=477.0,Y=-1.0 (should be at baseline 0?)

* Eogonek (U+0118): X=477.0,Y=-1.0 (should be at baseline 0?)

* Eogonek (U+0118): X=1019.0,Y=-1.0 (should be at baseline 0?)

* Eogonek (U+0118): X=477.0,Y=-1.0 (should be at baseline 0?)

* Eopen (U+0190): X=296.0,Y=1.0 (should be at baseline 0?)

* Eopen (U+0190): X=96.0,Y=2.0 (should be at baseline 0?)

* beta (U+03B2): X=107.0,Y=1547.0 (should be at cap-height 1548?)

* beta (U+03B2): X=107.0,Y=1547.0 (should be at cap-height 1548?)

* beta (U+03B2): X=930.0,Y=2.0 (should be at baseline 0?)

* beta (U+03B2): X=730.0,Y=2.0 (should be at baseline 0?)

* beta (U+03B2): X=930.0,Y=2.0 (should be at baseline 0?)

* beta (U+03B2): X=399.0,Y=2.0 (should be at baseline 0?)

* ccedilla (U+00E7): X=568.0,Y=2.0 (should be at baseline 0?)

* ccedilla (U+00E7): X=724.0,Y=2.0 (should be at baseline 0?)

* ccedilla (U+00E7): X=568.0,Y=2.0 (should be at baseline 0?)

* dblverticalbar (U+2016): X=454.0,Y=-1.0 (should be at baseline 0?)

* dblverticalbar (U+2016): X=251.0,Y=-1.0 (should be at baseline 0?)

* delta (U+03B4): X=331.0,Y=1549.0 (should be at cap-height 1548?)

* delta (U+03B4): X=863.0,Y=1549.0 (should be at cap-height 1548?)

* delta (U+03B4): X=331.0,Y=1549.0 (should be at cap-height 1548?)

* eopen (U+025B): X=296.0,Y=1.0 (should be at baseline 0?)

* eopen (U+025B): X=96.0,Y=2.0 (should be at baseline 0?)

* epsilon (U+03B5): X=296.0,Y=1.0 (should be at baseline 0?)

* epsilon (U+03B5): X=96.0,Y=2.0 (should be at baseline 0?)

* epsilontonos (U+03AD): X=296.0,Y=1.0 (should be at baseline 0?)

* epsilontonos (U+03AD): X=96.0,Y=2.0 (should be at baseline 0?)

* iogonek (U+012F): X=482.0,Y=2.0 (should be at baseline 0?)

* iogonek (U+012F): X=600.0,Y=2.0 (should be at baseline 0?)

* iogonek (U+012F): X=482.0,Y=2.0 (should be at baseline 0?)

* iogonek (U+012F): X=482.0,Y=2.0 (should be at baseline 0?)

* iogonek (U+012F): X=1024.0,Y=2.0 (should be at baseline 0?)

* iogonek (U+012F): X=482.0,Y=2.0 (should be at baseline 0?)

* iotadieresistonos (U+0390): X=805.0,Y=2.0 (should be at baseline 0?)

* kaiSymbol (U+03D7): X=845.0,Y=-2.0 (should be at baseline 0?)

* literSign (U+2113): X=555.0,Y=1549.0 (should be at cap-height 1548?)

* literSign (U+2113): X=555.0,Y=1549.0 (should be at cap-height 1548?)

* omega (U+03C9): X=102.0,Y=2.0 (should be at baseline 0?)

* omega (U+03C9): X=921.0,Y=2.0 (should be at baseline 0?)

* omegatonos (U+03CE): X=102.0,Y=2.0 (should be at baseline 0?)

* omegatonos (U+03CE): X=921.0,Y=2.0 (should be at baseline 0?)

* uni0947 (U+0947): X=66.0,Y=1550.0 (should be at cap-height 1548?)

* uni1E09 (U+1E09): X=568.0,Y=2.0 (should be at baseline 0?)

* uni1E09 (U+1E09): X=724.0,Y=2.0 (should be at baseline 0?)

* uni1E09 (U+1E09): X=568.0,Y=2.0 (should be at baseline 0?)

* uni2116 (U+2116): X=501.0,Y=1549.0 (should be at cap-height 1548?)

* uni2116 (U+2116): X=601.0,Y=1549.0 (should be at cap-height 1548?)

* uni2116 (U+2116): X=501.0,Y=1549.0 (should be at cap-height 1548?)

* uni2116 (U+2116): X=810.0,Y=1549.0 (should be at cap-height 1548?)

* uni2116 (U+2116): X=910.0,Y=1549.0 (should be at cap-height 1548?)

* uni2116 (U+2116): X=810.0,Y=1549.0 (should be at cap-height 1548?)

* uni2116 (U+2116): X=532.0,Y=1549.0 (should be at cap-height 1548?)

* uni2116 (U+2116): X=882.0,Y=1549.0 (should be at cap-height 1548?)

* uni2116 (U+2116): X=532.0,Y=1549.0 (should be at cap-height 1548?)

* uniFB02 (U+FB02): X=240.0,Y=1547.0 (should be at cap-height 1548?)

* uniFB02 (U+FB02): X=440.0,Y=1547.0 (should be at cap-height 1548?)

* uniFB02 (U+FB02): X=240.0,Y=1547.0 (should be at cap-height 1548?)

* uniFB02 (U+FB02): X=241.0,Y=1547.0 (should be at cap-height 1548?)

* uniFB02 (U+FB02): X=668.0,Y=1547.0 (should be at cap-height 1548?)

* uniFB02 (U+FB02): X=241.0,Y=1547.0 (should be at cap-height 1548?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-direction">outline_direction</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* lambda (U+03BB) has a counter-clockwise outer contour

* lambda (U+03BB) has a counter-clockwise outer contour
</code></pre>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> List all superfamily filepaths <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#superfamily-list">superfamily/list</a></summary>
    <div>







* ℹ️ **INFO** <p>fonts/variable</p>
 [code: family-path]



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> Show hinting filesize impact. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#hinting-impact">hinting_impact</a></summary>
    <div>







* ℹ️ **INFO** <p>Hinting filesize impact:</p>
<table>
<thead>
<tr>
<th align="left"></th>
<th align="right">fonts/variable/Samaano[wdth,wght].ttf</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Dehinted Size</td>
<td align="right">210.8kb</td>
</tr>
<tr>
<td align="left">Hinted Size</td>
<td align="right">210.9kb</td>
</tr>
<tr>
<td align="left">Increase</td>
<td align="right">24 bytes</td>
</tr>
<tr>
<td align="left">Change</td>
<td align="right">0.0 %</td>
</tr>
</tbody>
</table>
 [code: size-impact]



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> Font contains all required tables? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#required-tables">required_tables</a></summary>
    <div>







* ℹ️ **INFO** <p>This font contains the following optional tables:</p>
<pre><code>- loca

- prep

- GPOS

- GSUB

- gasp
</code></pre>
 [code: optional-tables]



* ✅ **PASS** <p>Font contains all required tables.</p>
 



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> Check for presence of an ARTICLE.en_us.html file <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-has-article">googlefonts/description/has_article</a></summary>
    <div>







* ℹ️ **INFO** <p>This font doesn't have an ARTICLE.en_us.html file.</p>
 [code: missing-article]



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-gasp">googlefonts/gasp</a></summary>
    <div>







* ℹ️ **INFO** <p>These are the ppm ranges declared on the gasp table:</p>
<p>PPM &lt;= 65535:
flag = 0x0F
- Use grid-fitting
- Use grayscale rendering
- Use gridfitting with ClearType symmetric smoothing
- Use smoothing along multiple axes with ClearType®</p>
 [code: ranges]



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-meta-script-lang-tags">googlefonts/meta/script_lang_tags</a></summary>
    <div>







* ℹ️ **INFO** <p>Latn</p>
 [code: dlng-tag]



* ℹ️ **INFO** <p>Latn,Deva,Grek</p>
 [code: slng-tag]



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> Font has old ttfautohint applied? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-old-ttfautohint">googlefonts/old_ttfautohint</a></summary>
    <div>







* ℹ️ **INFO** <p>Could not detect which version of ttfautohint was used in this font. It is typically specified as a comment in the font version entries of the 'name' table. Such font version strings are currently: ['Version 2.300']</p>
 [code: version-not-detected]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check hhea.caretSlopeRise and hhea.caretSlopeRun <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-caret-slope">opentype/caret_slope</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check code page character ranges <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-code-pages">opentype/code_pages</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Font follows the family naming recommendations? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-family-naming-recommendations">opentype/family_naming_recommendations</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking font version fields (head and name table). <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-font-version">opentype/font_version</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking OS/2 fsSelection value. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-fsselection">opentype/fsselection</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Axes and named instances fall within correct ranges? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-fvar-axis-ranges-correct">opentype/fvar/axis_ranges_correct</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Axes and named instances fall within correct ranges? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-fvar-regular-coords-correct">opentype/fvar/regular_coords_correct</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check glyphs do not have duplicate components which have the same x,y coordinates. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-glyf-non-transformed-duplicate-components">opentype/glyf_non_transformed_duplicate_components</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Is there any unused data at the end of the glyf table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-glyf-unused-data">opentype/glyf_unused_data</a></summary>
    <div>







* ✅ **PASS** <p>There is no unused data at the end of the glyf table.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking post.italicAngle value. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-italic-angle">opentype/italic_angle</a></summary>
    <div>







* ✅ **PASS** <p>Value of post.italicAngle is 0.0 with style=&quot;Bold&quot;.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Is there a usable "kern" table declared in the font? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-kern-table">opentype/kern_table</a></summary>
    <div>







* ✅ **PASS** <p>Font does not declare an optional &quot;kern&quot; table.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does the font have any invalid feature tags? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-layout-valid-feature-tags">opentype/layout_valid_feature_tags</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does the font have any invalid language tags? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-layout-valid-language-tags">opentype/layout_valid_language_tags</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does the font have any invalid script tags? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-layout-valid-script-tags">opentype/layout_valid_script_tags</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does the number of glyphs in the loca table match the maxp table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-loca-maxp-num-glyphs">opentype/loca/maxp_num_glyphs</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking head.macStyle value. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-mac-style">opentype/mac_style</a></summary>
    <div>







* ✅ **PASS** <p>head macStyle ITALIC bit is properly set.</p>
 



* ✅ **PASS** <p>head macStyle BOLD bit is properly set.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> MaxAdvanceWidth is consistent with values in the Hmtx and Hhea tables? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-maxadvancewidth">opentype/maxadvancewidth</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check name table for empty records. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-name-empty-records">opentype/name/empty_records</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does full font name begin with the font family name? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-name-match-familyname-fullfont">opentype/name/match_familyname_fullfont</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Name table ID 6 (PostScript name) must be consistent across platforms. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-name-postscript-name-consistency">opentype/name/postscript_name_consistency</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check for points out of bounds. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-points-out-of-bounds">opentype/points_out_of_bounds</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> PostScript name follows OpenType specification requirements? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-postscript-name">opentype/postscript_name</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Font has correct post table version? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-post-table-version">opentype/post_table_version</a></summary>
    <div>







* ✅ **PASS** <p>Font has an acceptable post format 2.0 table version.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking direction of slnt axis angles. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-slant-direction">opentype/slant_direction</a></summary>
    <div>







* ✅ **PASS** <p>Font has no slnt axis</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking unitsPerEm value is reasonable. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-unitsperem">opentype/unitsperem</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Validates that all of the instance records in a given font have distinct data. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-varfont-distinct-instance-records">opentype/varfont/distinct_instance_records</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Validate foundry-defined design-variation axis tag names. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-varfont-foundry-defined-tag-name">opentype/varfont/foundry_defined_tag_name</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Validates that all of the instance records in a given font have the same size. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-varfont-same-size-instance-records">opentype/varfont/same_size_instance_records</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> All fvar axes have a correspondent Axis Record on STAT table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-varfont-STAT-axis-record-for-each-axis">opentype/varfont/STAT_axis_record_for_each_axis</a></summary>
    <div>







* ✅ **PASS** <p>STAT table has all necessary Axis Records.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Validates subfamilyNameID and postScriptNameID for the default instance record <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-varfont-valid-default-instance-nameids">opentype/varfont/valid_default_instance_nameids</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Validates that all of the name IDs in an instance record are within the correct range <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-varfont-valid-nameids">opentype/varfont/valid_nameids</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking if OS/2 usWeightClass matches fvar. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-weight-class-fvar">opentype/weight_class_fvar</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check if OS/2 xAvgCharWidth is correct. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-xavgcharwidth">opentype/xavgcharwidth</a></summary>
    <div>







* ✅ **PASS** <p>OS/2 xAvgCharWidth value is correct.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check that Arabic spacing symbols U+FBB2–FBC1 aren't classified as marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#arabic-spacing-symbols">arabic_spacing_symbols</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check if uppercase glyphs are vertically centered. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#caps-vertically-centered">caps_vertically_centered</a></summary>
    <div>







* ✅ **PASS** <p>Uppercase glyphs are vertically centered in the em box.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#case-mapping">case_mapping</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Color layers should have a minimum brightness. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#color-cpal-brightness">color_cpal_brightness</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does font file include unacceptable control character glyphs? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#control-chars">control_chars</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Put an empty glyph on GID 1 right after the .notdef glyph for COLRv0 fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#empty-glyph-on-gid1-for-colrv0">empty_glyph_on_gid1_for_colrv0</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#family-win-ascent-and-descent">family/win_ascent_and_descent</a></summary>
    <div>







* ✅ **PASS** <p>OS/2 usWinAscent &amp; usWinDescent values look good!</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> All name entries referenced by fvar instances exist on the name table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fvar-name-entries">fvar_name_entries</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure files are not too large. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#file-size">file_size</a></summary>
    <div>







* ✅ **PASS** <p>Font had a reasonable file size</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>







* ✅ **PASS** <p>Font familyname seems to be unique.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure that the font can be rasterized by FreeType. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#freetype-rasterizer">freetype_rasterizer</a></summary>
    <div>







* ✅ **PASS** <p>Font can be rasterized by FreeType.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure no GPOS7 lookups are present. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#gpos7">gpos7</a></summary>
    <div>







* ✅ **PASS** <p>Font has no GPOS7 lookups</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#gpos-kerning-info">gpos_kerning_info</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check that legacy accents aren't used in composite glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#legacy-accents">legacy_accents</a></summary>
    <div>







* ✅ **PASS** <p>Looks good!</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking Vertical Metric Linegaps. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#linegaps">linegaps</a></summary>
    <div>







* ✅ **PASS** <p>OS/2 sTypoLineGap and hhea lineGap are both 0.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Font contains '.notdef' as its first glyph? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#mandatory-glyphs">mandatory_glyphs</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>







* ✅ **PASS** <p>Looks good.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure small caps glyphs are available. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#missing-small-caps-glyphs">missing_small_caps_glyphs</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Are there disallowed characters in the NAME table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#name-char-restrictions">name/char_restrictions</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Combined length of family and style must not exceed 32 characters. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#name-family-and-style-max-length">name/family_and_style_max_length</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Name table records must not have trailing spaces. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#name-trailing-spaces">name/trailing_spaces</a></summary>
    <div>







* ✅ **PASS** <p>No trailing spaces on name table entries.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Description strings in the name table must not contain copyright info. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#name-no-copyright-on-description">name/no_copyright_on_description</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure glyphs do not have components which are themselves components. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#nested-components">nested_components</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking OS/2 Metrics match hhea Metrics. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#os2-metrics-match-hhea">os2_metrics_match_hhea</a></summary>
    <div>







* ✅ **PASS** <p>OS/2.sTypoAscender/Descender values match hhea.ascent/descent.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking with ots-sanitize. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#ots">ots</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure indic fonts have the Indian Rupee Sign glyph. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#rupee">rupee</a></summary>
    <div>







* ✅ **PASS** <p>Looks good!</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Font has the proper sfntVersion value? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#sfnt-version">sfnt_version</a></summary>
    <div>







* ✅ **PASS** <p>Font has the correct sfntVersion value.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure smart dropout control is enabled in "prep" table instructions. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#smart-dropout">smart_dropout</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>







* ✅ **PASS** <p>Looks good!</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check correctness of STAT table strings <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#STAT-strings">STAT_strings</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure Stylistic Sets have description. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#stylisticset-description">stylisticset_description</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check tabular widths don't have kerning. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#tabular-kerning">tabular_kerning</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure component transforms do not perform scaling or rotation. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#transformed-components">transformed_components</a></summary>
    <div>







* ✅ **PASS** <p>No glyphs had components with scaling or rotation</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking with fontTools.ttx <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#ttx-roundtrip">ttx_roundtrip</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking that the typoAscender exceeds the yMax of the /Agrave. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#typoascender-exceeds-Agrave">typoascender_exceeds_Agrave</a></summary>
    <div>







* ✅ **PASS** <p>OS/2.sTypoAscender value is greater than the yMax of /Agrave.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Font contains unique glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unique-glyphnames">unique_glyphnames</a></summary>
    <div>







* ✅ **PASS** <p>Glyph names are all unique.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Are there unwanted Apple tables? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unwanted-aat-tables">unwanted_aat_tables</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Are there unwanted tables? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unwanted-tables">unwanted_tables</a></summary>
    <div>







* ✅ **PASS** <p>There are no unwanted tables.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#valid-glyphnames">valid_glyphnames</a></summary>
    <div>







* ✅ **PASS** <p>Glyph names are all valid.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> The variable font 'wght' (Weight) axis coordinate must be 700 on the 'Bold' instance. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#varfont-bold-wght-coord">varfont/bold_wght_coord</a></summary>
    <div>







* ✅ **PASS** <p>Bold:wght is 700.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check variable font instances don't have duplicate names <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#varfont-duplicate-instance-names">varfont/duplicate_instance_names</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure the font's instances are in the correct order. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#varfont-instances-in-order">varfont/instances_in_order</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure VFs do not contain (yet) the ital axis. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#varfont-unsupported-axes">varfont/unsupported_axes</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Font contains glyphs for whitespace characters? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#whitespace-glyphs">whitespace_glyphs</a></summary>
    <div>







* ✅ **PASS** <p>Font contains glyphs for whitespace characters.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Whitespace glyphs have ink? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#whitespace-ink">whitespace_ink</a></summary>
    <div>







* ✅ **PASS** <p>There is no whitespace glyph with ink.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Space and non-breaking space have the same width? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#whitespace-widths">whitespace_widths</a></summary>
    <div>







* ✅ **PASS** <p>Space and non-breaking space have the same width.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check name ID 25 to end with "Italic" for Italic VFs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-valid-nameid25">googlefonts/metadata/valid_nameid25</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check family name for GF Guide compliance. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-family-name-compliance">googlefonts/family_name_compliance</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Name table entries should not contain line-breaks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-line-breaks">googlefonts/name/line_breaks</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Copyright notices match canonical pattern in fonts <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-font-copyright">googlefonts/font_copyright</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check OFL body text is correct. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-license-OFL-body-text">googlefonts/license/OFL_body_text</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check license file has good copyright string. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-license-OFL-copyright">googlefonts/license/OFL_copyright</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check copyright namerecords match license file. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license">googlefonts/name/license</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> License URL matches License text on name table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license-url">googlefonts/name/license_url</a></summary>
    <div>







* ✅ **PASS** <p>Font has a valid license URL in NAME table.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Name table strings must not contain the string 'Reserved Font Name'. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-rfn">googlefonts/name/rfn</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> A font repository should not include FontBakery report files <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-repo-fb-report">googlefonts/repo/fb_report</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> A font repository should not include ZIP files <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-repo-zip-files">googlefonts/repo/zip_files</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#dotted-circle">dotted_circle</a></summary>
    <div>







* ✅ **PASS** <p>All marks were anchored to dotted circle</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Validate defaults on fvar table match registered fallback names in GFAxisRegistry. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-axisregistry-fvar-axis-defaults">googlefonts/axisregistry/fvar_axis_defaults</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking file is named canonically. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-canonical-filename">googlefonts/canonical_filename</a></summary>
    <div>







* ✅ **PASS** <p>Font filename is correct, &quot;Samaano[wdth,wght].ttf&quot;.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure font has the expected color font tables. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-colorfont-tables">googlefonts/colorfont_tables</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check font names are correct <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-font-names">googlefonts/font_names</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking OS/2 fsType does not impose restrictions. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-fstype">googlefonts/fstype</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check variable font instances <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-fvar-instances">googlefonts/fvar_instances</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check Google Fonts glyph coverage. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyph-coverage">googlefonts/glyph_coverage</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Description strings in the name table must not exceed 200 characters. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-description-max-length">googlefonts/name/description_max_length</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Make sure family name does not begin with a digit. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-familyname-first-char">googlefonts/name/familyname_first_char</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Font has all mandatory 'name' table entries? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-mandatory-entries">googlefonts/name/mandatory_entries</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Version format is correct in 'name' table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-version-format">googlefonts/name/version_format</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure font can render its own name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-render-own-name">googlefonts/render_own_name</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Validate STAT particle names and values match the fallback names in GFAxisRegistry. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-STAT-axisregistry">googlefonts/STAT/axisregistry</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Stricter unitsPerEm criteria for Google Fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-unitsperem">googlefonts/unitsperem</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check a static ttf can be generated from a variable font. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-varfont-generate-static">googlefonts/varfont/generate_static</a></summary>
    <div>







* ✅ **PASS** <p>fontTools.varLib.mutator generated a static font instance</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check that variable fonts have an HVAR table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-varfont-has-HVAR">googlefonts/varfont/has_HVAR</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vendor-id">googlefonts/vendor_id</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check font follows the Google Fonts vertical metric schema <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vertical-metrics">googlefonts/vertical_metrics</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check the OS/2 usWeightClass is appropriate for the font's best SubFamily name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-weightclass">googlefonts/weightclass</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Is the CFF2 subr/gsubr call depth > 10? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-cff2-call-depth">opentype/cff2_call_depth</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_cff2</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Does the font's CFF table top dict strings fit into the ASCII range? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-cff-ascii-strings">opentype/cff_ascii_strings</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_cff</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Is the CFF subr/gsubr call depth > 10? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-cff-call-depth">opentype/cff_call_depth</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_cff</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Does the font use deprecated CFF operators or operations? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-cff-deprecated-operators">opentype/cff_deprecated_operators</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_cff</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> CFF table FontName must match name table ID 6 (PostScript name). <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-name-postscript-vs-cff">opentype/name/postscript_vs_cff</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_cff</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Checking OS/2 achVendID against configuration. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-vendor-id">opentype/vendor_id</a></summary>
    <div>







* ⏩ **SKIP** <p>Add the <code>vendor_id</code> key to a <code>fontbakery.yaml</code> file on your font project directory to enable this check.
You'll also need to use the <code>--configuration</code> flag when invoking fontbakery.</p>
 



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Each font in set of sibling families must have the same set of vertical metrics values. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#superfamily-vertical-metrics">superfamily/vertical_metrics</a></summary>
    <div>







* ⏩ **SKIP** <p>Sibling families were not detected.</p>
 



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check that glyph for U+0675 ARABIC LETTER HIGH HAMZA is not a mark. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#arabic-high-hamza">arabic_high_hamza</a></summary>
    <div>







* ⏩ **SKIP** <p>This check will only run on fonts that have both glyphs U+0621 and U+0675</p>
 [code: glyphs-missing]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Does the font contain chws and vchw features? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#cjk-chws-feature">cjk_chws_feature</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_cjk_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Any CJK font should contain at least a minimal set of 150 CJK characters. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#cjk-not-enough-glyphs">cjk_not_enough_glyphs</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_claiming_to_be_cjk_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: not is_variable_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> PPEM must be an integer on hinted fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#integer-ppem-if-hinted">integer_ppem_if_hinted</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_hinted</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check name table IDs 1, 2, 16, 17 to conform to Italic style. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#name-italic-names">name/italic_names</a></summary>
    <div>







* ⏩ **SKIP** <p>Font is not Italic.</p>
 



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Ensure 'smcp' (small caps) lookups are defined before ligature lookups in the 'GSUB' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#smallcaps-before-ligatures">smallcaps_before_ligatures</a></summary>
    <div>







* ⏩ **SKIP** <p>Font lacks 'smcp' or 'liga' features.</p>
 



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Checking STAT table entries in static fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#STAT-in-statics">STAT_in_statics</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: not is_variable_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Ensure VFs with duplexed axes do not vary horizontal advance. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#varfont-duplexed-axis-reflow">varfont/duplexed_axis_reflow</a></summary>
    <div>







* ⏩ **SKIP** <p>This font has no duplexed axes</p>
 [code: no-relevant-axes]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Validate METADATA.pb axes values are within gf_axisregistry bounds. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-axisregistry-bounds">googlefonts/metadata/axisregistry_bounds</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Validate METADATA.pb axes tags are defined in gf_axisregistry. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-axisregistry-valid-tags">googlefonts/metadata/axisregistry_valid_tags</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Does METADATA.pb copyright field contain broken links? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-broken-links">googlefonts/metadata/broken_links</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Font styles are named canonically? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-canonical-style-names">googlefonts/metadata/canonical_style_names</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Check that font weight has a canonical value. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-canonical-weight-value">googlefonts/metadata/canonical_weight_value</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check samples can be rendered. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-can-render-samples">googlefonts/metadata/can_render_samples</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Ensure METADATA.pb category field is valid. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-category">googlefonts/metadata/category</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check if category on METADATA.pb matches what can be inferred from the family name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-category-hints">googlefonts/metadata/category_hints</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Validate VF axes match the ones declared on METADATA.pb. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-consistent-axis-enumeration">googlefonts/metadata/consistent_axis_enumeration</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Check URL on copyright string is the same as in repository_url field. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-consistent-repo-urls">googlefonts/metadata/consistent_repo_urls</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Validate 'date_added' field on METADATA.pb. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-date-added">googlefonts/metadata/date_added</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Designers are listed correctly on the Google Fonts catalog? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-designer-profiles">googlefonts/metadata/designer_profiles</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Multiple values in font designer field in METADATA.pb must be separated by commas. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-designer-values">googlefonts/metadata/designer_values</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> At least one designer is declared in METADATA.pb <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-empty-designer">googlefonts/metadata/empty_designer</a></summary>
    <div>







* ⏩ **SKIP** <p>No applicable arguments</p>
 [code: no-arguments]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Ensure METADATA.pb does not use escaped strings. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-escaped-strings">googlefonts/metadata/escaped_strings</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: metadata_file</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check font family directory name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-family-directory-name">googlefonts/metadata/family_directory_name</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check that METADATA.pb family values are all the same. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-familyname">googlefonts/metadata/familyname</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Font filenames match font.filename entries? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-filenames">googlefonts/metadata/filenames</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Ensure there is a regular style defined in METADATA.pb. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-has-regular">googlefonts/metadata/has_regular</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check METADATA.pb includes production subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-includes-production-subsets">googlefonts/metadata/includes_production_subsets</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata, listed_on_gfonts_api</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb font.filename and font.post_script_name fields have equivalent values? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-match-filename-postscript">googlefonts/metadata/match_filename_postscript</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata, not is_variable_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb font.full_name and font.post_script_name fields have equivalent values ? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-match-fullname-postscript">googlefonts/metadata/match_fullname_postscript</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Check font name is the same as family name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-match-name-familyname">googlefonts/metadata/match_name_familyname</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata, font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb weight matches postScriptName for static fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-match-weight-postscript">googlefonts/metadata/match_weight_postscript</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata, not is_variable_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb should contain at least "menu" and "latin" subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-menu-and-latin">googlefonts/metadata/menu_and_latin</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Validate family.minisite_url field. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-minisite-url">googlefonts/metadata/minisite_url</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb font.name and font.full_name fields match the values declared on the name table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-nameid-family-and-full-names">googlefonts/metadata/nameid/family_and_full_names</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb font.name value should be same as the family name declared on the name table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-nameid-font-name">googlefonts/metadata/nameid/font_name</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Checks METADATA.pb font.post_script_name matches postscript name declared on the name table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-nameid-post-script-name">googlefonts/metadata/nameid/post_script_name</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check METADATA.pb parse correctly. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-parses">googlefonts/metadata/parses</a></summary>
    <div>







* ⏩ **SKIP** <p>Font family at 'fonts/variable' lacks a METADATA.pb file.</p>
 [code: file-not-found]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Check for primary_script <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-primary-script">googlefonts/metadata/primary_script</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Regular should be 400. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-regular-is-400">googlefonts/metadata/regular_is_400</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata, has_regular_style</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check METADATA.pb file only contains a single CJK subset. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-single-cjk-subset">googlefonts/metadata/single_cjk_subset</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb subsets should be alphabetically ordered. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-subsets-order">googlefonts/metadata/subsets_order</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Ensure METADATA.pb lists all font binaries. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-undeclared-fonts">googlefonts/metadata/undeclared_fonts</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: check if fonts field only has unique "full_name" values. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unique-full-name-values">googlefonts/metadata/unique_full_name_values</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: check if fonts field only contains unique style:weight pairs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unique-weight-style-pairs">googlefonts/metadata/unique_weight_style_pairs</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check for METADATA subsets with zero support. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unsupported-subsets">googlefonts/metadata/unsupported_subsets</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb font.filename field contains font name in right format? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-valid-filename-values">googlefonts/metadata/valid_filename_values</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb font.full_name field contains font name in right format? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-valid-full-name-values">googlefonts/metadata/valid_full_name_values</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb font.post_script_name field contains font name in right format? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-valid-post-script-name-values">googlefonts/metadata/valid_post_script_name_values</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check METADATA.pb font weights are correct. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-weightclass">googlefonts/metadata/weightclass</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Does DESCRIPTION file contain broken links? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-broken-links">googlefonts/description/broken_links</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: description_and_article_html</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> DESCRIPTION.en_us.html should end in a linebreak. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-eof-linebreak">googlefonts/description/eof_linebreak</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: description</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> On a family update, the DESCRIPTION.en_us.html file should ideally also be updated. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-family-update">googlefonts/description/family_update</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: description</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Does DESCRIPTION file contain a upstream Git repo URL? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-git-url">googlefonts/description/git_url</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: description_html</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check the description doesn't contain unsupported html elements <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-has-unsupported-elements">googlefonts/description/has_unsupported_elements</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: description_and_article</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> DESCRIPTION.en_us.html must have more than 200 bytes. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-min-length">googlefonts/description/min_length</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: description</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> URLs on DESCRIPTION file must not display http(s) prefix. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-urls">googlefonts/description/urls</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: description_and_article_html</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Is this a proper HTML snippet? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-valid-html">googlefonts/description/valid_html</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: description_and_article</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check font has a license. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-family-has-license">googlefonts/family/has_license</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: gfonts_repo_structure</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Copyright notice is the same in all fonts? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-copyright">googlefonts/metadata/copyright</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb license is "APACHE2", "UFL" or "OFL"? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-license">googlefonts/metadata/license</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Copyright notice on METADATA.pb should not contain 'Reserved Font Name'. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-reserved-font-name">googlefonts/metadata/reserved_font_name</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check upstream.yaml file contains all required fields <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-repo-upstream-yaml-has-required-fields">googlefonts/repo/upstream_yaml_has_required_fields</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: upstream_yaml</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> A static fonts directory, if present, must contain manually hinted fonts <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-repo-vf-has-static-fonts">googlefonts/repo/vf_has_static_fonts</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: gfonts_repo_structure</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check that no collisions are found while shaping <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#shaping-collides">shaping/collides</a></summary>
    <div>







* ⏩ **SKIP** <p>Shaping test directory not defined in configuration file</p>
 



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check that no forbidden glyphs are found while shaping <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#shaping-forbidden">shaping/forbidden</a></summary>
    <div>







* ⏩ **SKIP** <p>Shaping test directory not defined in configuration file</p>
 



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check that texts shape as per expectation <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#shaping-regression">shaping/regression</a></summary>
    <div>







* ⏩ **SKIP** <p>Shaping test directory not defined in configuration file</p>
 



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-colinear-vectors">outline_colinear_vectors</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: not is_variable_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-jaggy-segments">outline_jaggy_segments</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: not is_variable_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-semi-vertical">outline_semi_vertical</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: not is_variable_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Are any segments inordinately short? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-short-segments">outline_short_segments</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: not is_variable_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check if the axes match between the font and the Google Fonts version. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-axes-match">googlefonts/axes_match</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: remote_style</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check font follows the Google Fonts CJK vertical metric schema <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-cjk-vertical-metrics">googlefonts/cjk_vertical_metrics</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_cjk_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check if the vertical metrics of a CJK family are similar to the same family hosted on Google Fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-cjk-vertical-metrics-regressions">googlefonts/cjk_vertical_metrics_regressions</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_cjk_font, regular_remote_style</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Font has ttfautohint params? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-has-ttfautohint-params">googlefonts/has_ttfautohint_params</a></summary>
    <div>







* ⏩ **SKIP** <p>Font appears to our heuristic as not hinted using ttfautohint.</p>
 [code: not-hinted]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vertical-metrics-regressions">googlefonts/vertical_metrics_regressions</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: regular_remote_style</p>
 [code: unfulfilled-conditions]



</div>
</details>
</div>
</details>

<details><summary>[17] Family checks</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure VFs have 'ital' STAT axis. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-STAT-ital-axis">opentype/STAT/ital_axis</a></summary>
    <div>







* 🔥 **FAIL** <p>Font fonts/variable/Samaano[wdth,wght].ttf lacks an 'ital' axis in the STAT table.</p>
 [code: missing-ital-axis]



* 🔥 **FAIL** <p>Font fonts/variable/Samaano-Italic[wdth,wght].ttf lacks an 'ital' axis in the STAT table.</p>
 [code: missing-ital-axis]



* ⏩ **SKIP** <p>Font {font.file} doesn't have an ital axis</p>
 



* ⏩ **SKIP** <p>Font {font.file} doesn't have an ital axis</p>
 



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> Check axis ordering on the STAT table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-STAT-axis-order">googlefonts/STAT/axis_order</a></summary>
    <div>







* ℹ️ **INFO** <p>None of the fonts lack a STAT table.</p>
<pre><code>And these are the most common STAT axis orderings:
('slnt-wdth-wght', 1)
('wdth-wght', 1)
</code></pre>
 [code: summary]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check that OS/2.fsSelection bold & italic settings are unique for each NameID1 <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-family-bold-italic-unique-for-nameid1">opentype/family/bold_italic_unique_for_nameid1</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Verify that family names in the name table are consistent across all fonts in the family. Checks Typographic Family name (nameID 16) if present, otherwise uses Font Family name (nameID 1) <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-family-consistent-family-name">opentype/family/consistent_family_name</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Make sure all font files have the same version value. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-family-equal-font-versions">opentype/family/equal_font_versions</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Verify that each group of fonts with the same nameID 1 has maximum of 4 fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-family-max-4-fonts-per-family-name">opentype/family/max_4_fonts_per_family_name</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Fonts have consistent PANOSE family type? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-family-panose-familytype">opentype/family/panose_familytype</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Fonts have consistent underline thickness? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-family-underline-thickness">opentype/family/underline_thickness</a></summary>
    <div>







* ✅ **PASS** <p>Fonts have consistent underline thickness.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check that family axis ranges are indentical <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-varfont-family-axis-ranges">opentype/varfont/family_axis_ranges</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking all files are in the same directory. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#family-single-directory">family/single_directory</a></summary>
    <div>







* ✅ **PASS** <p>All files are in the same directory.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Each font in a family must have the same set of vertical metrics values. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#family-vertical-metrics">family/vertical_metrics</a></summary>
    <div>







* ✅ **PASS** <p>Vertical metrics are the same across the family.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure that all variable font files have the same set of axes and axis ranges. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#varfont-consistent-axes">varfont/consistent_axes</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure Italic styles have Roman counterparts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-family-italics-have-roman-counterparts">googlefonts/family/italics_have_roman_counterparts</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> All tabular figures must have the same width across the RIBBI-family. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-family-tnum-horizontal-metrics">googlefonts/family/tnum_horizontal_metrics</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-use-typo-metrics">googlefonts/use_typo_metrics</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Fonts have equal codepoint coverage <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-family-equal-codepoint-coverage">googlefonts/family/equal_codepoint_coverage</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: stylenames_are_canonical</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Directory name in GFonts repo structure must match NameID 1 of the regular. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-repo-dirname-matches-nameid-1">googlefonts/repo/dirname_matches_nameid_1</a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: gfonts_repo_structure</p>
 [code: unfulfilled-conditions]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 7 | 30 | 169 | 15 | 234 | 0 | 
| 0% | 0% | 2% | 7% | 37% | 3% | 51% | 0% | 



**Note:** The following loglevels were omitted in this report:


* DEBUG
