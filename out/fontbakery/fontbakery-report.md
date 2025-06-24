## FontBakery report

fontbakery version: 1.0.0





## Experimental checks

These won't break the CI job for now, but will become effective after some time if nobody raises any concern.


<details><summary>[1] Samaano[slnt,wdth,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Check base characters have non-zero advance width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#base-has-width">base_has_width</a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs had zero advance width:
- anoteleia (U+0387)</p>
<pre><code>- uni1FBE (U+1FBE)
</code></pre>
 [code: zero-width-bases]



</div>
</details>
</div>
</details>




## All other checks



<details><summary>[218] Samaano[slnt,wdth,wght].ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 💥 **ERROR** <p>Failed with TypeError: argument 'lang': 'NoneType' object cannot be converted to 'Language'</p>
<pre><code>  File &quot;/media/artim/home/@home/artim/devel/samaano-fonts/venv-test/lib/python3.10/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/media/artim/home/@home/artim/devel/samaano-fonts/venv-test/lib/python3.10/site-packages/fontbakery/checks/vendorspecific/googlefonts/glyphsets/shape_languages.py&quot;, line 49, in check_glyphsets_shape_languages
    reporter = shaperglot_checker.check(shaperglot_languages[language_code])

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>







* 🔥 **FAIL** <p>On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead.</p>
 [code: mono-bad-post-isFixedPitch]



* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1417 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#valid-glyphnames">valid_glyphnames</a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyph names do not comply with naming conventions: Alpha-latin, Beta-latin, Gamma-latin, Iota-latin, Omega-latin, Upsilon-latin, alpha-latin, beta-latin, gamma-latin, iota-latin, omega-latin and upsilon-latin</p>
<p>A glyph name must be entirely comprised of characters from the following set: A-Z a-z 0-9 .(period) <em>(underscore). A glyph name must not start with a digit or period. There are a few exceptions such as the special glyph &quot;.notdef&quot;. The glyph names &quot;twocents&quot;, &quot;a1&quot;, and &quot;</em>&quot; are all valid, while &quot;2cents&quot; and &quot;.twocents&quot; are not.</p>
 [code: found-invalid-names]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check font names are correct <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-font-names">googlefonts/font_names</a></summary>
    <div>







* 🔥 **FAIL** <p>Font names are incorrect:</p>
<table>
<thead>
<tr>
<th align="left">nameID</th>
<th align="left">current</th>
<th align="left">expected</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Family Name</td>
<td align="left"><strong>Samaano Bold</strong></td>
<td align="left"><strong>Samaano</strong></td>
</tr>
<tr>
<td align="left">Subfamily Name</td>
<td align="left">Bold</td>
<td align="left">Bold</td>
</tr>
<tr>
<td align="left">Full Name</td>
<td align="left">Samaano Bold</td>
<td align="left">Samaano Bold</td>
</tr>
<tr>
<td align="left">Postscript Name</td>
<td align="left">Samaano-Bold</td>
<td align="left">Samaano-Bold</td>
</tr>
<tr>
<td align="left">Typographic Family Name</td>
<td align="left"><strong>Samaano</strong></td>
<td align="left"><strong>N/A</strong></td>
</tr>
<tr>
<td align="left">Typographic Subfamily Name</td>
<td align="left"><strong>Bold</strong></td>
<td align="left"><strong>N/A</strong></td>
</tr>
</tbody>
</table>
 [code: bad-names]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Validate STAT particle names and values match the fallback names in GFAxisRegistry. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-STAT-axisregistry">googlefonts/STAT/axisregistry</a></summary>
    <div>







* 🔥 **FAIL** <p>On the font variation axis 'slnt', the name 'Oblique' is not among the expected ones (Default) according to the Google Fonts Axis Registry.</p>
 [code: invalid-name]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-mark-chars">opentype/gdef_mark_chars</a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
acutemacroncomb (U+1DC7), gravemacroncomb (U+1DC5), macronacutecomb (U+1DC4), macrongravecomb (U+1DC6), uni0329 (U+0329), uni0955 (U+0955), uni0BC0 (U+0BC0) and uni0BCD (U+0BCD)</p>
 [code: mark-chars]



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
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#gpos-kerning-info">gpos_kerning_info</a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning information.</p>
 [code: lacks-kern-info]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Detect any interpolation issues in the font. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#interpolation-issues">interpolation_issues</a></summary>
    <div>







* ⚠️ **WARN** <p>Interpolation issues were found in the font:</p>
<pre><code>- Contour 1 in glyph 'uni0312': becomes underweight between slnt=-20,wdth=100,wght=100 and slnt=0,wdth=200,wght=100.

- Contour order differs in glyph 'Ramshorn': [0, 1, 2] in slnt=-20,wdth=100,wght=100, [1, 0, 2] in slnt=0,wdth=200,wght=100.

- Contour order differs in glyph 'Gamma-latin': [0, 1, 2] in slnt=-20,wdth=100,wght=100, [1, 0, 2] in slnt=0,wdth=200,wght=100.

- Contour 5 in glyph 'whook': becomes underweight between slnt=-20,wdth=100,wght=100 and slnt=0,wdth=200,wght=100.

- Contour 5 in glyph 'dhook': becomes underweight between slnt=-20,wdth=100,wght=100 and slnt=0,wdth=200,wght=100.

- Contour 5 in glyph 'phook': becomes underweight between slnt=-20,wdth=100,wght=100 and slnt=0,wdth=200,wght=100.

- Contour 3 in glyph 'thook': becomes underweight between slnt=0,wdth=100,wght=700 and slnt=-20,wdth=100,wght=700.

- Contour 4 in glyph 'thook': becomes underweight between slnt=0,wdth=100,wght=700 and slnt=-20,wdth=100,wght=700.

- Contour 3 in glyph 'thook': becomes underweight between slnt=-20,wdth=100,wght=700 and slnt=0,wdth=200,wght=700.

- Contour 4 in glyph 'thook': becomes underweight between slnt=-20,wdth=100,wght=700 and slnt=0,wdth=200,wght=700.

- Contour 3 in glyph 'thook': becomes underweight between slnt=-20,wdth=100,wght=100 and slnt=0,wdth=200,wght=100.

- Contour 4 in glyph 'thook': becomes underweight between slnt=-20,wdth=100,wght=100 and slnt=0,wdth=200,wght=100.

- Contour 3 in glyph 'thook': becomes underweight between slnt=0,wdth=200,wght=100 and slnt=-20,wdth=200,wght=100.

- Contour 4 in glyph 'thook': becomes underweight between slnt=0,wdth=200,wght=100 and slnt=-20,wdth=200,wght=100.

- Contour 4 in glyph 'hhook': becomes underweight between slnt=-20,wdth=100,wght=100 and slnt=0,wdth=200,wght=100.

- Contour 4 in glyph 'khook': becomes underweight between slnt=-20,wdth=100,wght=100 and slnt=0,wdth=200,wght=100.

- Contour 6 in glyph 'ghook': becomes underweight between slnt=-20,wdth=100,wght=100 and slnt=0,wdth=200,wght=100.

- Contour 5 in glyph 'Yhook': becomes underweight between slnt=-20,wdth=100,wght=100 and slnt=0,wdth=200,wght=100.

- Contour 4 start point differs in glyph 'uni0BAF' between location slnt=-20,wdth=200,wght=700 and location slnt=-20,wdth=100,wght=100

- Contour 4 start point differs in glyph 'uni0BAF' between location slnt=-20,wdth=100,wght=100 and location slnt=0,wdth=200,wght=100

- Contour order differs in glyph 'ramshorn': [0, 1, 2] in slnt=-20,wdth=100,wght=100, [1, 0, 2] in slnt=0,wdth=200,wght=100.

- Contour 1 start point differs in glyph 'ramshorn' between location slnt=-20,wdth=100,wght=100 and location slnt=0,wdth=200,wght=100

- Contour 4 in glyph 'Fhook': becomes underweight between slnt=-20,wdth=100,wght=100 and slnt=0,wdth=200,wght=100.

- Contour 7 in glyph 'uni20BF': becomes underweight between slnt=0,wdth=100,wght=100 and slnt=-20,wdth=200,wght=700.

- Contour 5 in glyph 'Whook': becomes underweight between slnt=-20,wdth=100,wght=100 and slnt=0,wdth=200,wght=100.

- Contour order differs in glyph 'blinebelow': [0, 1, 2, 3, 4] in slnt=0,wdth=200,wght=100, [4, 1, 2, 3, 0] in slnt=-20,wdth=200,wght=100.

- Contour 4 in glyph 'Nhookleft': becomes underweight between slnt=-20,wdth=100,wght=100 and slnt=0,wdth=200,wght=100.

- Contour 3 in glyph 'Dcroat': becomes underweight between slnt=0,wdth=100,wght=100 and slnt=-20,wdth=200,wght=700.

- Contour 5 in glyph 'yhook': becomes underweight between slnt=-20,wdth=100,wght=100 and slnt=0,wdth=200,wght=100.

- Contour 5 in glyph 'bhook': becomes underweight between slnt=-20,wdth=100,wght=100 and slnt=0,wdth=200,wght=100.

- Contour 4 in glyph 'chook': becomes underweight between slnt=-20,wdth=100,wght=100 and slnt=0,wdth=200,wght=100.

- Contour 3 in glyph 'Eth': becomes underweight between slnt=0,wdth=100,wght=100 and slnt=-20,wdth=200,wght=700.

- Contour order differs in glyph 'gamma-latin': [0, 1, 2] in slnt=-20,wdth=100,wght=100, [1, 0, 2] in slnt=0,wdth=200,wght=100.

- Contour 5 in glyph 'Ghook': becomes underweight between slnt=-20,wdth=100,wght=100 and slnt=0,wdth=200,wght=100.

- Contour 4 in glyph 'Chook': becomes underweight between slnt=-20,wdth=100,wght=100 and slnt=0,wdth=200,wght=100.

- Contour 4 in glyph 'nhookleft': becomes underweight between slnt=-20,wdth=100,wght=100 and slnt=0,wdth=200,wght=100.
</code></pre>
 [code: interpolation-issues]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#ligature-carets">ligature_carets</a></summary>
    <div>







* ⚠️ **WARN** <p>This font lacks caret positioning values for these ligature glyphs:
- j_uni0308</p>
<pre><code>- j_uni0311

- uni1ECB_uni0301
</code></pre>
 [code: incomplete-caret-pos-data]



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

* Beta-latin (U+A7B4): L&lt;&lt;433.0,1023.0&gt;--&lt;433.0,820.0&gt;&gt; has the same coordinates as a previous segment.

* Beta-latin (U+A7B4): L&lt;&lt;442.0,766.0&gt;--&lt;442.0,567.0&gt;&gt; has the same coordinates as a previous segment.

* Beta-latin (U+A7B4): L&lt;&lt;433.0,1537.0&gt;--&lt;433.0,1331.0&gt;&gt; has the same coordinates as a previous segment.

* Bhook (U+0181): L&lt;&lt;433.0,1023.0&gt;--&lt;433.0,820.0&gt;&gt; has the same coordinates as a previous segment.

* Bhook (U+0181): L&lt;&lt;442.0,766.0&gt;--&lt;442.0,567.0&gt;&gt; has the same coordinates as a previous segment.

* Bhook (U+0181): L&lt;&lt;433.0,1537.0&gt;--&lt;433.0,1331.0&gt;&gt; has the same coordinates as a previous segment.

* Blinebelow (U+1E06): L&lt;&lt;433.0,1023.0&gt;--&lt;433.0,820.0&gt;&gt; has the same coordinates as a previous segment.

* Blinebelow (U+1E06): L&lt;&lt;442.0,766.0&gt;--&lt;442.0,567.0&gt;&gt; has the same coordinates as a previous segment.

* Blinebelow (U+1E06): L&lt;&lt;433.0,1537.0&gt;--&lt;433.0,1331.0&gt;&gt; has the same coordinates as a previous segment.

* Btopbar (U+0182): L&lt;&lt;442.0,766.0&gt;--&lt;442.0,567.0&gt;&gt; has the same coordinates as a previous segment.

* D.circled (U+24B9): L&lt;&lt;480.0,1084.0&gt;--&lt;480.0,1004.0&gt;&gt; has the same coordinates as a previous segment.

* Ebreve (U+0114): L&lt;&lt;655.0,1769.0&gt;--&lt;655.0,1656.0&gt;&gt; has the same coordinates as a previous segment.

* Ebreve (U+0114): L&lt;&lt;331.0,1769.0&gt;--&lt;331.0,1656.0&gt;&gt; has the same coordinates as a previous segment.

* Ecedillabreve (U+1E1C): L&lt;&lt;655.0,1769.0&gt;--&lt;655.0,1656.0&gt;&gt; has the same coordinates as a previous segment.

* Ecedillabreve (U+1E1C): L&lt;&lt;331.0,1769.0&gt;--&lt;331.0,1656.0&gt;&gt; has the same coordinates as a previous segment.

* Etildebelow (U+1E1A): L&lt;&lt;381.0,-134.0&gt;--&lt;381.0,-233.0&gt;&gt; has the same coordinates as a previous segment.

* Etildebelow (U+1E1A): L&lt;&lt;731.0,-294.0&gt;--&lt;731.0,-195.0&gt;&gt; has the same coordinates as a previous segment.

* Euro (U+20AC): L&lt;&lt;324.0,179.0&gt;--&lt;514.0,179.0&gt;&gt; has the same coordinates as a previous segment.

* Gbreve (U+011E): L&lt;&lt;687.0,1777.0&gt;--&lt;687.0,1664.0&gt;&gt; has the same coordinates as a previous segment.

* Gbreve (U+011E): L&lt;&lt;363.0,1777.0&gt;--&lt;363.0,1664.0&gt;&gt; has the same coordinates as a previous segment.

* Ibreve (U+012C): L&lt;&lt;655.0,1769.0&gt;--&lt;655.0,1656.0&gt;&gt; has the same coordinates as a previous segment.

* Ibreve (U+012C): L&lt;&lt;331.0,1769.0&gt;--&lt;331.0,1656.0&gt;&gt; has the same coordinates as a previous segment.

* Itilde (U+0128): L&lt;&lt;282.0,1857.0&gt;--&lt;282.0,1758.0&gt;&gt; has the same coordinates as a previous segment.

* Itilde (U+0128): L&lt;&lt;632.0,1697.0&gt;--&lt;632.0,1796.0&gt;&gt; has the same coordinates as a previous segment.

* Itildebelow (U+1E2C): L&lt;&lt;385.0,-147.0&gt;--&lt;385.0,-246.0&gt;&gt; has the same coordinates as a previous segment.

* Itildebelow (U+1E2C): L&lt;&lt;735.0,-307.0&gt;--&lt;735.0,-208.0&gt;&gt; has the same coordinates as a previous segment.

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

* Utildebelow (U+1E74): L&lt;&lt;398.0,-138.0&gt;--&lt;398.0,-237.0&gt;&gt; has the same coordinates as a previous segment.

* Utildebelow (U+1E74): L&lt;&lt;748.0,-298.0&gt;--&lt;748.0,-199.0&gt;&gt; has the same coordinates as a previous segment.

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

* breveinvertedbelowcomb (U+032F): L&lt;&lt;-185.0,87.0&gt;--&lt;-185.0,155.0&gt;&gt; has the same coordinates as a previous segment.

* breveinvertedbelowcomb (U+032F): L&lt;&lt;139.0,87.0&gt;--&lt;139.0,155.0&gt;&gt; has the same coordinates as a previous segment.

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

* itildebelow (U+1E2D): L&lt;&lt;389.0,-142.0&gt;--&lt;389.0,-241.0&gt;&gt; has the same coordinates as a previous segment.

* itildebelow (U+1E2D): L&lt;&lt;739.0,-302.0&gt;--&lt;739.0,-203.0&gt;&gt; has the same coordinates as a previous segment.

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

* radical (U+221A): L&lt;&lt;688.0,117.0&gt;--&lt;504.0,117.0&gt;&gt; has the same coordinates as a previous segment.

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

* tildebelowcomb (U+0330): L&lt;&lt;-164.0,73.0&gt;--&lt;-164.0,-26.0&gt;&gt; has the same coordinates as a previous segment.

* tildebelowcomb (U+0330): L&lt;&lt;186.0,-87.0&gt;--&lt;186.0,12.0&gt;&gt; has the same coordinates as a previous segment.

* tildecomb (U+0303): L&lt;&lt;-194.0,994.0&gt;--&lt;-194.0,895.0&gt;&gt; has the same coordinates as a previous segment.

* tildecomb (U+0303): L&lt;&lt;156.0,834.0&gt;--&lt;156.0,933.0&gt;&gt; has the same coordinates as a previous segment.

* ubreve (U+016D): L&lt;&lt;625.0,1274.0&gt;--&lt;625.0,1161.0&gt;&gt; has the same coordinates as a previous segment.

* ubreve (U+016D): L&lt;&lt;301.0,1274.0&gt;--&lt;301.0,1161.0&gt;&gt; has the same coordinates as a previous segment.

* undertie (U+203F): L&lt;&lt;750.0,-252.0&gt;--&lt;750.0,-391.0&gt;&gt; has the same coordinates as a previous segment.

* undertie (U+203F): L&lt;&lt;304.0,-252.0&gt;--&lt;304.0,-391.0&gt;&gt; has the same coordinates as a previous segment.

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

* uni0B87 (U+0B87): L&lt;&lt;339.0,57.0&gt;--&lt;539.0,53.0&gt;&gt; has the same coordinates as a previous segment.

* uni0B87 (U+0B87): L&lt;&lt;211.0,-410.0&gt;--&lt;11.0,-410.0&gt;&gt; has the same coordinates as a previous segment.

* uni0B90 (U+0B90): L&lt;&lt;685.0,556.0&gt;--&lt;880.0,423.0&gt;&gt; has the same coordinates as a previous segment.

* uni0B90 (U+0B90): L&lt;&lt;60.0,426.0&gt;--&lt;263.0,257.0&gt;&gt; has the same coordinates as a previous segment.

* uni0B95_uni0BB7.akhn: L&lt;&lt;501.0,679.0&gt;--&lt;601.0,679.0&gt;&gt; has the same coordinates as a previous segment.

* uni0B95_uni0BC2: L&lt;&lt;803.0,288.0&gt;--&lt;932.0,287.0&gt;&gt; has the same coordinates as a previous segment.

* uni0B9C (U+0B9C): L&lt;&lt;685.0,556.0&gt;--&lt;880.0,423.0&gt;&gt; has the same coordinates as a previous segment.

* uni0B9C (U+0B9C): L&lt;&lt;60.0,426.0&gt;--&lt;263.0,257.0&gt;&gt; has the same coordinates as a previous segment.

* uni0BB0 (U+0BB0): L&lt;&lt;637.0,-15.0&gt;--&lt;841.0,-124.0&gt;&gt; has the same coordinates as a previous segment.

* uni0BB4 (U+0BB4): L&lt;&lt;810.0,661.0&gt;--&lt;1010.0,661.0&gt;&gt; has the same coordinates as a previous segment.

* uni0BB5 (U+0BB5): L&lt;&lt;438.0,682.0&gt;--&lt;637.0,680.0&gt;&gt; has the same coordinates as a previous segment.

* uni0BB9 (U+0BB9): L&lt;&lt;325.0,682.0&gt;--&lt;465.0,680.0&gt;&gt; has the same coordinates as a previous segment.

* uni0BF1 (U+0BF1): L&lt;&lt;283.0,1028.0&gt;--&lt;281.0,1216.0&gt;&gt; has the same coordinates as a previous segment.

* uni0BF3 (U+0BF3): L&lt;&lt;438.0,682.0&gt;--&lt;637.0,680.0&gt;&gt; has the same coordinates as a previous segment.

* uni0BF4 (U+0BF4): L&lt;&lt;931.0,1532.0&gt;--&lt;931.0,1628.0&gt;&gt; has the same coordinates as a previous segment.

* uni0BF5 (U+0BF5): L&lt;&lt;360.0,676.0&gt;--&lt;457.0,678.0&gt;&gt; has the same coordinates as a previous segment.

* uni0BF7 (U+0BF7): L&lt;&lt;856.0,213.0&gt;--&lt;916.0,212.0&gt;&gt; has the same coordinates as a previous segment.

* uni0BF9 (U+0BF9): L&lt;&lt;625.0,1510.0&gt;--&lt;725.0,1509.0&gt;&gt; has the same coordinates as a previous segment.

* uni0BFA (U+0BFA): L&lt;&lt;817.0,1451.0&gt;--&lt;897.0,1450.0&gt;&gt; has the same coordinates as a previous segment.

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

* utildebelow (U+1E75): L&lt;&lt;364.0,-193.0&gt;--&lt;364.0,-292.0&gt;&gt; has the same coordinates as a previous segment.

* utildebelow (U+1E75): L&lt;&lt;714.0,-353.0&gt;--&lt;714.0,-254.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- brevecomb_acutecomb

- brevecomb_gravecomb

- brevecomb_hookabovecomb

- brevecomb_tildecomb

- circumflexcomb_acutecomb

- circumflexcomb_gravecomb

- circumflexcomb_hookabovecomb

- circumflexcomb_tildecomb

- idotaccent

- uni0B99_uni0BC1

- uni0B99_uni0BC2

- uni0B9A_uni0BC1

- uni0B9A_uni0BC2

- uni0B9E_uni0BC1

- uni0B9E_uni0BC2

- uni0BC1.alt

- uni0BC2.alt
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
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, cherokee, tifinagh, math</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: glagolitic, math, elbasan, gothic, coptic</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: syriac, todhri, hebrew, tai-le, duployan, math, canadian-aboriginal, tifinagh, old-permic, coptic, malayalam</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+030D COMBINING VERTICAL LINE ABOVE: try adding sunuwar</li>
<li>U+030F COMBINING DOUBLE GRAVE ACCENT: not included in any glyphset definition</li>
<li>U+0310 COMBINING CANDRABINDU: try adding one of: sunuwar, math</li>
<li>U+0311 COMBINING INVERTED BREVE: try adding one of: coptic, todhri</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: cherokee, duployan, syriac</li>
<li>U+0325 COMBINING RING BELOW: try adding syriac</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032D COMBINING CIRCUMFLEX ACCENT BELOW: try adding one of: sunuwar, syriac</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+032F COMBINING INVERTED BREVE BELOW: try adding math</li>
<li>U+0330 COMBINING TILDE BELOW: try adding one of: cherokee, syriac, math</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: syriac, cherokee, caucasian-albanian, tifinagh, gothic, thai, sunuwar</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+035F COMBINING DOUBLE MACRON BELOW: not included in any glyphset definition</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+1DC4 COMBINING MACRON-ACUTE: not included in any glyphset definition</li>
<li>U+1DC5 COMBINING GRAVE-MACRON: not included in any glyphset definition</li>
<li>U+1DC6 COMBINING MACRON-GRAVE: not included in any glyphset definition</li>
<li>U+1DC7 COMBINING ACUTE-MACRON: not included in any glyphset definition</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+203F UNDERTIE: not included in any glyphset definition</li>
<li>U+2042 ASTERISM: not included in any glyphset definition</li>
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
<li>U+20C1 : not included in any glyphset definition</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math</li>
<li>U+2195 UP DOWN ARROW: try adding one of: symbols, math</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: yi, symbols, math, tai-tham</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+22EF MIDLINE HORIZONTAL ELLIPSIS: try adding math</li>
<li>U+24B6 CIRCLED LATIN CAPITAL LETTER A: try adding symbols</li>
<li>U+24B9 CIRCLED LATIN CAPITAL LETTER D: try adding symbols</li>
<li>U+24D0 CIRCLED LATIN SMALL LETTER A: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B4 BLACK UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B5 WHITE UP-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B8 BLACK RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25B9 WHITE RIGHT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25BE BLACK DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25BF WHITE DOWN-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C2 BLACK LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C3 WHITE LEFT-POINTING SMALL TRIANGLE: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+27E8 MATHEMATICAL LEFT ANGLE BRACKET: try adding math</li>
<li>U+27E9 MATHEMATICAL RIGHT ANGLE BRACKET: try adding math</li>
<li>U+E0FC : not included in any glyphset definition</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic-ext</code>, <code>devanagari</code>, <code>greek</code>, <code>greek-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>tamil</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-dotted">soft_dotted</a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: i̍ i̐ i᷆ i᷇ ɨ̀ ɨ́ ɨ̂ ɨ̃ ɨ̄ ɨ̈ ɨ̋ ɨ̌ ɨ̏ ɨ̧̀ ɨ̧́ ɨ̧̂ ɨ̧̌ ɨ̱̀ ɨ̱́ ɨ̱̈ ḭ̀ ḭ́ ḭ̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̅ i̇ i̒ i᷄ i᷅ i̛̅ i̛̇ i̛̊ i̛̋ i̛̍ i̛̐ i̛̒ i̛᷄ i̛᷅ i̛᷆ i̛᷇ i̤̅ i̤̇ i̤̊ i̤̋</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-direction">outline_direction</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* glottalstopreversed (U+0295) has a counter-clockwise outer contour

* glottalstopreversed (U+0295) has a counter-clockwise outer contour

* glottalstopreversed (U+0295) has a counter-clockwise outer contour

* glottalstopreversed (U+0295) has a counter-clockwise outer contour

* lambda (U+03BB) has a counter-clockwise outer contour

* lambda (U+03BB) has a counter-clockwise outer contour

* uni0BB8 (U+0BB8) has a counter-clockwise outer contour
</code></pre>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-meta-script-lang-tags">googlefonts/meta/script_lang_tags</a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



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
    <summary>ℹ️ <b>INFO</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>







* ℹ️ **INFO** <p>The family name &quot;Samaano&quot; seems to be already in use.
Please visit <a href="http://namecheck.fontdata.com/?q=Samaano">http://namecheck.fontdata.com/?q=Samaano</a> for more info.</p>
 [code: name-collision]



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
<th align="right">fonts/variable/Samaano[slnt,wdth,wght].ttf</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Dehinted Size</td>
<td align="right">372.6kb</td>
</tr>
<tr>
<td align="left">Hinted Size</td>
<td align="right">372.6kb</td>
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
    <summary>ℹ️ <b>INFO</b> Font has old ttfautohint applied? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-old-ttfautohint">googlefonts/old_ttfautohint</a></summary>
    <div>







* ℹ️ **INFO** <p>Could not detect which version of ttfautohint was used in this font. It is typically specified as a comment in the font version entries of the 'name' table. Such font version strings are currently: ['Version 2.400']</p>
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
    <summary>✅ <b>PASS</b> The font should not need a DSIG table anymore. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-dsig">opentype/dsig</a></summary>
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
    <summary>✅ <b>PASS</b> Check GDEF mark glyph class doesn't have characters that are not marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-non-mark-chars">opentype/gdef_non_mark_chars</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check glyphs in mark glyph class are non-spacing. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-spacing-marks">opentype/gdef_spacing_marks</a></summary>
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







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



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
    <summary>✅ <b>PASS</b> Are there unwanted Apple tables? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-unwanted-aat-tables">opentype/unwanted_aat_tables</a></summary>
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
    <summary>✅ <b>PASS</b> Do we have the latest version of FontBakery installed? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontbakery-version">fontbakery_version</a></summary>
    <div>







* ✅ **PASS** <p>FontBakery is up-to-date.</p>
 



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
    <summary>✅ <b>PASS</b> Ensure variable fonts include an avar table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#mandatory-avar-table">mandatory_avar_table</a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



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
    <summary>✅ <b>PASS</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-alignment-miss">outline_alignment_miss</a></summary>
    <div>







* ✅ **PASS** <p>So many Y-coordinates of points were close to boundaries that this was probably by design.</p>
 



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







* ✅ **PASS** <p>Font filename is correct, &quot;Samaano[slnt,wdth,wght].ttf&quot;.</p>
 



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
    <summary>⏩ <b>SKIP</b> Check that glyph for U+0674 ARABIC LETTER HIGH HAMZA is not a mark. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#arabic-high-hamza">arabic_high_hamza</a></summary>
    <div>







* ⏩ **SKIP** <p>This check will only run on fonts that have U+0674 glyph</p>
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
    <summary>ℹ️ <b>INFO</b> Check axis ordering on the STAT table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-STAT-axis-order">googlefonts/STAT/axis_order</a></summary>
    <div>







* ℹ️ **INFO** <p>None of the fonts lack a STAT table.</p>
<pre><code>And these are the most common STAT axis orderings:
('wdth-wght-slnt', 1)
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
    <summary>⏩ <b>SKIP</b> Ensure VFs have 'ital' STAT axis. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-STAT-ital-axis">opentype/STAT/ital_axis</a></summary>
    <div>







* ⏩ **SKIP** <p>Font {font.file} doesn't have an ital axis</p>
 



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
| 1 | 0 | 5 | 12 | 87 | 8 | 123 | 0 | 
| 0% | 0% | 2% | 5% | 37% | 3% | 52% | 0% | 



**Note:** The following loglevels were omitted in this report:


* DEBUG
