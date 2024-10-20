## FontBakery report

fontbakery version: 0.12.10





## Check results



<details><summary>[1] Family checks</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Verify that family names in the name table are consistent across all fonts in the family. Checks Typographic Family name (nameID 16) if present, otherwise uses Font Family name (nameID 1) <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>7 different Font Family names were found:</p>
<ul>
<li>
<p>'Samaano' was found in:</p>
<ul>
<li>Samaano-Bold.ttf (nameID 1)</li>
<li>Samaano-Thin.ttf (nameID 16)</li>
</ul>
</li>
<li>
<p>'Samaano Wide-Bold' was found in:</p>
<ul>
<li>Samaano-Wide-Bold.ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Samaano Wide-Thin' was found in:</p>
<ul>
<li>Samaano-Wide-Thin.ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Samaano Bold-Slanted' was found in:</p>
<ul>
<li>Samaano-Bold-Slanted.ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Samaano Thin-Slanted' was found in:</p>
<ul>
<li>Samaano-Thin-Slanted.ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Samaano Wide-Bold-Slanted' was found in:</p>
<ul>
<li>Samaano-Wide-Bold-Slanted.ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Samaano Wide-Thin-Slanted' was found in:</p>
<ul>
<li>Samaano-Wide-Thin-Slanted.ttf (nameID 1)</li>
</ul>
</li>
</ul>
 [code: inconsistent-family-name]



</div>
</details>
</div>
</details>

<details><summary>[16] Samaano-Bold.ttf</summary>
<div>
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
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: parenleft	Contours detected: 2	Expected: 1

- Glyph name: Z	Contours detected: 2	Expected: 1

- Glyph name: braceleft	Contours detected: 2	Expected: 1

- Glyph name: mu	Contours detected: 2	Expected: 1

- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: Zacute	Contours detected: 3	Expected: 2

- Glyph name: Zdotaccent	Contours detected: 3	Expected: 2

- Glyph name: Zcaron	Contours detected: 3	Expected: 2

- Glyph name: uni01C4	Contours detected: 5	Expected: 4

- Glyph name: uni0916	Contours detected: 2	Expected: 1 or 3

- Glyph name: uni091B	Contours detected: 1	Expected: 2

- Glyph name: uni092D	Contours detected: 2	Expected: 1

- Glyph name: uni092E	Contours detected: 3	Expected: 2

- Glyph name: uni093D	Contours detected: 3	Expected: 1

- Glyph name: uni0945	Contours detected: 2	Expected: 1

- Glyph name: uni0955	Contours detected: 3	Expected: 2

- Glyph name: uni0956	Contours detected: 2	Expected: 1

- Glyph name: uni0957	Contours detected: 3	Expected: 2

- Glyph name: uni0959	Contours detected: 3	Expected: 2 or 4

- Glyph name: uni0962	Contours detected: 2	Expected: 1

- Glyph name: uni0963	Contours detected: 2	Expected: 1

- Glyph name: uni0967	Contours detected: 2	Expected: 1

- Glyph name: uni0970	Contours detected: 1	Expected: 2

- Glyph name: uni097F	Contours detected: 2	Expected: 3

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: Z	Contours detected: 2	Expected: 1

- Glyph name: Zacute	Contours detected: 3	Expected: 2

- Glyph name: Zcaron	Contours detected: 3	Expected: 2

- Glyph name: Zdotaccent	Contours detected: 3	Expected: 2

- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: braceleft	Contours detected: 2	Expected: 1

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: parenleft	Contours detected: 2	Expected: 1

- Glyph name: uni01C4	Contours detected: 5	Expected: 4

- Glyph name: uni0916	Contours detected: 2	Expected: 1 or 3

- Glyph name: uni091B	Contours detected: 1	Expected: 2

- Glyph name: uni092D	Contours detected: 2	Expected: 1

- Glyph name: uni092E	Contours detected: 3	Expected: 2

- Glyph name: uni093D	Contours detected: 3	Expected: 1

- Glyph name: uni0945	Contours detected: 2	Expected: 1

- Glyph name: uni0955	Contours detected: 3	Expected: 2

- Glyph name: uni0956	Contours detected: 2	Expected: 1

- Glyph name: uni0957	Contours detected: 3	Expected: 2

- Glyph name: uni0959	Contours detected: 3	Expected: 2 or 4

- Glyph name: uni0962	Contours detected: 2	Expected: 1

- Glyph name: uni0963	Contours detected: 2	Expected: 1

- Glyph name: uni0967	Contours detected: 2	Expected: 1

- Glyph name: uni0970	Contours detected: 1	Expected: 2

- Glyph name: uni097F	Contours detected: 2	Expected: 3

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

- Glyph name: uogonek	Contours detected: 2	Expected: 1
</code></pre>
 [code: contour-count]



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







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, tifinagh, coptic, cherokee</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: coptic, glagolitic, gothic, elbasan, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: duployan, malayalam, hebrew, old-permic, todhri, tai-le, coptic, tifinagh, math, syriac, canadian-aboriginal</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: gothic, thai, tifinagh, caucasian-albanian, syriac, sunuwar, cherokee</li>
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
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Nzakara (Latn, 50,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Makaa (Latn, 221,000 speakers), Ejagham (Latn, 120,000 speakers), Igbo (Latn, 27,823,640 speakers), Zapotec (Latn, 490,000 speakers), Aghem (Latn, 38,843 speakers), Yala (Latn, 200,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Sar (Latn, 500,000 speakers), Koonzime (Latn, 40,000 speakers), Mundani (Latn, 34,000 speakers), Dutch (Latn, 31,709,104 speakers), Ngbaka (Latn, 1,020,000 speakers), Ekpeye (Latn, 226,000 speakers), Avokaya (Latn, 100,000 speakers), Mango (Latn, 77,000 speakers), Southern Kisi (Latn, 360,000 speakers), Gulay (Latn, 250,478 speakers), Cicipu (Latn, 44,000 speakers), Basaa (Latn, 332,940 speakers), Dii (Latn, 71,000 speakers), South Central Banda (Latn, 244,000 speakers), Lugbara (Latn, 2,200,000 speakers), Navajo (Latn, 166,319 speakers), Nateni (Latn, 100,000 speakers), Kom (Latn, 360,685 speakers), Belarusian (Cyrl, 10,064,517 speakers), Ma’di (Latn, 584,000 speakers), Ebira (Latn, 2,200,000 speakers), Mfumte (Latn, 79,000 speakers), Bafut (Latn, 158,146 speakers), Vute (Latn, 21,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Fur (Latn, 1,230,163 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Dan (Latn, 1,099,244 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have on-curve points which have potentially incorrect y coordinates:</p>
<pre><code>* N (U+004E): X=722.0,Y=2.0 (should be at baseline 0?)

* Ntilde (U+00D1): X=722.0,Y=2.0 (should be at baseline 0?)

* Nacute (U+0143): X=722.0,Y=2.0 (should be at baseline 0?)

* uni0145 (U+0145): X=722.0,Y=2.0 (should be at baseline 0?)

* Ncaron (U+0147): X=722.0,Y=2.0 (should be at baseline 0?)

* Eng (U+014A): X=112.0,Y=1550.0 (should be at cap-height 1548?)

* Eng (U+014A): X=911.0,Y=1550.0 (should be at cap-height 1548?)

* uni01C4 (U+01C4): X=213.0,Y=1550.0 (should be at cap-height 1548?)

* uni01C4 (U+01C4): X=213.0,Y=1549.0 (should be at cap-height 1548?)

* uni01C4 (U+01C4): X=151.0,Y=1549.0 (should be at cap-height 1548?)

* uni01C5 (U+01C5): X=214.0,Y=1550.0 (should be at cap-height 1548?)

* uni01C5 (U+01C5): X=214.0,Y=1549.0 (should be at cap-height 1548?)

* uni01C5 (U+01C5): X=152.0,Y=1549.0 (should be at cap-height 1548?)

* uni1E44 (U+1E44): X=722.0,Y=2.0 (should be at baseline 0?)

* uni1E46 (U+1E46): X=722.0,Y=2.0 (should be at baseline 0?)

* uni1E48 (U+1E48): X=722.0,Y=2.0 (should be at baseline 0?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* B (U+0042): L&lt;&lt;947.0,1215.0&gt;--&lt;947.0,1215.0&gt;&gt; -&gt; L&lt;&lt;947.0,1215.0&gt;--&lt;948.0,1215.0&gt;&gt;

* uni092F (U+092F): L&lt;&lt;688.0,223.0&gt;--&lt;140.0,467.0&gt;&gt; -&gt; L&lt;&lt;140.0,467.0&gt;--&lt;127.0,472.0&gt;&gt;

* uni092F_uni0930_uni094D.vatu: L&lt;&lt;574.0,273.0&gt;--&lt;140.0,467.0&gt;&gt; -&gt; L&lt;&lt;140.0,467.0&gt;--&lt;127.0,472.0&gt;&gt;

* uni092F_uni094D.half: L&lt;&lt;991.0,199.0&gt;--&lt;390.0,467.0&gt;&gt; -&gt; L&lt;&lt;390.0,467.0&gt;--&lt;377.0,472.0&gt;&gt;

* uni092F_uni094D.haln: L&lt;&lt;688.0,223.0&gt;--&lt;140.0,467.0&gt;&gt; -&gt; L&lt;&lt;140.0,467.0&gt;--&lt;127.0,472.0&gt;&gt;

* uni0943 (U+0943): L&lt;&lt;-211.0,-611.0&gt;--&lt;-254.0,-495.0&gt;&gt; -&gt; L&lt;&lt;-254.0,-495.0&gt;--&lt;-269.0,-455.0&gt;&gt;

* uni0943 (U+0943): L&lt;&lt;-269.0,-455.0&gt;--&lt;-338.0,-269.0&gt;&gt; -&gt; L&lt;&lt;-338.0,-269.0&gt;--&lt;-389.0,-133.0&gt;&gt;

* uni095F (U+095F): L&lt;&lt;688.0,223.0&gt;--&lt;140.0,467.0&gt;&gt; -&gt; L&lt;&lt;140.0,467.0&gt;--&lt;127.0,472.0&gt;&gt;

* uni095F_uni0930_uni094D.vatu: L&lt;&lt;574.0,273.0&gt;--&lt;140.0,467.0&gt;&gt; -&gt; L&lt;&lt;140.0,467.0&gt;--&lt;127.0,472.0&gt;&gt;

* uni095F_uni094D.half: L&lt;&lt;688.0,223.0&gt;--&lt;140.0,467.0&gt;&gt; -&gt; L&lt;&lt;140.0,467.0&gt;--&lt;127.0,472.0&gt;&gt;

* uni095F_uni094D.haln: L&lt;&lt;688.0,223.0&gt;--&lt;140.0,467.0&gt;&gt; -&gt; L&lt;&lt;140.0,467.0&gt;--&lt;127.0,472.0&gt;&gt;

* uni097A (U+097A): L&lt;&lt;688.0,223.0&gt;--&lt;140.0,467.0&gt;&gt; -&gt; L&lt;&lt;140.0,467.0&gt;--&lt;127.0,472.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* questiondown (U+00BF): L&lt;&lt;655.0,1273.0&gt;--&lt;405.0,1272.0&gt;&gt;

* uni0930_uni0942.blws: L&lt;&lt;-2.0,1347.0&gt;--&lt;-1.0,1548.0&gt;&gt;

* uni0930_uni0942.blws: L&lt;&lt;1023.0,1348.0&gt;--&lt;451.0,1347.0&gt;&gt;

* uni0930_uni0942.blws: L&lt;&lt;1024.0,1548.0&gt;--&lt;1023.0,1348.0&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



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

<details><summary>[17] Samaano-Thin.ttf</summary>
<div>
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







* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 434 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



* ⚠️ **WARN** <p>Font is monospaced but 3 glyphs (0.42%) have a different width. You should check the widths of: ['uni0308', 'uni030A', 'uni030B']</p>
 [code: mono-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check glyphs in mark glyph class are non-spacing. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following spacing glyphs may be in the GDEF mark glyph class by mistake:
acutecomb (U+0301), dotbelowcomb (U+0323), glyph094D (unencoded), gravecomb (U+0300), uni0304 (U+0304), uni0308 (U+0308), uni030A (U+030A), uni030B (U+030B), uni030C (U+030C), uni0326 (U+0326), uni0327 (U+0327), uni0328 (U+0328), uni0331 (U+0331), uni0930_uni094D.blwf (unencoded), uni0930_uni094D.rphf (unencoded), uni093A (U+093A), uni093C (U+093C), uni0945 (U+0945), uni0946 (U+0946), uni0947 (U+0947), uni0948 (U+0948), uni0951 (U+0951), uni0952 (U+0952), uni0953 (U+0953), uni0954 (U+0954), uni0955 (U+0955), uni0956 (U+0956), uni0957 (U+0957), uni0962 (U+0962) and uni0963 (U+0963)</p>
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
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gpos.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning information.</p>
 [code: lacks-kern-info]



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
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: D	Contours detected: 1	Expected: 2

- Glyph name: g	Contours detected: 1	Expected: 2 or 3

- Glyph name: o	Contours detected: 1	Expected: 2

- Glyph name: braceleft	Contours detected: 2	Expected: 1

- Glyph name: ograve	Contours detected: 2	Expected: 3

- Glyph name: oacute	Contours detected: 2	Expected: 3

- Glyph name: ocircumflex	Contours detected: 2	Expected: 3

- Glyph name: otilde	Contours detected: 2	Expected: 3

- Glyph name: odieresis	Contours detected: 3	Expected: 4

- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: Dcaron	Contours detected: 2	Expected: 3

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: gcircumflex	Contours detected: 2	Expected: 3 or 4

- Glyph name: gbreve	Contours detected: 2	Expected: 3 or 4

- Glyph name: gdotaccent	Contours detected: 2	Expected: 3 or 4

- Glyph name: uni0123	Contours detected: 2	Expected: 3 or 4

- Glyph name: omacron	Contours detected: 2	Expected: 3

- Glyph name: obreve	Contours detected: 2	Expected: 3

- Glyph name: ohungarumlaut	Contours detected: 3	Expected: 4

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: uni01C4	Contours detected: 3	Expected: 4

- Glyph name: uni01C5	Contours detected: 3	Expected: 4

- Glyph name: uni0910	Contours detected: 2	Expected: 1

- Glyph name: uni091B	Contours detected: 1	Expected: 2

- Glyph name: uni092D	Contours detected: 2	Expected: 1

- Glyph name: uni092E	Contours detected: 3	Expected: 2

- Glyph name: uni093D	Contours detected: 2	Expected: 1

- Glyph name: uni0945	Contours detected: 2	Expected: 1

- Glyph name: uni0955	Contours detected: 3	Expected: 2

- Glyph name: uni0956	Contours detected: 2	Expected: 1

- Glyph name: uni0957	Contours detected: 3	Expected: 2

- Glyph name: uni0962	Contours detected: 2	Expected: 1

- Glyph name: uni0963	Contours detected: 2	Expected: 1

- Glyph name: uni0967	Contours detected: 2	Expected: 1

- Glyph name: uni0970	Contours detected: 1	Expected: 2

- Glyph name: uni097F	Contours detected: 2	Expected: 3

- Glyph name: uni1E0C	Contours detected: 2	Expected: 3

- Glyph name: uni1E4D	Contours detected: 3	Expected: 4

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

- Glyph name: D	Contours detected: 1	Expected: 2

- Glyph name: Dcaron	Contours detected: 2	Expected: 3

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: braceleft	Contours detected: 2	Expected: 1

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: g	Contours detected: 1	Expected: 2 or 3

- Glyph name: gbreve	Contours detected: 2	Expected: 3 or 4

- Glyph name: gcircumflex	Contours detected: 2	Expected: 3 or 4

- Glyph name: gdotaccent	Contours detected: 2	Expected: 3 or 4

- Glyph name: o	Contours detected: 1	Expected: 2

- Glyph name: oacute	Contours detected: 2	Expected: 3

- Glyph name: ocircumflex	Contours detected: 2	Expected: 3

- Glyph name: odieresis	Contours detected: 3	Expected: 4

- Glyph name: ograve	Contours detected: 2	Expected: 3

- Glyph name: ohungarumlaut	Contours detected: 3	Expected: 4

- Glyph name: omacron	Contours detected: 2	Expected: 3

- Glyph name: otilde	Contours detected: 2	Expected: 3

- Glyph name: uni0123	Contours detected: 2	Expected: 3 or 4

- Glyph name: uni01C4	Contours detected: 3	Expected: 4

- Glyph name: uni01C5	Contours detected: 3	Expected: 4

- Glyph name: uni0910	Contours detected: 2	Expected: 1

- Glyph name: uni091B	Contours detected: 1	Expected: 2

- Glyph name: uni092D	Contours detected: 2	Expected: 1

- Glyph name: uni092E	Contours detected: 3	Expected: 2

- Glyph name: uni093D	Contours detected: 2	Expected: 1

- Glyph name: uni0945	Contours detected: 2	Expected: 1

- Glyph name: uni0955	Contours detected: 3	Expected: 2

- Glyph name: uni0956	Contours detected: 2	Expected: 1

- Glyph name: uni0957	Contours detected: 3	Expected: 2

- Glyph name: uni0962	Contours detected: 2	Expected: 1

- Glyph name: uni0963	Contours detected: 2	Expected: 1

- Glyph name: uni0967	Contours detected: 2	Expected: 1

- Glyph name: uni0970	Contours detected: 1	Expected: 2

- Glyph name: uni097F	Contours detected: 2	Expected: 3

- Glyph name: uni1E0C	Contours detected: 2	Expected: 3

- Glyph name: uni1E4D	Contours detected: 3	Expected: 4

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

- Glyph name: uogonek	Contours detected: 2	Expected: 1
</code></pre>
 [code: contour-count]



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







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, tifinagh, coptic, cherokee</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: coptic, glagolitic, gothic, elbasan, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: duployan, malayalam, hebrew, old-permic, todhri, tai-le, coptic, tifinagh, math, syriac, canadian-aboriginal</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: gothic, thai, tifinagh, caucasian-albanian, syriac, sunuwar, cherokee</li>
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
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Nzakara (Latn, 50,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Makaa (Latn, 221,000 speakers), Ejagham (Latn, 120,000 speakers), Igbo (Latn, 27,823,640 speakers), Zapotec (Latn, 490,000 speakers), Aghem (Latn, 38,843 speakers), Yala (Latn, 200,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Sar (Latn, 500,000 speakers), Koonzime (Latn, 40,000 speakers), Mundani (Latn, 34,000 speakers), Dutch (Latn, 31,709,104 speakers), Ngbaka (Latn, 1,020,000 speakers), Ekpeye (Latn, 226,000 speakers), Avokaya (Latn, 100,000 speakers), Mango (Latn, 77,000 speakers), Southern Kisi (Latn, 360,000 speakers), Gulay (Latn, 250,478 speakers), Cicipu (Latn, 44,000 speakers), Basaa (Latn, 332,940 speakers), Dii (Latn, 71,000 speakers), South Central Banda (Latn, 244,000 speakers), Lugbara (Latn, 2,200,000 speakers), Navajo (Latn, 166,319 speakers), Nateni (Latn, 100,000 speakers), Kom (Latn, 360,685 speakers), Belarusian (Cyrl, 10,064,517 speakers), Ma’di (Latn, 584,000 speakers), Ebira (Latn, 2,200,000 speakers), Mfumte (Latn, 79,000 speakers), Bafut (Latn, 158,146 speakers), Vute (Latn, 21,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Fur (Latn, 1,230,163 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Dan (Latn, 1,099,244 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* a (U+0061): L&lt;&lt;168.0,1024.0&gt;--&lt;817.0,1023.0&gt;&gt; -&gt; L&lt;&lt;817.0,1023.0&gt;--&lt;856.0,1023.0&gt;&gt;

* aacute (U+00E1): L&lt;&lt;168.0,1024.0&gt;--&lt;817.0,1023.0&gt;&gt; -&gt; L&lt;&lt;817.0,1023.0&gt;--&lt;856.0,1023.0&gt;&gt;

* abreve (U+0103): L&lt;&lt;168.0,1024.0&gt;--&lt;817.0,1023.0&gt;&gt; -&gt; L&lt;&lt;817.0,1023.0&gt;--&lt;856.0,1023.0&gt;&gt;

* acircumflex (U+00E2): L&lt;&lt;168.0,1024.0&gt;--&lt;817.0,1023.0&gt;&gt; -&gt; L&lt;&lt;817.0,1023.0&gt;--&lt;856.0,1023.0&gt;&gt;

* adieresis (U+00E4): L&lt;&lt;168.0,1024.0&gt;--&lt;817.0,1023.0&gt;&gt; -&gt; L&lt;&lt;817.0,1023.0&gt;--&lt;856.0,1023.0&gt;&gt;

* agrave (U+00E0): L&lt;&lt;168.0,1024.0&gt;--&lt;817.0,1023.0&gt;&gt; -&gt; L&lt;&lt;817.0,1023.0&gt;--&lt;856.0,1023.0&gt;&gt;

* amacron (U+0101): L&lt;&lt;168.0,1024.0&gt;--&lt;817.0,1023.0&gt;&gt; -&gt; L&lt;&lt;817.0,1023.0&gt;--&lt;856.0,1023.0&gt;&gt;

* aogonek (U+0105): L&lt;&lt;168.0,1024.0&gt;--&lt;817.0,1023.0&gt;&gt; -&gt; L&lt;&lt;817.0,1023.0&gt;--&lt;856.0,1023.0&gt;&gt;

* aring (U+00E5): L&lt;&lt;168.0,1024.0&gt;--&lt;817.0,1023.0&gt;&gt; -&gt; L&lt;&lt;817.0,1023.0&gt;--&lt;856.0,1023.0&gt;&gt;

* atilde (U+00E3): L&lt;&lt;168.0,1024.0&gt;--&lt;817.0,1023.0&gt;&gt; -&gt; L&lt;&lt;817.0,1023.0&gt;--&lt;856.0,1023.0&gt;&gt;

* uni0944 (U+0944): L&lt;&lt;-210.0,-942.0&gt;--&lt;-220.0,-945.0&gt;&gt; -&gt; L&lt;&lt;-220.0,-945.0&gt;--&lt;-228.0,-947.0&gt;&gt;

* uni094F (U+094F): L&lt;&lt;134.0,2066.0&gt;--&lt;143.0,2105.0&gt;&gt; -&gt; L&lt;&lt;143.0,2105.0&gt;--&lt;187.0,2323.0&gt;&gt;

* uni094F (U+094F): L&lt;&lt;722.0,1934.0&gt;--&lt;162.0,2060.0&gt;&gt; -&gt; L&lt;&lt;162.0,2060.0&gt;--&lt;135.0,2064.0&gt;&gt;

* uni0975 (U+0975): L&lt;&lt;439.0,2080.0&gt;--&lt;433.0,2083.0&gt;&gt; -&gt; L&lt;&lt;433.0,2083.0&gt;--&lt;428.0,2086.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* uni0913 (U+0913): L&lt;&lt;846.0,1550.0&gt;--&lt;842.0,1549.0&gt;&gt;/L&lt;&lt;842.0,1549.0&gt;--&lt;1024.0,1549.0&gt;&gt; = 14.036243467926484

* uni093D (U+093D): L&lt;&lt;455.0,104.0&gt;--&lt;457.0,127.0&gt;&gt;/L&lt;&lt;457.0,127.0&gt;--&lt;454.0,107.0&gt;&gt; = 3.561024881837821

* uni0944 (U+0944): L&lt;&lt;-220.0,-945.0&gt;--&lt;-228.0,-947.0&gt;&gt;/L&lt;&lt;-228.0,-947.0&gt;--&lt;-228.0,-947.0&gt;&gt; = 14.036243467926484

* uni0968 (U+0968): L&lt;&lt;221.0,486.0&gt;--&lt;239.0,488.0&gt;&gt;/L&lt;&lt;239.0,488.0&gt;--&lt;224.0,488.0&gt;&gt; = 6.340191745909908
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* a (U+0061): L&lt;&lt;168.0,1024.0&gt;--&lt;817.0,1023.0&gt;&gt;

* aacute (U+00E1): L&lt;&lt;168.0,1024.0&gt;--&lt;817.0,1023.0&gt;&gt;

* abreve (U+0103): L&lt;&lt;168.0,1024.0&gt;--&lt;817.0,1023.0&gt;&gt;

* acircumflex (U+00E2): L&lt;&lt;168.0,1024.0&gt;--&lt;817.0,1023.0&gt;&gt;

* adieresis (U+00E4): L&lt;&lt;168.0,1024.0&gt;--&lt;817.0,1023.0&gt;&gt;

* agrave (U+00E0): L&lt;&lt;168.0,1024.0&gt;--&lt;817.0,1023.0&gt;&gt;

* amacron (U+0101): L&lt;&lt;168.0,1024.0&gt;--&lt;817.0,1023.0&gt;&gt;

* aogonek (U+0105): L&lt;&lt;168.0,1024.0&gt;--&lt;817.0,1023.0&gt;&gt;

* aring (U+00E5): L&lt;&lt;168.0,1024.0&gt;--&lt;817.0,1023.0&gt;&gt;

* atilde (U+00E3): L&lt;&lt;168.0,1024.0&gt;--&lt;817.0,1023.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;538.0,1035.0&gt;--&lt;542.0,17.0&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



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

<details><summary>[21] Samaano-Wide-Bold.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead.</p>
 [code: mono-bad-post-isFixedPitch]



* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 434 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



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
<td align="left">U+0189: LATIN CAPITAL LETTER AFRICAN D</td>
<td align="left">U+0256: LATIN SMALL LETTER D WITH TAIL</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



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
    <summary>🔥 <b>FAIL</b> Check family name for GF Guide compliance. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>&quot;Samaano Wide-Bold&quot; contains the following characters which are not allowed: &quot;-&quot;.</p>
 [code: forbidden-characters]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking file is named canonically. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Expected &quot;SamaanoWide-Bold-Regular.ttf. Got Samaano-Wide-Bold.ttf.</p>
 [code: bad-filename]



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
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gpos.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning information.</p>
 [code: lacks-kern-info]



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
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: parenleft	Contours detected: 2	Expected: 1

- Glyph name: Z	Contours detected: 2	Expected: 1

- Glyph name: braceleft	Contours detected: 2	Expected: 1

- Glyph name: mu	Contours detected: 2	Expected: 1

- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: Zacute	Contours detected: 3	Expected: 2

- Glyph name: Zdotaccent	Contours detected: 3	Expected: 2

- Glyph name: Zcaron	Contours detected: 3	Expected: 2

- Glyph name: uni01C4	Contours detected: 5	Expected: 4

- Glyph name: uni0916	Contours detected: 2	Expected: 1 or 3

- Glyph name: uni091B	Contours detected: 1	Expected: 2

- Glyph name: uni092D	Contours detected: 2	Expected: 1

- Glyph name: uni092E	Contours detected: 3	Expected: 2

- Glyph name: uni093D	Contours detected: 3	Expected: 1

- Glyph name: uni0945	Contours detected: 2	Expected: 1

- Glyph name: uni0955	Contours detected: 3	Expected: 2

- Glyph name: uni0956	Contours detected: 2	Expected: 1

- Glyph name: uni0957	Contours detected: 3	Expected: 2

- Glyph name: uni0959	Contours detected: 3	Expected: 2 or 4

- Glyph name: uni0962	Contours detected: 2	Expected: 1

- Glyph name: uni0963	Contours detected: 2	Expected: 1

- Glyph name: uni0967	Contours detected: 2	Expected: 1

- Glyph name: uni0970	Contours detected: 1	Expected: 2

- Glyph name: uni097F	Contours detected: 2	Expected: 3

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: Z	Contours detected: 2	Expected: 1

- Glyph name: Zacute	Contours detected: 3	Expected: 2

- Glyph name: Zcaron	Contours detected: 3	Expected: 2

- Glyph name: Zdotaccent	Contours detected: 3	Expected: 2

- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: braceleft	Contours detected: 2	Expected: 1

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: parenleft	Contours detected: 2	Expected: 1

- Glyph name: uni01C4	Contours detected: 5	Expected: 4

- Glyph name: uni0916	Contours detected: 2	Expected: 1 or 3

- Glyph name: uni091B	Contours detected: 1	Expected: 2

- Glyph name: uni092D	Contours detected: 2	Expected: 1

- Glyph name: uni092E	Contours detected: 3	Expected: 2

- Glyph name: uni093D	Contours detected: 3	Expected: 1

- Glyph name: uni0945	Contours detected: 2	Expected: 1

- Glyph name: uni0955	Contours detected: 3	Expected: 2

- Glyph name: uni0956	Contours detected: 2	Expected: 1

- Glyph name: uni0957	Contours detected: 3	Expected: 2

- Glyph name: uni0959	Contours detected: 3	Expected: 2 or 4

- Glyph name: uni0962	Contours detected: 2	Expected: 1

- Glyph name: uni0963	Contours detected: 2	Expected: 1

- Glyph name: uni0967	Contours detected: 2	Expected: 1

- Glyph name: uni0970	Contours detected: 1	Expected: 2

- Glyph name: uni097F	Contours detected: 2	Expected: 3

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

- Glyph name: uogonek	Contours detected: 2	Expected: 1
</code></pre>
 [code: contour-count]



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







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, tifinagh, coptic, cherokee</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: coptic, glagolitic, gothic, elbasan, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: duployan, malayalam, hebrew, old-permic, todhri, tai-le, coptic, tifinagh, math, syriac, canadian-aboriginal</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: gothic, thai, tifinagh, caucasian-albanian, syriac, sunuwar, cherokee</li>
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
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Nzakara (Latn, 50,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Makaa (Latn, 221,000 speakers), Ejagham (Latn, 120,000 speakers), Igbo (Latn, 27,823,640 speakers), Zapotec (Latn, 490,000 speakers), Aghem (Latn, 38,843 speakers), Yala (Latn, 200,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Sar (Latn, 500,000 speakers), Koonzime (Latn, 40,000 speakers), Mundani (Latn, 34,000 speakers), Dutch (Latn, 31,709,104 speakers), Ngbaka (Latn, 1,020,000 speakers), Ekpeye (Latn, 226,000 speakers), Avokaya (Latn, 100,000 speakers), Mango (Latn, 77,000 speakers), Southern Kisi (Latn, 360,000 speakers), Gulay (Latn, 250,478 speakers), Cicipu (Latn, 44,000 speakers), Basaa (Latn, 332,940 speakers), Dii (Latn, 71,000 speakers), South Central Banda (Latn, 244,000 speakers), Lugbara (Latn, 2,200,000 speakers), Navajo (Latn, 166,319 speakers), Nateni (Latn, 100,000 speakers), Kom (Latn, 360,685 speakers), Belarusian (Cyrl, 10,064,517 speakers), Ma’di (Latn, 584,000 speakers), Ebira (Latn, 2,200,000 speakers), Mfumte (Latn, 79,000 speakers), Bafut (Latn, 158,146 speakers), Vute (Latn, 21,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Fur (Latn, 1,230,163 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Dan (Latn, 1,099,244 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have on-curve points which have potentially incorrect y coordinates:</p>
<pre><code>* N (U+004E): X=1912.0,Y=2.0 (should be at baseline 0?)

* N (U+004E): X=1710.0,Y=2.0 (should be at baseline 0?)

* v (U+0076): X=1128.0,Y=1.0 (should be at baseline 0?)

* v (U+0076): X=921.0,Y=1.0 (should be at baseline 0?)

* Ntilde (U+00D1): X=1912.0,Y=2.0 (should be at baseline 0?)

* Ntilde (U+00D1): X=1710.0,Y=2.0 (should be at baseline 0?)

* ccedilla (U+00E7): X=1844.0,Y=-617.0 (should be at descender -615?)

* ccedilla (U+00E7): X=1398.0,Y=-617.0 (should be at descender -615?)

* Nacute (U+0143): X=1912.0,Y=2.0 (should be at baseline 0?)

* Nacute (U+0143): X=1710.0,Y=2.0 (should be at baseline 0?)

* uni0145 (U+0145): X=1912.0,Y=2.0 (should be at baseline 0?)

* uni0145 (U+0145): X=1710.0,Y=2.0 (should be at baseline 0?)

* uni0145 (U+0145): X=913.0,Y=-2.0 (should be at baseline 0?)

* uni0145 (U+0145): X=1161.0,Y=-2.0 (should be at baseline 0?)

* Ncaron (U+0147): X=1912.0,Y=2.0 (should be at baseline 0?)

* Ncaron (U+0147): X=1710.0,Y=2.0 (should be at baseline 0?)

* Eng (U+014A): X=112.0,Y=1547.0 (should be at cap-height 1548?)

* Eng (U+014A): X=313.0,Y=1547.0 (should be at cap-height 1548?)

* uni0156 (U+0156): X=878.0,Y=1.0 (should be at baseline 0?)

* uni0156 (U+0156): X=1126.0,Y=1.0 (should be at baseline 0?)

* Uogonek (U+0172): X=1340.0,Y=-2.0 (should be at baseline 0?)

* Uogonek (U+0172): X=1882.0,Y=-2.0 (should be at baseline 0?)

* uni1E44 (U+1E44): X=1912.0,Y=2.0 (should be at baseline 0?)

* uni1E44 (U+1E44): X=1710.0,Y=2.0 (should be at baseline 0?)

* uni1E46 (U+1E46): X=1912.0,Y=2.0 (should be at baseline 0?)

* uni1E46 (U+1E46): X=1710.0,Y=2.0 (should be at baseline 0?)

* uni1E48 (U+1E48): X=1912.0,Y=2.0 (should be at baseline 0?)

* uni1E48 (U+1E48): X=1710.0,Y=2.0 (should be at baseline 0?)

* uni094A_uni0930_uni094D.abvs: X=1378.0,Y=1549.0 (should be at cap-height 1548?)

* uni094A_uni0930_uni094D.abvs: X=1576.0,Y=1549.0 (should be at cap-height 1548?)

* uni095C_uni0930_uni094D.vatu: X=282.0,Y=1.0 (should be at baseline 0?)

* uni095C_uni0930_uni094D.vatu: X=548.0,Y=1.0 (should be at baseline 0?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* uni0921 (U+0921): L&lt;&lt;1581.0,746.0&gt;--&lt;1581.0,703.0&gt;&gt; -&gt; L&lt;&lt;1581.0,703.0&gt;--&lt;1582.0,5.0&gt;&gt;

* uni0921_uni0930_uni094D.vatu: L&lt;&lt;1581.0,837.0&gt;--&lt;1581.0,794.0&gt;&gt; -&gt; L&lt;&lt;1581.0,794.0&gt;--&lt;1582.0,164.0&gt;&gt;

* uni0921_uni094D.haln: L&lt;&lt;1581.0,746.0&gt;--&lt;1581.0,703.0&gt;&gt; -&gt; L&lt;&lt;1581.0,703.0&gt;--&lt;1582.0,5.0&gt;&gt;

* uni0943 (U+0943): L&lt;&lt;-612.0,-611.0&gt;--&lt;-655.0,-495.0&gt;&gt; -&gt; L&lt;&lt;-655.0,-495.0&gt;--&lt;-670.0,-455.0&gt;&gt;

* uni0943 (U+0943): L&lt;&lt;-670.0,-455.0&gt;--&lt;-739.0,-269.0&gt;&gt; -&gt; L&lt;&lt;-739.0,-269.0&gt;--&lt;-790.0,-133.0&gt;&gt;

* uni0943 (U+0943): L&lt;&lt;-790.0,-132.0&gt;--&lt;-730.0,-122.0&gt;&gt; -&gt; L&lt;&lt;-730.0,-122.0&gt;--&lt;-8.0,9.0&gt;&gt;

* uni095C (U+095C): L&lt;&lt;1581.0,746.0&gt;--&lt;1581.0,703.0&gt;&gt; -&gt; L&lt;&lt;1581.0,703.0&gt;--&lt;1582.0,5.0&gt;&gt;

* uni095C_uni0930_uni094D.vatu: L&lt;&lt;1581.0,837.0&gt;--&lt;1581.0,794.0&gt;&gt; -&gt; L&lt;&lt;1581.0,794.0&gt;--&lt;1582.0,164.0&gt;&gt;

* uni095C_uni094D.haln: L&lt;&lt;1581.0,746.0&gt;--&lt;1581.0,703.0&gt;&gt; -&gt; L&lt;&lt;1581.0,703.0&gt;--&lt;1582.0,5.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* uni0916_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1587.0,370.0&gt;&gt; = 13.552189259088937

* uni0916_uni0930_uni094D.vatu: L&lt;&lt;52.0,0.0&gt;--&lt;1587.0,370.0&gt;&gt;/L&lt;&lt;1587.0,370.0&gt;--&lt;317.0,370.0&gt;&gt; = 13.552189259088937

* uni0917_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1717.0,401.0&gt;&gt; = 13.541277371563512

* uni0918_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1726.0,403.0&gt;&gt; = 13.535856369134248

* uni091A_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1662.0,388.0&gt;&gt; = 13.549559916764828

* uni091C_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1719.0,402.0&gt;&gt; = 13.558114398357505

* uni091E_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1756.0,411.0&gt;&gt; = 13.560573371057753

* uni0923_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1740.0,407.0&gt;&gt; = 13.556055413364934

* uni0924_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1402.0,325.0&gt;&gt; = 13.535856369134248

* uni0925_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1429.0,332.0&gt;&gt; = 13.555519612214798

* uni0925_uni0930_uni094D.vatu: L&lt;&lt;52.0,0.0&gt;--&lt;1429.0,332.0&gt;&gt;/L&lt;&lt;1429.0,332.0&gt;--&lt;21.0,332.0&gt;&gt; = 13.555519612214798

* uni0927_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1405.0,326.0&gt;&gt; = 13.546974566830361

* uni0927_uni0930_uni094D.vatu: L&lt;&lt;52.0,0.0&gt;--&lt;1405.0,326.0&gt;&gt;/L&lt;&lt;1405.0,326.0&gt;--&lt;90.0,326.0&gt;&gt; = 13.546974566830361

* uni0928_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1730.0,404.0&gt;&gt; = 13.53705172462755

* uni0929_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1727.0,404.0&gt;&gt; = 13.56040263584047

* uni092A_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1723.0,403.0&gt;&gt; = 13.559261261373097

* uni092C_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1684.0,393.0&gt;&gt; = 13.539543474860553

* uni092D_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1752.0,410.0&gt;&gt; = 13.559451870534032

* uni092E_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1770.0,414.0&gt;&gt; = 13.548698506267515

* uni092F_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1209.0,279.0&gt;&gt; = 13.557524842313844

* uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1778.0,416.0&gt;&gt; = 13.550962950816185

* uni0932_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1728.0,404.0&gt;&gt; = 13.552610220387871

* uni0935_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1684.0,393.0&gt;&gt; = 13.539543474860553

* uni0936_uni0930_uni094D.vatu: L&lt;&lt;1797.0,658.0&gt;--&lt;1027.0,922.0&gt;&gt;/L&lt;&lt;1027.0,922.0&gt;--&lt;1197.0,861.0&gt;&gt; = 0.8145364198432462

* uni0937_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1716.0,401.0&gt;&gt; = 13.54911523508201

* uni0948 (U+0948): L&lt;&lt;-22.0,1548.0&gt;--&lt;68.0,1548.0&gt;&gt;/L&lt;&lt;68.0,1548.0&gt;--&lt;-812.0,1750.0&gt;&gt; = 12.928027006757656

* uni0948_uni0902.abvs: L&lt;&lt;-22.0,1548.0&gt;--&lt;68.0,1548.0&gt;&gt;/L&lt;&lt;68.0,1548.0&gt;--&lt;-812.0,1750.0&gt;&gt; = 12.928027006757656

* uni0948_uni0930_uni094D.abvs: L&lt;&lt;-22.0,1548.0&gt;--&lt;68.0,1548.0&gt;&gt;/L&lt;&lt;68.0,1548.0&gt;--&lt;-812.0,1750.0&gt;&gt; = 12.928027006757656

* uni0959_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1587.0,370.0&gt;&gt; = 13.552189259088937

* uni0959_uni0930_uni094D.vatu: L&lt;&lt;52.0,0.0&gt;--&lt;1587.0,370.0&gt;&gt;/L&lt;&lt;1587.0,370.0&gt;--&lt;317.0,370.0&gt;&gt; = 13.552189259088937

* uni095A_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1717.0,401.0&gt;&gt; = 13.541277371563512

* uni095B_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1719.0,402.0&gt;&gt; = 13.558114398357505

* uni095F_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1209.0,279.0&gt;&gt; = 13.557524842313844
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* braceright (U+007D): L&lt;&lt;1040.0,1548.0&gt;--&lt;1036.0,838.0&gt;&gt;

* greater (U+003E): L&lt;&lt;1436.0,777.0&gt;--&lt;1437.0,568.0&gt;&gt;

* guilsinglright (U+203A): L&lt;&lt;1436.0,777.0&gt;--&lt;1437.0,568.0&gt;&gt;

* questiondown (U+00BF): L&lt;&lt;1168.0,1273.0&gt;--&lt;918.0,1272.0&gt;&gt;

* uni0921 (U+0921): L&lt;&lt;1383.0,200.0&gt;--&lt;1382.0,538.0&gt;&gt;

* uni0921 (U+0921): L&lt;&lt;1581.0,703.0&gt;--&lt;1582.0,5.0&gt;&gt;

* uni0921_uni0930_uni094D.vatu: L&lt;&lt;1383.0,359.0&gt;--&lt;1382.0,629.0&gt;&gt;

* uni0921_uni0930_uni094D.vatu: L&lt;&lt;1581.0,794.0&gt;--&lt;1582.0,164.0&gt;&gt;

* uni0921_uni094D.haln: L&lt;&lt;1383.0,200.0&gt;--&lt;1382.0,538.0&gt;&gt;

* uni0921_uni094D.haln: L&lt;&lt;1581.0,703.0&gt;--&lt;1582.0,5.0&gt;&gt;

* uni095C (U+095C): L&lt;&lt;1383.0,200.0&gt;--&lt;1382.0,538.0&gt;&gt;

* uni095C (U+095C): L&lt;&lt;1581.0,703.0&gt;--&lt;1582.0,5.0&gt;&gt;

* uni095C_uni0930_uni094D.vatu: L&lt;&lt;1383.0,359.0&gt;--&lt;1382.0,629.0&gt;&gt;

* uni095C_uni0930_uni094D.vatu: L&lt;&lt;1581.0,794.0&gt;--&lt;1582.0,164.0&gt;&gt;

* uni095C_uni094D.haln: L&lt;&lt;1383.0,200.0&gt;--&lt;1382.0,538.0&gt;&gt;

* uni095C_uni094D.haln: L&lt;&lt;1581.0,703.0&gt;--&lt;1582.0,5.0&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



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

<details><summary>[20] Samaano-Wide-Thin.ttf</summary>
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
<td align="left">U+0189: LATIN CAPITAL LETTER AFRICAN D</td>
<td align="left">U+0256: LATIN SMALL LETTER D WITH TAIL</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



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
    <summary>🔥 <b>FAIL</b> Check family name for GF Guide compliance. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>&quot;Samaano Wide-Thin&quot; contains the following characters which are not allowed: &quot;-&quot;.</p>
 [code: forbidden-characters]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking file is named canonically. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Expected &quot;SamaanoWide-Thin-Regular.ttf. Got Samaano-Wide-Thin.ttf.</p>
 [code: bad-filename]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 355 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



* ⚠️ **WARN** <p>Font is monospaced but 2 glyphs (0.28%) have a different width. You should check the widths of: ['Eng', 'eng']</p>
 [code: mono-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check glyphs in mark glyph class are non-spacing. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following spacing glyphs may be in the GDEF mark glyph class by mistake:
glyph094D (unencoded), uni0331 (U+0331), uni0900 (U+0900), uni0901 (U+0901), uni0902 (U+0902), uni0930_uni094D.blwf (unencoded), uni0930_uni094D.rphf (unencoded), uni093A (U+093A), uni093C (U+093C), uni0941 (U+0941), uni0942 (U+0942), uni0943 (U+0943), uni0944 (U+0944), uni0945 (U+0945), uni0946 (U+0946), uni0947 (U+0947), uni0948 (U+0948), uni094D (U+094D), uni0951 (U+0951), uni0952 (U+0952), uni0953 (U+0953), uni0954 (U+0954), uni0955 (U+0955), uni0956 (U+0956), uni0957 (U+0957), uni0962 (U+0962) and uni0963 (U+0963)</p>
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
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gpos.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning information.</p>
 [code: lacks-kern-info]



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
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: D	Contours detected: 1	Expected: 2

- Glyph name: g	Contours detected: 1	Expected: 2 or 3

- Glyph name: braceleft	Contours detected: 3	Expected: 1

- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: Dcaron	Contours detected: 2	Expected: 3

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: gcircumflex	Contours detected: 2	Expected: 3 or 4

- Glyph name: gbreve	Contours detected: 2	Expected: 3 or 4

- Glyph name: gdotaccent	Contours detected: 2	Expected: 3 or 4

- Glyph name: uni0123	Contours detected: 2	Expected: 3 or 4

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: uni01C4	Contours detected: 3	Expected: 4

- Glyph name: uni01C5	Contours detected: 3	Expected: 4

- Glyph name: uni091B	Contours detected: 1	Expected: 2

- Glyph name: uni092D	Contours detected: 2	Expected: 1

- Glyph name: uni092E	Contours detected: 3	Expected: 2

- Glyph name: uni093D	Contours detected: 2	Expected: 1

- Glyph name: uni0945	Contours detected: 2	Expected: 1

- Glyph name: uni0955	Contours detected: 3	Expected: 2

- Glyph name: uni0956	Contours detected: 2	Expected: 1

- Glyph name: uni0957	Contours detected: 3	Expected: 2

- Glyph name: uni0962	Contours detected: 2	Expected: 1

- Glyph name: uni0963	Contours detected: 2	Expected: 1

- Glyph name: uni0967	Contours detected: 2	Expected: 1

- Glyph name: uni0970	Contours detected: 1	Expected: 2

- Glyph name: uni097F	Contours detected: 2	Expected: 3

- Glyph name: uni1E0C	Contours detected: 2	Expected: 3

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

- Glyph name: D	Contours detected: 1	Expected: 2

- Glyph name: Dcaron	Contours detected: 2	Expected: 3

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: braceleft	Contours detected: 3	Expected: 1

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: g	Contours detected: 1	Expected: 2 or 3

- Glyph name: gbreve	Contours detected: 2	Expected: 3 or 4

- Glyph name: gcircumflex	Contours detected: 2	Expected: 3 or 4

- Glyph name: gdotaccent	Contours detected: 2	Expected: 3 or 4

- Glyph name: uni0123	Contours detected: 2	Expected: 3 or 4

- Glyph name: uni01C4	Contours detected: 3	Expected: 4

- Glyph name: uni01C5	Contours detected: 3	Expected: 4

- Glyph name: uni091B	Contours detected: 1	Expected: 2

- Glyph name: uni092D	Contours detected: 2	Expected: 1

- Glyph name: uni092E	Contours detected: 3	Expected: 2

- Glyph name: uni093D	Contours detected: 2	Expected: 1

- Glyph name: uni0945	Contours detected: 2	Expected: 1

- Glyph name: uni0955	Contours detected: 3	Expected: 2

- Glyph name: uni0956	Contours detected: 2	Expected: 1

- Glyph name: uni0957	Contours detected: 3	Expected: 2

- Glyph name: uni0962	Contours detected: 2	Expected: 1

- Glyph name: uni0963	Contours detected: 2	Expected: 1

- Glyph name: uni0967	Contours detected: 2	Expected: 1

- Glyph name: uni0970	Contours detected: 1	Expected: 2

- Glyph name: uni097F	Contours detected: 2	Expected: 3

- Glyph name: uni1E0C	Contours detected: 2	Expected: 3

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

- Glyph name: uogonek	Contours detected: 2	Expected: 1
</code></pre>
 [code: contour-count]



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







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, tifinagh, coptic, cherokee</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: coptic, glagolitic, gothic, elbasan, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: duployan, malayalam, hebrew, old-permic, todhri, tai-le, coptic, tifinagh, math, syriac, canadian-aboriginal</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: gothic, thai, tifinagh, caucasian-albanian, syriac, sunuwar, cherokee</li>
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
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Nzakara (Latn, 50,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Makaa (Latn, 221,000 speakers), Ejagham (Latn, 120,000 speakers), Igbo (Latn, 27,823,640 speakers), Zapotec (Latn, 490,000 speakers), Aghem (Latn, 38,843 speakers), Yala (Latn, 200,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Sar (Latn, 500,000 speakers), Koonzime (Latn, 40,000 speakers), Mundani (Latn, 34,000 speakers), Dutch (Latn, 31,709,104 speakers), Ngbaka (Latn, 1,020,000 speakers), Ekpeye (Latn, 226,000 speakers), Avokaya (Latn, 100,000 speakers), Mango (Latn, 77,000 speakers), Southern Kisi (Latn, 360,000 speakers), Gulay (Latn, 250,478 speakers), Cicipu (Latn, 44,000 speakers), Basaa (Latn, 332,940 speakers), Dii (Latn, 71,000 speakers), South Central Banda (Latn, 244,000 speakers), Lugbara (Latn, 2,200,000 speakers), Navajo (Latn, 166,319 speakers), Nateni (Latn, 100,000 speakers), Kom (Latn, 360,685 speakers), Belarusian (Cyrl, 10,064,517 speakers), Ma’di (Latn, 584,000 speakers), Ebira (Latn, 2,200,000 speakers), Mfumte (Latn, 79,000 speakers), Bafut (Latn, 158,146 speakers), Vute (Latn, 21,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Fur (Latn, 1,230,163 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Dan (Latn, 1,099,244 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* uni092C (U+092C): L&lt;&lt;136.0,964.0&gt;--&lt;136.0,964.0&gt;&gt; -&gt; L&lt;&lt;136.0,964.0&gt;--&lt;136.0,964.0&gt;&gt;

* uni092C_uni0930_uni094D.vatu: L&lt;&lt;136.0,1264.0&gt;--&lt;136.0,1264.0&gt;&gt; -&gt; L&lt;&lt;136.0,1264.0&gt;--&lt;136.0,1264.0&gt;&gt;

* uni092C_uni094D.half: L&lt;&lt;386.0,964.0&gt;--&lt;386.0,964.0&gt;&gt; -&gt; L&lt;&lt;386.0,964.0&gt;--&lt;386.0,964.0&gt;&gt;

* uni092C_uni094D.haln: L&lt;&lt;136.0,964.0&gt;--&lt;136.0,964.0&gt;&gt; -&gt; L&lt;&lt;136.0,964.0&gt;--&lt;136.0,964.0&gt;&gt;

* uni0930_uni0942.blws: L&lt;&lt;1376.0,1026.0&gt;--&lt;1436.0,1026.0&gt;&gt; -&gt; L&lt;&lt;1436.0,1026.0&gt;--&lt;1436.0,1026.0&gt;&gt;

* uni0930_uni0942.blws: L&lt;&lt;1436.0,1026.0&gt;--&lt;1436.0,1026.0&gt;&gt; -&gt; L&lt;&lt;1436.0,1026.0&gt;--&lt;1836.0,1026.0&gt;&gt;

* uni094F (U+094F): L&lt;&lt;1376.0,1934.0&gt;--&lt;816.0,2060.0&gt;&gt; -&gt; L&lt;&lt;816.0,2060.0&gt;--&lt;789.0,2064.0&gt;&gt;

* uni094F (U+094F): L&lt;&lt;788.0,2066.0&gt;--&lt;797.0,2105.0&gt;&gt; -&gt; L&lt;&lt;797.0,2105.0&gt;--&lt;841.0,2323.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* uni0913 (U+0913): L&lt;&lt;1982.0,1550.0&gt;--&lt;1978.0,1549.0&gt;&gt;/L&lt;&lt;1978.0,1549.0&gt;--&lt;2048.0,1549.0&gt;&gt; = 14.036243467926484

* uni0916_uni0930_uni094D.vatu: L&lt;&lt;190.0,0.0&gt;--&lt;1679.0,370.0&gt;&gt;/L&lt;&lt;1679.0,370.0&gt;--&lt;457.0,370.0&gt;&gt; = 13.95472881922188

* uni0916_uni0930_uni094D.vatu: L&lt;&lt;447.0,0.0&gt;--&lt;190.0,0.0&gt;&gt;/L&lt;&lt;190.0,0.0&gt;--&lt;1679.0,370.0&gt;&gt; = 13.95472881922188

* uni0917_uni0930_uni094D.vatu: L&lt;&lt;453.0,0.0&gt;--&lt;196.0,0.0&gt;&gt;/L&lt;&lt;196.0,0.0&gt;--&lt;1846.0,410.0&gt;&gt; = 13.954509173136843

* uni0918_uni0930_uni094D.vatu: L&lt;&lt;219.0,-49.0&gt;--&lt;1728.0,326.0&gt;&gt;/L&lt;&lt;1728.0,326.0&gt;--&lt;180.0,326.0&gt;&gt; = 13.955809576666178

* uni0918_uni0930_uni094D.vatu: L&lt;&lt;476.0,-49.0&gt;--&lt;219.0,-49.0&gt;&gt;/L&lt;&lt;219.0,-49.0&gt;--&lt;1728.0,326.0&gt;&gt; = 13.955809576666178

* uni091A_uni0930_uni094D.vatu: L&lt;&lt;383.0,0.0&gt;--&lt;126.0,0.0&gt;&gt;/L&lt;&lt;126.0,0.0&gt;--&lt;1800.0,416.0&gt;&gt; = 13.955681401342739

* uni091B_uni0930_uni094D.vatu: L&lt;&lt;383.0,0.0&gt;--&lt;126.0,0.0&gt;&gt;/L&lt;&lt;126.0,0.0&gt;--&lt;1482.0,333.0&gt;&gt; = 13.797388032395103

* uni091C_uni0930_uni094D.vatu: L&lt;&lt;448.0,0.0&gt;--&lt;191.0,0.0&gt;&gt;/L&lt;&lt;191.0,0.0&gt;--&lt;1857.0,414.0&gt;&gt; = 13.95529441255671

* uni091E_uni0930_uni094D.vatu: L&lt;&lt;505.0,0.0&gt;--&lt;248.0,0.0&gt;&gt;/L&lt;&lt;248.0,0.0&gt;--&lt;1899.0,410.0&gt;&gt; = 13.94638702966965

* uni0923_uni0930_uni094D.vatu: L&lt;&lt;481.0,0.0&gt;--&lt;224.0,0.0&gt;&gt;/L&lt;&lt;224.0,0.0&gt;--&lt;1883.0,412.0&gt;&gt; = 13.946820502133802

* uni0925_uni0930_uni094D.vatu: L&lt;&lt;523.0,0.0&gt;--&lt;266.0,0.0&gt;&gt;/L&lt;&lt;266.0,0.0&gt;--&lt;1923.0,412.0&gt;&gt; = 13.962996062429674

* uni0926_uni0930_uni094D.vatu: L&lt;&lt;383.0,0.0&gt;--&lt;126.0,0.0&gt;&gt;/L&lt;&lt;126.0,0.0&gt;--&lt;1262.0,264.0&gt;&gt; = 13.082990674811118

* uni0927_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;219.0,0.0&gt;&gt;/L&lt;&lt;219.0,0.0&gt;--&lt;1880.0,413.0&gt;&gt; = 13.963172511989223

* uni0928_uni0930_uni094D.vatu: L&lt;&lt;470.0,0.0&gt;--&lt;213.0,0.0&gt;&gt;/L&lt;&lt;213.0,0.0&gt;--&lt;1868.0,411.0&gt;&gt; = 13.946604289939135

* uni0929_uni0930_uni094D.vatu: L&lt;&lt;456.0,0.0&gt;--&lt;199.0,0.0&gt;&gt;/L&lt;&lt;199.0,0.0&gt;--&lt;1865.0,414.0&gt;&gt; = 13.95529441255671

* uni092A_uni0930_uni094D.vatu: L&lt;&lt;446.0,0.0&gt;--&lt;189.0,0.0&gt;&gt;/L&lt;&lt;189.0,0.0&gt;--&lt;1851.0,413.0&gt;&gt; = 13.9550995206004

* uni092B_uni0930_uni094D.vatu: L&lt;&lt;383.0,0.0&gt;--&lt;126.0,0.0&gt;&gt;/L&lt;&lt;126.0,0.0&gt;--&lt;1452.0,334.0&gt;&gt; = 14.137867659892134

* uni092C_uni0930_uni094D.vatu: L&lt;&lt;406.0,0.0&gt;--&lt;149.0,0.0&gt;&gt;/L&lt;&lt;149.0,0.0&gt;--&lt;1823.0,416.0&gt;&gt; = 13.955681401342739

* uni092D_uni0930_uni094D.vatu: L&lt;&lt;495.0,0.0&gt;--&lt;238.0,0.0&gt;&gt;/L&lt;&lt;238.0,0.0&gt;--&lt;1892.0,411.0&gt;&gt; = 13.954706907750937

* uni092E_uni0930_uni094D.vatu: L&lt;&lt;507.0,0.0&gt;--&lt;250.0,0.0&gt;&gt;/L&lt;&lt;250.0,0.0&gt;--&lt;1910.0,413.0&gt;&gt; = 13.971254663228907

* uni092F_uni0930_uni094D.vatu: L&lt;&lt;383.0,0.0&gt;--&lt;126.0,0.0&gt;&gt;/L&lt;&lt;126.0,0.0&gt;--&lt;1863.0,323.0&gt;&gt; = 10.533993557738619

* uni0930_uni0930_uni094D.vatu: L&lt;&lt;383.0,0.0&gt;--&lt;126.0,0.0&gt;&gt;/L&lt;&lt;126.0,0.0&gt;--&lt;1045.0,230.0&gt;&gt; = 14.050912125955458

* uni0930_uni094D.vatu: L&lt;&lt;383.0,0.0&gt;--&lt;126.0,0.0&gt;&gt;/L&lt;&lt;126.0,0.0&gt;--&lt;1800.0,416.0&gt;&gt; = 13.955681401342739

* uni0931_uni0930_uni094D.vatu: L&lt;&lt;383.0,0.0&gt;--&lt;126.0,0.0&gt;&gt;/L&lt;&lt;126.0,0.0&gt;--&lt;1084.0,202.0&gt;&gt; = 11.906741925249397

* uni0932_uni0930_uni094D.vatu: L&lt;&lt;493.0,0.0&gt;--&lt;236.0,0.0&gt;&gt;/L&lt;&lt;236.0,0.0&gt;--&lt;1868.0,404.0&gt;&gt; = 13.903997241115658

* uni0935_uni0930_uni094D.vatu: L&lt;&lt;426.0,0.0&gt;--&lt;169.0,0.0&gt;&gt;/L&lt;&lt;169.0,0.0&gt;--&lt;1824.0,411.0&gt;&gt; = 13.946604289939135

* uni0937_uni0930_uni094D.vatu: L&lt;&lt;458.0,6.0&gt;--&lt;201.0,6.0&gt;&gt;/L&lt;&lt;201.0,6.0&gt;--&lt;1851.0,416.0&gt;&gt; = 13.954509173136843

* uni0939_uni0930_uni094D.vatu: L&lt;&lt;823.0,370.0&gt;--&lt;566.0,370.0&gt;&gt;/L&lt;&lt;566.0,370.0&gt;--&lt;1542.0,615.0&gt;&gt; = 14.091481608935501

* uni0944 (U+0944): L&lt;&lt;14.0,-841.0&gt;--&lt;-764.0,-947.0&gt;&gt;/L&lt;&lt;-764.0,-947.0&gt;--&lt;-764.0,-947.0&gt;&gt; = 7.758593140226185

* uni0959_uni0930_uni094D.vatu: L&lt;&lt;190.0,0.0&gt;--&lt;1679.0,370.0&gt;&gt;/L&lt;&lt;1679.0,370.0&gt;--&lt;457.0,370.0&gt;&gt; = 13.95472881922188

* uni0959_uni0930_uni094D.vatu: L&lt;&lt;447.0,0.0&gt;--&lt;190.0,0.0&gt;&gt;/L&lt;&lt;190.0,0.0&gt;--&lt;1679.0,370.0&gt;&gt; = 13.95472881922188

* uni095A_uni0930_uni094D.vatu: L&lt;&lt;453.0,0.0&gt;--&lt;196.0,0.0&gt;&gt;/L&lt;&lt;196.0,0.0&gt;--&lt;1846.0,410.0&gt;&gt; = 13.954509173136843

* uni095B_uni0930_uni094D.vatu: L&lt;&lt;448.0,0.0&gt;--&lt;191.0,0.0&gt;&gt;/L&lt;&lt;191.0,0.0&gt;--&lt;1857.0,414.0&gt;&gt; = 13.95529441255671

* uni095E_uni0930_uni094D.vatu: L&lt;&lt;383.0,0.0&gt;--&lt;126.0,0.0&gt;&gt;/L&lt;&lt;126.0,0.0&gt;--&lt;1452.0,334.0&gt;&gt; = 14.137867659892134

* uni095F_uni0930_uni094D.vatu: L&lt;&lt;383.0,0.0&gt;--&lt;126.0,0.0&gt;&gt;/L&lt;&lt;126.0,0.0&gt;--&lt;1863.0,323.0&gt;&gt; = 10.533993557738619

* uni0968 (U+0968): L&lt;&lt;221.0,486.0&gt;--&lt;239.0,488.0&gt;&gt;/L&lt;&lt;239.0,488.0&gt;--&lt;224.0,488.0&gt;&gt; = 6.340191745909908
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* braceright (U+007D): L&lt;&lt;1040.0,1544.0&gt;--&lt;1039.0,838.0&gt;&gt;

* eight (U+0038): L&lt;&lt;1993.0,-3.0&gt;--&lt;56.0,0.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;1050.0,1035.0&gt;--&lt;1054.0,17.0&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



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

<details><summary>[21] Samaano-Bold-Slanted.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead.</p>
 [code: mono-bad-post-isFixedPitch]



* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 435 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking head.macStyle value. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.head.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>head macStyle BOLD bit should be set.</p>
 [code: bad-BOLD]





</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 fsSelection value. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.os2.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2 fsSelection REGULAR bit should be unset.</p>
 [code: bad-REGULAR]



* 🔥 **FAIL** <p>OS/2 fsSelection BOLD bit should be set.</p>
 [code: bad-BOLD]





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
    <summary>🔥 <b>FAIL</b> Check family name for GF Guide compliance. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>&quot;Samaano Bold-Slanted&quot; contains the following characters which are not allowed: &quot;-&quot;.</p>
 [code: forbidden-characters]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking file is named canonically. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Expected &quot;SamaanoBold-Slanted-Regular.ttf. Got Samaano-Bold-Slanted.ttf.</p>
 [code: bad-filename]



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
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gpos.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning information.</p>
 [code: lacks-kern-info]



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
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: parenleft	Contours detected: 2	Expected: 1

- Glyph name: B	Contours detected: 1	Expected: 2 or 3

- Glyph name: D	Contours detected: 1	Expected: 2

- Glyph name: Z	Contours detected: 2	Expected: 1

- Glyph name: braceleft	Contours detected: 2	Expected: 1

- Glyph name: mu	Contours detected: 2	Expected: 1

- Glyph name: Eth	Contours detected: 1	Expected: 2

- Glyph name: germandbls	Contours detected: 3	Expected: 1

- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: Dcaron	Contours detected: 2	Expected: 3

- Glyph name: Dcroat	Contours detected: 1	Expected: 2

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: Zacute	Contours detected: 3	Expected: 2

- Glyph name: Zdotaccent	Contours detected: 3	Expected: 2

- Glyph name: Zcaron	Contours detected: 3	Expected: 2

- Glyph name: uni01C5	Contours detected: 3	Expected: 4

- Glyph name: uni090B	Contours detected: 2	Expected: 1

- Glyph name: uni0916	Contours detected: 2	Expected: 1 or 3

- Glyph name: uni091B	Contours detected: 1	Expected: 2

- Glyph name: uni092D	Contours detected: 2	Expected: 1

- Glyph name: uni092E	Contours detected: 3	Expected: 2

- Glyph name: uni093D	Contours detected: 3	Expected: 1

- Glyph name: uni0945	Contours detected: 2	Expected: 1

- Glyph name: uni0955	Contours detected: 3	Expected: 2

- Glyph name: uni0956	Contours detected: 2	Expected: 1

- Glyph name: uni0957	Contours detected: 3	Expected: 2

- Glyph name: uni0959	Contours detected: 3	Expected: 2 or 4

- Glyph name: uni0960	Contours detected: 2	Expected: 1

- Glyph name: uni0962	Contours detected: 2	Expected: 1

- Glyph name: uni0963	Contours detected: 2	Expected: 1

- Glyph name: uni0967	Contours detected: 2	Expected: 1

- Glyph name: uni0970	Contours detected: 1	Expected: 2

- Glyph name: uni097F	Contours detected: 2	Expected: 3

- Glyph name: uni1E0C	Contours detected: 2	Expected: 3

- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

- Glyph name: B	Contours detected: 1	Expected: 2 or 3

- Glyph name: D	Contours detected: 1	Expected: 2

- Glyph name: Dcaron	Contours detected: 2	Expected: 3

- Glyph name: Dcroat	Contours detected: 1	Expected: 2

- Glyph name: Eth	Contours detected: 1	Expected: 2

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: Z	Contours detected: 2	Expected: 1

- Glyph name: Zacute	Contours detected: 3	Expected: 2

- Glyph name: Zcaron	Contours detected: 3	Expected: 2

- Glyph name: Zdotaccent	Contours detected: 3	Expected: 2

- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: braceleft	Contours detected: 2	Expected: 1

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: germandbls	Contours detected: 3	Expected: 1

- Glyph name: parenleft	Contours detected: 2	Expected: 1

- Glyph name: uni01C5	Contours detected: 3	Expected: 4

- Glyph name: uni090B	Contours detected: 2	Expected: 1

- Glyph name: uni0916	Contours detected: 2	Expected: 1 or 3

- Glyph name: uni091B	Contours detected: 1	Expected: 2

- Glyph name: uni092D	Contours detected: 2	Expected: 1

- Glyph name: uni092E	Contours detected: 3	Expected: 2

- Glyph name: uni093D	Contours detected: 3	Expected: 1

- Glyph name: uni0945	Contours detected: 2	Expected: 1

- Glyph name: uni0955	Contours detected: 3	Expected: 2

- Glyph name: uni0956	Contours detected: 2	Expected: 1

- Glyph name: uni0957	Contours detected: 3	Expected: 2

- Glyph name: uni0959	Contours detected: 3	Expected: 2 or 4

- Glyph name: uni0960	Contours detected: 2	Expected: 1

- Glyph name: uni0962	Contours detected: 2	Expected: 1

- Glyph name: uni0963	Contours detected: 2	Expected: 1

- Glyph name: uni0967	Contours detected: 2	Expected: 1

- Glyph name: uni0970	Contours detected: 1	Expected: 2

- Glyph name: uni097F	Contours detected: 2	Expected: 3

- Glyph name: uni1E0C	Contours detected: 2	Expected: 3

- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

- Glyph name: uogonek	Contours detected: 2	Expected: 1
</code></pre>
 [code: contour-count]



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







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, tifinagh, coptic, cherokee</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: coptic, glagolitic, gothic, elbasan, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: duployan, malayalam, hebrew, old-permic, todhri, tai-le, coptic, tifinagh, math, syriac, canadian-aboriginal</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: gothic, thai, tifinagh, caucasian-albanian, syriac, sunuwar, cherokee</li>
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
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Nzakara (Latn, 50,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Makaa (Latn, 221,000 speakers), Ejagham (Latn, 120,000 speakers), Igbo (Latn, 27,823,640 speakers), Zapotec (Latn, 490,000 speakers), Aghem (Latn, 38,843 speakers), Yala (Latn, 200,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Sar (Latn, 500,000 speakers), Koonzime (Latn, 40,000 speakers), Mundani (Latn, 34,000 speakers), Dutch (Latn, 31,709,104 speakers), Ngbaka (Latn, 1,020,000 speakers), Ekpeye (Latn, 226,000 speakers), Avokaya (Latn, 100,000 speakers), Mango (Latn, 77,000 speakers), Southern Kisi (Latn, 360,000 speakers), Gulay (Latn, 250,478 speakers), Cicipu (Latn, 44,000 speakers), Basaa (Latn, 332,940 speakers), Dii (Latn, 71,000 speakers), South Central Banda (Latn, 244,000 speakers), Lugbara (Latn, 2,200,000 speakers), Navajo (Latn, 166,319 speakers), Nateni (Latn, 100,000 speakers), Kom (Latn, 360,685 speakers), Belarusian (Cyrl, 10,064,517 speakers), Ma’di (Latn, 584,000 speakers), Ebira (Latn, 2,200,000 speakers), Mfumte (Latn, 79,000 speakers), Bafut (Latn, 158,146 speakers), Vute (Latn, 21,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Fur (Latn, 1,230,163 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Dan (Latn, 1,099,244 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have on-curve points which have potentially incorrect y coordinates:</p>
<pre><code>* N (U+004E): X=444.0,Y=2.0 (should be at baseline 0?)

* Ntilde (U+00D1): X=405.0,Y=2.0 (should be at baseline 0?)

* Nacute (U+0143): X=444.0,Y=2.0 (should be at baseline 0?)

* uni0145 (U+0145): X=444.0,Y=2.0 (should be at baseline 0?)

* Ncaron (U+0147): X=444.0,Y=2.0 (should be at baseline 0?)

* Eng (U+014A): X=395.0,Y=1550.0 (should be at cap-height 1548?)

* Eng (U+014A): X=1194.0,Y=1550.0 (should be at cap-height 1548?)

* uni1E44 (U+1E44): X=444.0,Y=2.0 (should be at baseline 0?)

* uni1E46 (U+1E46): X=444.0,Y=2.0 (should be at baseline 0?)

* uni1E48 (U+1E48): X=444.0,Y=2.0 (should be at baseline 0?)

* uni1E4D (U+1E4D): X=662.0,Y=1550.0 (should be at cap-height 1548?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* glyph094D: L&lt;&lt;630.0,-22.0&gt;--&lt;629.0,-23.0&gt;&gt;/L&lt;&lt;629.0,-23.0&gt;--&lt;632.0,-21.0&gt;&gt; = 11.309932474020227

* uni01C4 (U+01C4): L&lt;&lt;336.0,767.0&gt;--&lt;337.0,771.0&gt;&gt;/L&lt;&lt;337.0,771.0&gt;--&lt;336.0,769.0&gt;&gt; = 12.528807709151492

* uni01C4 (U+01C4): L&lt;&lt;336.0,769.0&gt;--&lt;-320.0,0.0&gt;&gt;/L&lt;&lt;-320.0,0.0&gt;--&lt;-210.0,201.0&gt;&gt; = 11.775746289963823

* uni01C5 (U+01C5): L&lt;&lt;553.0,769.0&gt;--&lt;-102.0,0.0&gt;&gt;/L&lt;&lt;-102.0,0.0&gt;--&lt;7.0,201.0&gt;&gt; = 11.952410103730198

* uni0915_uni094D.haln: L&lt;&lt;370.0,-22.0&gt;--&lt;369.0,-23.0&gt;&gt;/L&lt;&lt;369.0,-23.0&gt;--&lt;372.0,-21.0&gt;&gt; = 11.309932474020227

* uni0915_uni094D_uni0937_uni094D: L&lt;&lt;1363.0,-22.0&gt;--&lt;1362.0,-23.0&gt;&gt;/L&lt;&lt;1362.0,-23.0&gt;--&lt;1365.0,-21.0&gt;&gt; = 11.309932474020227

* uni0916_uni094D.haln: L&lt;&lt;285.0,-22.0&gt;--&lt;284.0,-23.0&gt;&gt;/L&lt;&lt;284.0,-23.0&gt;--&lt;287.0,-21.0&gt;&gt; = 11.309932474020227

* uni091A_uni094D.haln: L&lt;&lt;447.0,-22.0&gt;--&lt;446.0,-23.0&gt;&gt;/L&lt;&lt;446.0,-23.0&gt;--&lt;449.0,-21.0&gt;&gt; = 11.309932474020227

* uni091B_uni094D.haln: L&lt;&lt;98.0,-13.0&gt;--&lt;97.0,-14.0&gt;&gt;/L&lt;&lt;97.0,-14.0&gt;--&lt;100.0,-12.0&gt;&gt; = 11.309932474020227

* uni091C_uni094D.haln: L&lt;&lt;264.0,-22.0&gt;--&lt;263.0,-23.0&gt;&gt;/L&lt;&lt;263.0,-23.0&gt;--&lt;266.0,-21.0&gt;&gt; = 11.309932474020227

* uni091C_uni094D_uni091E_uni094D: L&lt;&lt;1294.0,-22.0&gt;--&lt;1293.0,-23.0&gt;&gt;/L&lt;&lt;1293.0,-23.0&gt;--&lt;1296.0,-21.0&gt;&gt; = 11.309932474020227

* uni0926_uni094D.half: L&lt;&lt;359.0,-22.0&gt;--&lt;358.0,-23.0&gt;&gt;/L&lt;&lt;358.0,-23.0&gt;--&lt;361.0,-21.0&gt;&gt; = 11.309932474020227

* uni0926_uni094D.haln: L&lt;&lt;241.0,-22.0&gt;--&lt;240.0,-23.0&gt;&gt;/L&lt;&lt;240.0,-23.0&gt;--&lt;243.0,-21.0&gt;&gt; = 11.309932474020227

* uni0929_uni094D.haln: L&lt;&lt;511.0,-22.0&gt;--&lt;510.0,-23.0&gt;&gt;/L&lt;&lt;510.0,-23.0&gt;--&lt;513.0,-21.0&gt;&gt; = 11.309932474020227

* uni092A_uni094D.haln: L&lt;&lt;397.0,-22.0&gt;--&lt;396.0,-23.0&gt;&gt;/L&lt;&lt;396.0,-23.0&gt;--&lt;399.0,-21.0&gt;&gt; = 11.309932474020227

* uni092B_uni094D.haln: L&lt;&lt;485.0,-22.0&gt;--&lt;484.0,-23.0&gt;&gt;/L&lt;&lt;484.0,-23.0&gt;--&lt;487.0,-21.0&gt;&gt; = 11.309932474020227

* uni0937_uni094D.haln: L&lt;&lt;396.0,-22.0&gt;--&lt;395.0,-23.0&gt;&gt;/L&lt;&lt;395.0,-23.0&gt;--&lt;398.0,-21.0&gt;&gt; = 11.309932474020227

* uni0938_uni094D.haln: L&lt;&lt;504.0,-22.0&gt;--&lt;503.0,-23.0&gt;&gt;/L&lt;&lt;503.0,-23.0&gt;--&lt;506.0,-21.0&gt;&gt; = 11.309932474020227

* uni0959_uni094D.haln: L&lt;&lt;286.0,-22.0&gt;--&lt;285.0,-23.0&gt;&gt;/L&lt;&lt;285.0,-23.0&gt;--&lt;288.0,-21.0&gt;&gt; = 11.309932474020227
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* questiondown (U+00BF): L&lt;&lt;930.0,1273.0&gt;--&lt;680.0,1272.0&gt;&gt;

* uni091C_uni094D_uni091E_uni094D: L&lt;&lt;-114.0,367.0&gt;--&lt;-112.0,75.0&gt;&gt;

* uni0930_uni0942.blws: L&lt;&lt;1113.0,1348.0&gt;--&lt;541.0,1347.0&gt;&gt;

* uni093D (U+093D): L&lt;&lt;626.0,1079.0&gt;--&lt;624.0,269.0&gt;&gt;

* uni0943 (U+0943): L&lt;&lt;-289.0,-250.0&gt;--&lt;-288.0,-385.0&gt;&gt;

* uni0943 (U+0943): L&lt;&lt;-500.0,-611.0&gt;--&lt;-501.0,-495.0&gt;&gt;

* uni0943 (U+0943): L&lt;&lt;-503.0,-270.0&gt;--&lt;-504.0,-133.0&gt;&gt;

* uni0943 (U+0943): L&lt;&lt;-70.0,9.0&gt;--&lt;-69.0,-178.0&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



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

<details><summary>[19] Samaano-Thin-Slanted.ttf</summary>
<div>
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
    <summary>🔥 <b>FAIL</b> Check family name for GF Guide compliance. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>&quot;Samaano Thin-Slanted&quot; contains the following characters which are not allowed: &quot;-&quot;.</p>
 [code: forbidden-characters]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking file is named canonically. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Expected &quot;SamaanoThin-Slanted-Regular.ttf. Got Samaano-Thin-Slanted.ttf.</p>
 [code: bad-filename]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Font has all mandatory 'name' table entries? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Font lacks entry with nameId=16 (TYPOGRAPHIC_FAMILY_NAME)</p>
 [code: missing-entry]



* 🔥 **FAIL** <p>Font lacks entry with nameId=17 (TYPOGRAPHIC_SUBFAMILY_NAME)</p>
 [code: missing-entry]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 425 instead.
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
acutecomb (U+0301), dotbelowcomb (U+0323), glyph094D (unencoded), tildecomb (U+0303), uni0302 (U+0302), uni0304 (U+0304), uni0306 (U+0306), uni0307 (U+0307), uni0308 (U+0308), uni030A (U+030A), uni030B (U+030B), uni0326 (U+0326), uni0327 (U+0327), uni0328 (U+0328), uni0331 (U+0331), uni0930_uni094D.blwf (unencoded), uni0930_uni094D.rphf (unencoded), uni093A (U+093A), uni093C (U+093C), uni0945 (U+0945), uni0946 (U+0946), uni0947 (U+0947), uni0948 (U+0948), uni094D (U+094D), uni0951 (U+0951), uni0952 (U+0952), uni0953 (U+0953), uni0954 (U+0954), uni0955 (U+0955), uni0956 (U+0956), uni0957 (U+0957), uni0962 (U+0962) and uni0963 (U+0963)</p>
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
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gpos.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning information.</p>
 [code: lacks-kern-info]



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
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: A	Contours detected: 1	Expected: 2

- Glyph name: g	Contours detected: 1	Expected: 2 or 3

- Glyph name: o	Contours detected: 1	Expected: 2

- Glyph name: braceleft	Contours detected: 2	Expected: 1

- Glyph name: Agrave	Contours detected: 2	Expected: 3

- Glyph name: Aacute	Contours detected: 2	Expected: 3

- Glyph name: Acircumflex	Contours detected: 2	Expected: 3

- Glyph name: Atilde	Contours detected: 2	Expected: 3

- Glyph name: Adieresis	Contours detected: 3	Expected: 4

- Glyph name: ograve	Contours detected: 2	Expected: 3

- Glyph name: oacute	Contours detected: 2	Expected: 3

- Glyph name: ocircumflex	Contours detected: 2	Expected: 3

- Glyph name: otilde	Contours detected: 2	Expected: 3

- Glyph name: odieresis	Contours detected: 3	Expected: 4

- Glyph name: Amacron	Contours detected: 2	Expected: 3

- Glyph name: Abreve	Contours detected: 2	Expected: 3

- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: gcircumflex	Contours detected: 2	Expected: 3 or 4

- Glyph name: gbreve	Contours detected: 2	Expected: 3 or 4

- Glyph name: gdotaccent	Contours detected: 2	Expected: 3 or 4

- Glyph name: uni0123	Contours detected: 2	Expected: 3 or 4

- Glyph name: Eng	Contours detected: 2	Expected: 1

- Glyph name: omacron	Contours detected: 2	Expected: 3

- Glyph name: obreve	Contours detected: 2	Expected: 3

- Glyph name: ohungarumlaut	Contours detected: 3	Expected: 4

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: uni0910	Contours detected: 2	Expected: 1

- Glyph name: uni091B	Contours detected: 1	Expected: 2

- Glyph name: uni092D	Contours detected: 2	Expected: 1

- Glyph name: uni092E	Contours detected: 3	Expected: 2

- Glyph name: uni093D	Contours detected: 2	Expected: 1

- Glyph name: uni0945	Contours detected: 2	Expected: 1

- Glyph name: uni0955	Contours detected: 3	Expected: 2

- Glyph name: uni0956	Contours detected: 2	Expected: 1

- Glyph name: uni0957	Contours detected: 3	Expected: 2

- Glyph name: uni0962	Contours detected: 2	Expected: 1

- Glyph name: uni0963	Contours detected: 2	Expected: 1

- Glyph name: uni0967	Contours detected: 2	Expected: 1

- Glyph name: uni0970	Contours detected: 1	Expected: 2

- Glyph name: uni097F	Contours detected: 2	Expected: 3

- Glyph name: uni1E4D	Contours detected: 3	Expected: 4

- Glyph name: wacute	Contours detected: 1	Expected: 2

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

- Glyph name: A	Contours detected: 1	Expected: 2

- Glyph name: Aacute	Contours detected: 2	Expected: 3

- Glyph name: Abreve	Contours detected: 2	Expected: 3

- Glyph name: Acircumflex	Contours detected: 2	Expected: 3

- Glyph name: Adieresis	Contours detected: 3	Expected: 4

- Glyph name: Agrave	Contours detected: 2	Expected: 3

- Glyph name: Amacron	Contours detected: 2	Expected: 3

- Glyph name: Atilde	Contours detected: 2	Expected: 3

- Glyph name: Eng	Contours detected: 2	Expected: 1

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: braceleft	Contours detected: 2	Expected: 1

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: g	Contours detected: 1	Expected: 2 or 3

- Glyph name: gbreve	Contours detected: 2	Expected: 3 or 4

- Glyph name: gcircumflex	Contours detected: 2	Expected: 3 or 4

- Glyph name: gdotaccent	Contours detected: 2	Expected: 3 or 4

- Glyph name: o	Contours detected: 1	Expected: 2

- Glyph name: oacute	Contours detected: 2	Expected: 3

- Glyph name: ocircumflex	Contours detected: 2	Expected: 3

- Glyph name: odieresis	Contours detected: 3	Expected: 4

- Glyph name: ograve	Contours detected: 2	Expected: 3

- Glyph name: ohungarumlaut	Contours detected: 3	Expected: 4

- Glyph name: omacron	Contours detected: 2	Expected: 3

- Glyph name: otilde	Contours detected: 2	Expected: 3

- Glyph name: uni0123	Contours detected: 2	Expected: 3 or 4

- Glyph name: uni0910	Contours detected: 2	Expected: 1

- Glyph name: uni091B	Contours detected: 1	Expected: 2

- Glyph name: uni092D	Contours detected: 2	Expected: 1

- Glyph name: uni092E	Contours detected: 3	Expected: 2

- Glyph name: uni093D	Contours detected: 2	Expected: 1

- Glyph name: uni0945	Contours detected: 2	Expected: 1

- Glyph name: uni0955	Contours detected: 3	Expected: 2

- Glyph name: uni0956	Contours detected: 2	Expected: 1

- Glyph name: uni0957	Contours detected: 3	Expected: 2

- Glyph name: uni0962	Contours detected: 2	Expected: 1

- Glyph name: uni0963	Contours detected: 2	Expected: 1

- Glyph name: uni0967	Contours detected: 2	Expected: 1

- Glyph name: uni0970	Contours detected: 1	Expected: 2

- Glyph name: uni097F	Contours detected: 2	Expected: 3

- Glyph name: uni1E4D	Contours detected: 3	Expected: 4

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: wacute	Contours detected: 1	Expected: 2
</code></pre>
 [code: contour-count]



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







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, tifinagh, coptic, cherokee</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: coptic, glagolitic, gothic, elbasan, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: duployan, malayalam, hebrew, old-permic, todhri, tai-le, coptic, tifinagh, math, syriac, canadian-aboriginal</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: gothic, thai, tifinagh, caucasian-albanian, syriac, sunuwar, cherokee</li>
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
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Nzakara (Latn, 50,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Makaa (Latn, 221,000 speakers), Ejagham (Latn, 120,000 speakers), Igbo (Latn, 27,823,640 speakers), Zapotec (Latn, 490,000 speakers), Aghem (Latn, 38,843 speakers), Yala (Latn, 200,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Sar (Latn, 500,000 speakers), Koonzime (Latn, 40,000 speakers), Mundani (Latn, 34,000 speakers), Dutch (Latn, 31,709,104 speakers), Ngbaka (Latn, 1,020,000 speakers), Ekpeye (Latn, 226,000 speakers), Avokaya (Latn, 100,000 speakers), Mango (Latn, 77,000 speakers), Southern Kisi (Latn, 360,000 speakers), Gulay (Latn, 250,478 speakers), Cicipu (Latn, 44,000 speakers), Basaa (Latn, 332,940 speakers), Dii (Latn, 71,000 speakers), South Central Banda (Latn, 244,000 speakers), Lugbara (Latn, 2,200,000 speakers), Navajo (Latn, 166,319 speakers), Nateni (Latn, 100,000 speakers), Kom (Latn, 360,685 speakers), Belarusian (Cyrl, 10,064,517 speakers), Ma’di (Latn, 584,000 speakers), Ebira (Latn, 2,200,000 speakers), Mfumte (Latn, 79,000 speakers), Bafut (Latn, 158,146 speakers), Vute (Latn, 21,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Fur (Latn, 1,230,163 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Dan (Latn, 1,099,244 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* uni0913 (U+0913): L&lt;&lt;1120.0,1550.0&gt;--&lt;1116.0,1549.0&gt;&gt;/L&lt;&lt;1116.0,1549.0&gt;--&lt;1298.0,1549.0&gt;&gt; = 14.036243467926484

* uni093D (U+093D): L&lt;&lt;179.0,104.0&gt;--&lt;190.0,127.0&gt;&gt;/L&lt;&lt;190.0,127.0&gt;--&lt;179.0,107.0&gt;&gt; = 3.250828571149245

* uni0944 (U+0944): L&lt;&lt;-130.0,-841.0&gt;--&lt;-527.0,-942.0&gt;&gt;/L&lt;&lt;-527.0,-942.0&gt;--&lt;-527.0,-942.0&gt;&gt; = 14.273702414211385

* uni0944 (U+0944): L&lt;&lt;-527.0,-942.0&gt;--&lt;-527.0,-942.0&gt;&gt;/L&lt;&lt;-527.0,-942.0&gt;--&lt;-539.0,-945.0&gt;&gt; = 14.036243467926484

* uni0944 (U+0944): L&lt;&lt;-539.0,-945.0&gt;--&lt;-547.0,-947.0&gt;&gt;/L&lt;&lt;-547.0,-947.0&gt;--&lt;-547.0,-947.0&gt;&gt; = 14.036243467926484

* uni0944 (U+0944): L&lt;&lt;-547.0,-947.0&gt;--&lt;-547.0,-947.0&gt;&gt;/L&lt;&lt;-547.0,-947.0&gt;--&lt;-591.0,-958.0&gt;&gt; = 14.036243467926484

* uni0968 (U+0968): L&lt;&lt;45.0,486.0&gt;--&lt;64.0,488.0&gt;&gt;/L&lt;&lt;64.0,488.0&gt;--&lt;48.0,488.0&gt;&gt; = 6.009005957494474
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* a (U+0061): L&lt;&lt;353.0,1024.0&gt;--&lt;1001.0,1023.0&gt;&gt;

* aacute (U+00E1): L&lt;&lt;353.0,1024.0&gt;--&lt;1001.0,1023.0&gt;&gt;

* abreve (U+0103): L&lt;&lt;353.0,1024.0&gt;--&lt;1001.0,1023.0&gt;&gt;

* acircumflex (U+00E2): L&lt;&lt;353.0,1024.0&gt;--&lt;1001.0,1023.0&gt;&gt;

* adieresis (U+00E4): L&lt;&lt;353.0,1024.0&gt;--&lt;1001.0,1023.0&gt;&gt;

* agrave (U+00E0): L&lt;&lt;353.0,1024.0&gt;--&lt;1001.0,1023.0&gt;&gt;

* amacron (U+0101): L&lt;&lt;353.0,1024.0&gt;--&lt;1001.0,1023.0&gt;&gt;

* aogonek (U+0105): L&lt;&lt;353.0,1024.0&gt;--&lt;1001.0,1023.0&gt;&gt;

* aring (U+00E5): L&lt;&lt;353.0,1024.0&gt;--&lt;1001.0,1023.0&gt;&gt;

* atilde (U+00E3): L&lt;&lt;353.0,1024.0&gt;--&lt;1001.0,1023.0&gt;&gt;

* backslash (U+005C): L&lt;&lt;466.0,0.0&gt;--&lt;475.0,1550.0&gt;&gt;

* trademark (U+2122): L&lt;&lt;699.0,905.0&gt;--&lt;700.0,1123.0&gt;&gt;

* uni0938_uni094D.haln: L&lt;&lt;-182.0,659.0&gt;--&lt;-186.0,0.0&gt;&gt;

* uni0943 (U+0943): L&lt;&lt;-431.0,-169.0&gt;--&lt;-428.0,-566.0&gt;&gt;

* uni0943 (U+0943): L&lt;&lt;-501.0,-590.0&gt;--&lt;-504.0,-132.0&gt;&gt;

* uni0947_uni0902.abvs: L&lt;&lt;126.0,1553.0&gt;--&lt;127.0,1724.0&gt;&gt;

* uni0947_uni0902.abvs: L&lt;&lt;127.0,1738.0&gt;--&lt;128.0,1962.0&gt;&gt;

* uni0947_uni0930_uni094D.abvs: L&lt;&lt;105.0,1553.0&gt;--&lt;107.0,1962.0&gt;&gt;

* uni1E42 (U+1E42): L&lt;&lt;663.0,1033.0&gt;--&lt;665.0,1470.0&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



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

<details><summary>[22] Samaano-Wide-Bold-Slanted.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>On monospaced fonts, the value of post.isFixedPitch must be set to a non-zero value (meaning 'fixed width monospaced'), but got 0 instead.</p>
 [code: mono-bad-post-isFixedPitch]



* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 445 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



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
<td align="left">U+0189: LATIN CAPITAL LETTER AFRICAN D</td>
<td align="left">U+0256: LATIN SMALL LETTER D WITH TAIL</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs have no contours even though they were expected to have some:</p>
<pre><code>- Glyph name: kgreenlandic	Expected: 1 or 2

- Glyph name: Tbar	Expected: 1

- Glyph name: tbar	Expected: 1

- Glyph name: Tbar	Expected: 1

- Glyph name: kgreenlandic	Expected: 1 or 2

- Glyph name: tbar	Expected: 1
</code></pre>
 [code: no-contour]



* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: parenleft	Contours detected: 2	Expected: 1

- Glyph name: D	Contours detected: 1	Expected: 2

- Glyph name: Z	Contours detected: 2	Expected: 1

- Glyph name: braceleft	Contours detected: 2	Expected: 1

- Glyph name: mu	Contours detected: 2	Expected: 1

- Glyph name: germandbls	Contours detected: 3	Expected: 1

- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: Dcaron	Contours detected: 2	Expected: 3

- Glyph name: Dcroat	Contours detected: 1	Expected: 2

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: Zacute	Contours detected: 3	Expected: 2

- Glyph name: Zdotaccent	Contours detected: 3	Expected: 2

- Glyph name: Zcaron	Contours detected: 3	Expected: 2

- Glyph name: Eth	Contours detected: 1	Expected: 2

- Glyph name: uni01C5	Contours detected: 3	Expected: 4

- Glyph name: uni090B	Contours detected: 2	Expected: 1

- Glyph name: uni0916	Contours detected: 2	Expected: 1 or 3

- Glyph name: uni091B	Contours detected: 1	Expected: 2

- Glyph name: uni092D	Contours detected: 2	Expected: 1

- Glyph name: uni092E	Contours detected: 3	Expected: 2

- Glyph name: uni093D	Contours detected: 3	Expected: 1

- Glyph name: uni0945	Contours detected: 2	Expected: 1

- Glyph name: uni0955	Contours detected: 3	Expected: 2

- Glyph name: uni0956	Contours detected: 2	Expected: 1

- Glyph name: uni0957	Contours detected: 3	Expected: 2

- Glyph name: uni0959	Contours detected: 3	Expected: 2 or 4

- Glyph name: uni0960	Contours detected: 2	Expected: 1

- Glyph name: uni0962	Contours detected: 2	Expected: 1

- Glyph name: uni0963	Contours detected: 2	Expected: 1

- Glyph name: uni0967	Contours detected: 2	Expected: 1

- Glyph name: uni0970	Contours detected: 1	Expected: 2

- Glyph name: uni097F	Contours detected: 2	Expected: 3

- Glyph name: uni1E0C	Contours detected: 2	Expected: 3

- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

- Glyph name: D	Contours detected: 1	Expected: 2

- Glyph name: Dcaron	Contours detected: 2	Expected: 3

- Glyph name: Dcroat	Contours detected: 1	Expected: 2

- Glyph name: Eth	Contours detected: 1	Expected: 2

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: Z	Contours detected: 2	Expected: 1

- Glyph name: Zacute	Contours detected: 3	Expected: 2

- Glyph name: Zcaron	Contours detected: 3	Expected: 2

- Glyph name: Zdotaccent	Contours detected: 3	Expected: 2

- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: braceleft	Contours detected: 2	Expected: 1

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: germandbls	Contours detected: 3	Expected: 1

- Glyph name: parenleft	Contours detected: 2	Expected: 1

- Glyph name: uni01C5	Contours detected: 3	Expected: 4

- Glyph name: uni090B	Contours detected: 2	Expected: 1

- Glyph name: uni0916	Contours detected: 2	Expected: 1 or 3

- Glyph name: uni091B	Contours detected: 1	Expected: 2

- Glyph name: uni092D	Contours detected: 2	Expected: 1

- Glyph name: uni092E	Contours detected: 3	Expected: 2

- Glyph name: uni093D	Contours detected: 3	Expected: 1

- Glyph name: uni0945	Contours detected: 2	Expected: 1

- Glyph name: uni0955	Contours detected: 3	Expected: 2

- Glyph name: uni0956	Contours detected: 2	Expected: 1

- Glyph name: uni0957	Contours detected: 3	Expected: 2

- Glyph name: uni0959	Contours detected: 3	Expected: 2 or 4

- Glyph name: uni0960	Contours detected: 2	Expected: 1

- Glyph name: uni0962	Contours detected: 2	Expected: 1

- Glyph name: uni0963	Contours detected: 2	Expected: 1

- Glyph name: uni0967	Contours detected: 2	Expected: 1

- Glyph name: uni0970	Contours detected: 1	Expected: 2

- Glyph name: uni097F	Contours detected: 2	Expected: 3

- Glyph name: uni1E0C	Contours detected: 2	Expected: 3

- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

- Glyph name: uogonek	Contours detected: 2	Expected: 1
</code></pre>
 [code: contour-count]



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
    <summary>🔥 <b>FAIL</b> Check family name for GF Guide compliance. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>&quot;Samaano Wide-Bold-Slanted&quot; contains the following characters which are not allowed: &quot;-&quot;.</p>
 [code: forbidden-characters]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking file is named canonically. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Expected &quot;SamaanoWide-Bold-Slanted-Regular.ttf. Got Samaano-Wide-Bold-Slanted.ttf.</p>
 [code: bad-filename]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check glyphs in mark glyph class are non-spacing. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following spacing glyphs may be in the GDEF mark glyph class by mistake:
glyph094D (unencoded), uni0331 (U+0331), uni0930_uni094D.blwf (unencoded), uni0930_uni094D.rphf (unencoded), uni093A (U+093A), uni093C (U+093C), uni0945 (U+0945), uni0946 (U+0946), uni0947 (U+0947), uni0948 (U+0948), uni0955 (U+0955), uni0956 (U+0956), uni0957 (U+0957), uni0962 (U+0962) and uni0963 (U+0963)</p>
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
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gpos.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning information.</p>
 [code: lacks-kern-info]



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







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, tifinagh, coptic, cherokee</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: coptic, glagolitic, gothic, elbasan, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: duployan, malayalam, hebrew, old-permic, todhri, tai-le, coptic, tifinagh, math, syriac, canadian-aboriginal</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: gothic, thai, tifinagh, caucasian-albanian, syriac, sunuwar, cherokee</li>
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
    <summary>⚠️ <b>WARN</b> Combined length of family and style must not exceed 32 characters. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Name ID 6 'SamaanoWide-Bold-Slanted-Regular' exceeds 27 characters. This has been found to cause problems with PostScript printers, especially on Mac platforms.</p>
 [code: nameid6-too-long]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̅ i̇ ỉ ǐ ị̅ ị̇ ị̉ ị̊ ị̋ ị̌ i̦̅ i̦̇ ỉ̦ i̦̊ i̦̋ ǐ̦ i̧̅ i̧̇ ỉ̧ i̧̊</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Nzakara (Latn, 50,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Makaa (Latn, 221,000 speakers), Ejagham (Latn, 120,000 speakers), Igbo (Latn, 27,823,640 speakers), Zapotec (Latn, 490,000 speakers), Aghem (Latn, 38,843 speakers), Yala (Latn, 200,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Sar (Latn, 500,000 speakers), Koonzime (Latn, 40,000 speakers), Mundani (Latn, 34,000 speakers), Dutch (Latn, 31,709,104 speakers), Ngbaka (Latn, 1,020,000 speakers), Ekpeye (Latn, 226,000 speakers), Avokaya (Latn, 100,000 speakers), Mango (Latn, 77,000 speakers), Southern Kisi (Latn, 360,000 speakers), Gulay (Latn, 250,478 speakers), Cicipu (Latn, 44,000 speakers), Basaa (Latn, 332,940 speakers), Dii (Latn, 71,000 speakers), South Central Banda (Latn, 244,000 speakers), Lugbara (Latn, 2,200,000 speakers), Navajo (Latn, 166,319 speakers), Nateni (Latn, 100,000 speakers), Kom (Latn, 360,685 speakers), Belarusian (Cyrl, 10,064,517 speakers), Ma’di (Latn, 584,000 speakers), Ebira (Latn, 2,200,000 speakers), Mfumte (Latn, 79,000 speakers), Bafut (Latn, 158,146 speakers), Vute (Latn, 21,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Fur (Latn, 1,230,163 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Dan (Latn, 1,099,244 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have on-curve points which have potentially incorrect y coordinates:</p>
<pre><code>* N (U+004E): X=1913.0,Y=2.0 (should be at baseline 0?)

* N (U+004E): X=1711.0,Y=2.0 (should be at baseline 0?)

* v (U+0076): X=1129.0,Y=1.0 (should be at baseline 0?)

* v (U+0076): X=922.0,Y=1.0 (should be at baseline 0?)

* Ntilde (U+00D1): X=1913.0,Y=2.0 (should be at baseline 0?)

* Ntilde (U+00D1): X=1711.0,Y=2.0 (should be at baseline 0?)

* Nacute (U+0143): X=1913.0,Y=2.0 (should be at baseline 0?)

* Nacute (U+0143): X=1711.0,Y=2.0 (should be at baseline 0?)

* uni0145 (U+0145): X=1913.0,Y=2.0 (should be at baseline 0?)

* uni0145 (U+0145): X=1711.0,Y=2.0 (should be at baseline 0?)

* Ncaron (U+0147): X=1913.0,Y=2.0 (should be at baseline 0?)

* Ncaron (U+0147): X=1711.0,Y=2.0 (should be at baseline 0?)

* Eng (U+014A): X=675.0,Y=1547.0 (should be at cap-height 1548?)

* Eng (U+014A): X=876.0,Y=1547.0 (should be at cap-height 1548?)

* uni1E44 (U+1E44): X=1913.0,Y=2.0 (should be at baseline 0?)

* uni1E44 (U+1E44): X=1711.0,Y=2.0 (should be at baseline 0?)

* uni1E46 (U+1E46): X=1913.0,Y=2.0 (should be at baseline 0?)

* uni1E46 (U+1E46): X=1711.0,Y=2.0 (should be at baseline 0?)

* uni1E48 (U+1E48): X=1913.0,Y=2.0 (should be at baseline 0?)

* uni1E48 (U+1E48): X=1711.0,Y=2.0 (should be at baseline 0?)

* uni094A_uni0930_uni094D.abvs: X=2505.0,Y=1549.0 (should be at cap-height 1548?)

* uni094A_uni0930_uni094D.abvs: X=2703.0,Y=1549.0 (should be at cap-height 1548?)

* uni095C_uni0930_uni094D.vatu: X=282.0,Y=1.0 (should be at baseline 0?)

* uni095C_uni0930_uni094D.vatu: X=548.0,Y=1.0 (should be at baseline 0?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* G (U+0047): L&lt;&lt;1995.0,202.0&gt;--&lt;1964.0,118.0&gt;&gt; -&gt; L&lt;&lt;1964.0,118.0&gt;--&lt;1928.0,18.0&gt;&gt;

* Gbreve (U+011E): L&lt;&lt;1995.0,202.0&gt;--&lt;1964.0,118.0&gt;&gt; -&gt; L&lt;&lt;1964.0,118.0&gt;--&lt;1928.0,18.0&gt;&gt;

* Gcircumflex (U+011C): L&lt;&lt;1995.0,202.0&gt;--&lt;1964.0,118.0&gt;&gt; -&gt; L&lt;&lt;1964.0,118.0&gt;--&lt;1928.0,18.0&gt;&gt;

* Gdotaccent (U+0120): L&lt;&lt;1995.0,202.0&gt;--&lt;1964.0,118.0&gt;&gt; -&gt; L&lt;&lt;1964.0,118.0&gt;--&lt;1928.0,18.0&gt;&gt;

* S (U+0053): L&lt;&lt;512.0,1028.0&gt;--&lt;661.0,1438.0&gt;&gt; -&gt; L&lt;&lt;661.0,1438.0&gt;--&lt;697.0,1537.0&gt;&gt;

* Sacute (U+015A): L&lt;&lt;512.0,1028.0&gt;--&lt;661.0,1438.0&gt;&gt; -&gt; L&lt;&lt;661.0,1438.0&gt;--&lt;697.0,1537.0&gt;&gt;

* Scaron (U+0160): L&lt;&lt;512.0,1028.0&gt;--&lt;661.0,1438.0&gt;&gt; -&gt; L&lt;&lt;661.0,1438.0&gt;--&lt;697.0,1537.0&gt;&gt;

* Scedilla (U+015E): L&lt;&lt;512.0,1028.0&gt;--&lt;661.0,1438.0&gt;&gt; -&gt; L&lt;&lt;661.0,1438.0&gt;--&lt;697.0,1537.0&gt;&gt;

* Scircumflex (U+015C): L&lt;&lt;512.0,1028.0&gt;--&lt;661.0,1438.0&gt;&gt; -&gt; L&lt;&lt;661.0,1438.0&gt;--&lt;697.0,1537.0&gt;&gt;

* Z (U+005A): L&lt;&lt;185.0,211.0&gt;--&lt;185.0,211.0&gt;&gt; -&gt; L&lt;&lt;185.0,211.0&gt;--&lt;185.0,211.0&gt;&gt;

* Zacute (U+0179): L&lt;&lt;185.0,211.0&gt;--&lt;185.0,211.0&gt;&gt; -&gt; L&lt;&lt;185.0,211.0&gt;--&lt;185.0,211.0&gt;&gt;

* Zcaron (U+017D): L&lt;&lt;185.0,211.0&gt;--&lt;185.0,211.0&gt;&gt; -&gt; L&lt;&lt;185.0,211.0&gt;--&lt;185.0,211.0&gt;&gt;

* Zdotaccent (U+017B): L&lt;&lt;185.0,211.0&gt;--&lt;185.0,211.0&gt;&gt; -&gt; L&lt;&lt;185.0,211.0&gt;--&lt;185.0,211.0&gt;&gt;

* ampersand (U+0026): L&lt;&lt;1842.0,1446.0&gt;--&lt;1653.0,926.0&gt;&gt; -&gt; L&lt;&lt;1653.0,926.0&gt;--&lt;1623.0,843.0&gt;&gt;

* cedilla (U+00B8): L&lt;&lt;1250.0,5.0&gt;--&lt;1127.0,-333.0&gt;&gt; -&gt; L&lt;&lt;1127.0,-333.0&gt;--&lt;1100.0,-406.0&gt;&gt;

* nine (U+0039): L&lt;&lt;333.0,759.0&gt;--&lt;616.0,1537.0&gt;&gt; -&gt; L&lt;&lt;616.0,1537.0&gt;--&lt;623.0,1554.0&gt;&gt;

* six (U+0036): L&lt;&lt;41.0,0.0&gt;--&lt;114.0,201.0&gt;&gt; -&gt; L&lt;&lt;114.0,201.0&gt;--&lt;604.0,1548.0&gt;&gt;

* uni0122 (U+0122): L&lt;&lt;1995.0,202.0&gt;--&lt;1964.0,118.0&gt;&gt; -&gt; L&lt;&lt;1964.0,118.0&gt;--&lt;1928.0,18.0&gt;&gt;

* uni01C4 (U+01C4): L&lt;&lt;973.0,211.0&gt;--&lt;973.0,211.0&gt;&gt; -&gt; L&lt;&lt;973.0,211.0&gt;--&lt;973.0,211.0&gt;&gt;

* uni0218 (U+0218): L&lt;&lt;886.0,1028.0&gt;--&lt;1185.0,1439.0&gt;&gt; -&gt; L&lt;&lt;1185.0,1439.0&gt;--&lt;1257.0,1537.0&gt;&gt;

* uni0907 (U+0907): L&lt;&lt;1703.0,1205.0&gt;--&lt;1694.0,1181.0&gt;&gt; -&gt; L&lt;&lt;1694.0,1181.0&gt;--&lt;1668.0,1110.0&gt;&gt;

* uni0907 (U+0907): L&lt;&lt;419.0,681.0&gt;--&lt;473.0,831.0&gt;&gt; -&gt; L&lt;&lt;473.0,831.0&gt;--&lt;536.0,1004.0&gt;&gt;

* uni0907 (U+0907): L&lt;&lt;536.0,1004.0&gt;--&lt;593.0,1160.0&gt;&gt; -&gt; L&lt;&lt;593.0,1160.0&gt;--&lt;601.0,1181.0&gt;&gt;

* uni0908 (U+0908): L&lt;&lt;419.0,681.0&gt;--&lt;473.0,831.0&gt;&gt; -&gt; L&lt;&lt;473.0,831.0&gt;--&lt;536.0,1004.0&gt;&gt;

* uni0908 (U+0908): L&lt;&lt;536.0,1004.0&gt;--&lt;593.0,1160.0&gt;&gt; -&gt; L&lt;&lt;593.0,1160.0&gt;--&lt;601.0,1181.0&gt;&gt;

* uni090C (U+090C): L&lt;&lt;265.0,590.0&gt;--&lt;309.0,713.0&gt;&gt; -&gt; L&lt;&lt;309.0,713.0&gt;--&lt;333.0,777.0&gt;&gt;

* uni090D (U+090D): L&lt;&lt;1254.0,358.0&gt;--&lt;1242.0,325.0&gt;&gt; -&gt; L&lt;&lt;1242.0,325.0&gt;--&lt;1232.0,297.0&gt;&gt;

* uni090E (U+090E): L&lt;&lt;2647.0,1858.0&gt;--&lt;2614.0,1765.0&gt;&gt; -&gt; L&lt;&lt;2614.0,1765.0&gt;--&lt;2578.0,1667.0&gt;&gt;

* uni0915_uni094D_uni0937.akhn: L&lt;&lt;2337.0,1078.0&gt;--&lt;2299.0,972.0&gt;&gt; -&gt; L&lt;&lt;2299.0,972.0&gt;--&lt;1945.0,0.0&gt;&gt;

* uni0919 (U+0919): L&lt;&lt;114.0,0.0&gt;--&lt;161.0,130.0&gt;&gt; -&gt; L&lt;&lt;161.0,130.0&gt;--&lt;268.0,423.0&gt;&gt;

* uni0919 (U+0919): L&lt;&lt;453.0,620.0&gt;--&lt;499.0,747.0&gt;&gt; -&gt; L&lt;&lt;499.0,747.0&gt;--&lt;621.0,1083.0&gt;&gt;

* uni0919_uni0930_uni094D.vatu: L&lt;&lt;226.0,308.0&gt;--&lt;275.0,443.0&gt;&gt; -&gt; L&lt;&lt;275.0,443.0&gt;--&lt;296.0,501.0&gt;&gt;

* uni0919_uni0930_uni094D.vatu: L&lt;&lt;529.0,829.0&gt;--&lt;598.0,1020.0&gt;&gt; -&gt; L&lt;&lt;598.0,1020.0&gt;--&lt;599.0,1023.0&gt;&gt;

* uni0919_uni094D.half: L&lt;&lt;153.0,108.0&gt;--&lt;202.0,243.0&gt;&gt; -&gt; L&lt;&lt;202.0,243.0&gt;--&lt;224.0,301.0&gt;&gt;

* uni0919_uni094D.haln: L&lt;&lt;114.0,0.0&gt;--&lt;209.0,130.0&gt;&gt; -&gt; L&lt;&lt;209.0,130.0&gt;--&lt;422.0,423.0&gt;&gt;

* uni091B (U+091B): L&lt;&lt;1816.0,808.0&gt;--&lt;1560.0,104.0&gt;&gt; -&gt; L&lt;&lt;1560.0,104.0&gt;--&lt;1522.0,0.0&gt;&gt;

* uni091B_uni0930_uni094D.vatu: L&lt;&lt;1851.0,905.0&gt;--&lt;1639.0,321.0&gt;&gt; -&gt; L&lt;&lt;1639.0,321.0&gt;--&lt;1620.0,270.0&gt;&gt;

* uni091B_uni094D.haln: L&lt;&lt;2110.0,808.0&gt;--&lt;1610.0,121.0&gt;&gt; -&gt; L&lt;&lt;1610.0,121.0&gt;--&lt;1522.0,0.0&gt;&gt;

* uni091E (U+091E): L&lt;&lt;1293.0,460.0&gt;--&lt;1258.0,364.0&gt;&gt; -&gt; L&lt;&lt;1258.0,364.0&gt;--&lt;1241.0,316.0&gt;&gt;

* uni091E_uni094D.half: L&lt;&lt;1553.0,460.0&gt;--&lt;1518.0,364.0&gt;&gt; -&gt; L&lt;&lt;1518.0,364.0&gt;--&lt;1501.0,316.0&gt;&gt;

* uni091F_uni0930_uni094D.vatu: L&lt;&lt;196.0,305.0&gt;--&lt;236.0,414.0&gt;&gt; -&gt; L&lt;&lt;236.0,414.0&gt;--&lt;267.0,501.0&gt;&gt;

* uni0921 (U+0921): L&lt;&lt;616.0,638.0&gt;--&lt;635.0,690.0&gt;&gt; -&gt; L&lt;&lt;635.0,690.0&gt;--&lt;656.0,746.0&gt;&gt;

* uni0921_uni0930_uni094D.vatu: L&lt;&lt;1886.0,837.0&gt;--&lt;1870.0,794.0&gt;&gt; -&gt; L&lt;&lt;1870.0,794.0&gt;--&lt;1642.0,164.0&gt;&gt;

* uni0922_uni0930_uni094D.vatu: L&lt;&lt;210.0,305.0&gt;--&lt;254.0,425.0&gt;&gt; -&gt; L&lt;&lt;254.0,425.0&gt;--&lt;281.0,501.0&gt;&gt;

* uni0925 (U+0925): L&lt;&lt;316.0,810.0&gt;--&lt;339.0,873.0&gt;&gt; -&gt; L&lt;&lt;339.0,873.0&gt;--&lt;365.0,946.0&gt;&gt;

* uni0925_uni0930_uni094D.vatu: L&lt;&lt;316.0,810.0&gt;--&lt;338.0,870.0&gt;&gt; -&gt; L&lt;&lt;338.0,870.0&gt;--&lt;365.0,946.0&gt;&gt;

* uni0925_uni094D.half: L&lt;&lt;316.0,810.0&gt;--&lt;339.0,873.0&gt;&gt; -&gt; L&lt;&lt;339.0,873.0&gt;--&lt;365.0,946.0&gt;&gt;

* uni0925_uni094D.haln: L&lt;&lt;611.0,810.0&gt;--&lt;656.0,873.0&gt;&gt; -&gt; L&lt;&lt;656.0,873.0&gt;--&lt;710.0,946.0&gt;&gt;

* uni092A_uni094D.haln: L&lt;&lt;710.0,825.0&gt;--&lt;725.0,846.0&gt;&gt; -&gt; L&lt;&lt;725.0,846.0&gt;--&lt;1091.0,1349.0&gt;&gt;

* uni092B_uni094D.haln: L&lt;&lt;709.0,824.0&gt;--&lt;784.0,927.0&gt;&gt; -&gt; L&lt;&lt;784.0,927.0&gt;--&lt;1091.0,1349.0&gt;&gt;

* uni0932_uni094D.haln: L&lt;&lt;462.0,582.0&gt;--&lt;514.0,654.0&gt;&gt; -&gt; L&lt;&lt;514.0,654.0&gt;--&lt;550.0,703.0&gt;&gt;

* uni0933_uni094D.haln: L&lt;&lt;462.0,582.0&gt;--&lt;514.0,654.0&gt;&gt; -&gt; L&lt;&lt;514.0,654.0&gt;--&lt;550.0,703.0&gt;&gt;

* uni0934_uni094D.haln: L&lt;&lt;467.0,582.0&gt;--&lt;519.0,654.0&gt;&gt; -&gt; L&lt;&lt;519.0,654.0&gt;--&lt;555.0,703.0&gt;&gt;

* uni0936_uni094D.haln: L&lt;&lt;941.0,1224.0&gt;--&lt;1118.0,1467.0&gt;&gt; -&gt; L&lt;&lt;1118.0,1467.0&gt;--&lt;1177.0,1548.0&gt;&gt;

* uni0937 (U+0937): L&lt;&lt;2273.0,981.0&gt;--&lt;2273.0,981.0&gt;&gt; -&gt; L&lt;&lt;2273.0,981.0&gt;--&lt;2273.0,981.0&gt;&gt;

* uni0937 (U+0937): L&lt;&lt;394.0,824.0&gt;--&lt;455.0,992.0&gt;&gt; -&gt; L&lt;&lt;455.0,992.0&gt;--&lt;585.0,1350.0&gt;&gt;

* uni0937_uni0930_uni094D.vatu: L&lt;&lt;2273.0,981.0&gt;--&lt;2273.0,981.0&gt;&gt; -&gt; L&lt;&lt;2273.0,981.0&gt;--&lt;2273.0,981.0&gt;&gt;

* uni0937_uni0930_uni094D.vatu: L&lt;&lt;394.0,824.0&gt;--&lt;455.0,992.0&gt;&gt; -&gt; L&lt;&lt;455.0,992.0&gt;--&lt;585.0,1350.0&gt;&gt;

* uni0937_uni094D.half: L&lt;&lt;594.0,824.0&gt;--&lt;655.0,992.0&gt;&gt; -&gt; L&lt;&lt;655.0,992.0&gt;--&lt;785.0,1350.0&gt;&gt;

* uni0937_uni094D.haln: L&lt;&lt;2630.0,981.0&gt;--&lt;2630.0,981.0&gt;&gt; -&gt; L&lt;&lt;2630.0,981.0&gt;--&lt;2630.0,981.0&gt;&gt;

* uni0937_uni094D.haln: L&lt;&lt;694.0,824.0&gt;--&lt;816.0,992.0&gt;&gt; -&gt; L&lt;&lt;816.0,992.0&gt;--&lt;1077.0,1350.0&gt;&gt;

* uni0938 (U+0938): L&lt;&lt;419.0,729.0&gt;--&lt;450.0,814.0&gt;&gt; -&gt; L&lt;&lt;450.0,814.0&gt;--&lt;466.0,858.0&gt;&gt;

* uni0938_uni0930_uni094D.vatu: L&lt;&lt;423.0,729.0&gt;--&lt;454.0,814.0&gt;&gt; -&gt; L&lt;&lt;454.0,814.0&gt;--&lt;470.0,858.0&gt;&gt;

* uni0938_uni094D.half: L&lt;&lt;619.0,729.0&gt;--&lt;650.0,814.0&gt;&gt; -&gt; L&lt;&lt;650.0,814.0&gt;--&lt;666.0,858.0&gt;&gt;

* uni0938_uni094D.haln: L&lt;&lt;685.0,729.0&gt;--&lt;764.0,838.0&gt;&gt; -&gt; L&lt;&lt;764.0,838.0&gt;--&lt;779.0,858.0&gt;&gt;

* uni0939 (U+0939): L&lt;&lt;1689.0,789.0&gt;--&lt;1656.0,698.0&gt;&gt; -&gt; L&lt;&lt;1656.0,698.0&gt;--&lt;1636.0,643.0&gt;&gt;

* uni0939_uni0930_uni094D.vatu: L&lt;&lt;1989.0,789.0&gt;--&lt;1946.0,671.0&gt;&gt; -&gt; L&lt;&lt;1946.0,671.0&gt;--&lt;1936.0,643.0&gt;&gt;

* uni0940_uni0930_uni094D.abvs: L&lt;&lt;2763.0,1869.0&gt;--&lt;2764.0,1870.0&gt;&gt; -&gt; L&lt;&lt;2764.0,1870.0&gt;--&lt;2765.0,1871.0&gt;&gt;

* uni0943 (U+0943): L&lt;&lt;-834.0,-611.0&gt;--&lt;-835.0,-495.0&gt;&gt; -&gt; L&lt;&lt;-835.0,-495.0&gt;--&lt;-836.0,-455.0&gt;&gt;

* uni0943 (U+0943): L&lt;&lt;-836.0,-455.0&gt;--&lt;-837.0,-270.0&gt;&gt; -&gt; L&lt;&lt;-837.0,-270.0&gt;--&lt;-838.0,-133.0&gt;&gt;

* uni0943 (U+0943): L&lt;&lt;-838.0,-132.0&gt;--&lt;-775.0,-122.0&gt;&gt; -&gt; L&lt;&lt;-775.0,-122.0&gt;--&lt;-5.0,9.0&gt;&gt;

* uni0945_uni0930_uni094D.abvs: L&lt;&lt;1888.0,1869.0&gt;--&lt;1889.0,1870.0&gt;&gt; -&gt; L&lt;&lt;1889.0,1870.0&gt;--&lt;1890.0,1871.0&gt;&gt;

* uni0946 (U+0946): L&lt;&lt;874.0,1858.0&gt;--&lt;870.0,1846.0&gt;&gt; -&gt; L&lt;&lt;870.0,1846.0&gt;--&lt;840.0,1763.0&gt;&gt;

* uni0946_uni0902.abvs: L&lt;&lt;1551.0,1858.0&gt;--&lt;1521.0,1817.0&gt;&gt; -&gt; L&lt;&lt;1521.0,1817.0&gt;--&lt;1481.0,1763.0&gt;&gt;

* uni0946_uni0930_uni094D.abvs: L&lt;&lt;1551.0,1858.0&gt;--&lt;1521.0,1817.0&gt;&gt; -&gt; L&lt;&lt;1521.0,1817.0&gt;--&lt;1481.0,1763.0&gt;&gt;

* uni0946_uni0930_uni094D.abvs: L&lt;&lt;1809.0,1861.0&gt;--&lt;1810.0,1862.0&gt;&gt; -&gt; L&lt;&lt;1810.0,1862.0&gt;--&lt;1811.0,1863.0&gt;&gt;

* uni0947_uni0930_uni094D.abvs: L&lt;&lt;1785.0,1861.0&gt;--&lt;1786.0,1862.0&gt;&gt; -&gt; L&lt;&lt;1786.0,1862.0&gt;--&lt;1787.0,1863.0&gt;&gt;

* uni0949_uni0930_uni094D.abvs: L&lt;&lt;3315.0,1875.0&gt;--&lt;3316.0,1876.0&gt;&gt; -&gt; L&lt;&lt;3316.0,1876.0&gt;--&lt;3317.0,1877.0&gt;&gt;

* uni094B_uni0930_uni094D.abvs: L&lt;&lt;2511.0,1880.0&gt;--&lt;2512.0,1881.0&gt;&gt; -&gt; L&lt;&lt;2512.0,1881.0&gt;--&lt;2513.0,1882.0&gt;&gt;

* uni094F (U+094F): L&lt;&lt;1109.0,1866.0&gt;--&lt;1048.0,1697.0&gt;&gt; -&gt; L&lt;&lt;1048.0,1697.0&gt;--&lt;996.0,1555.0&gt;&gt;

* uni095C (U+095C): L&lt;&lt;616.0,638.0&gt;--&lt;635.0,690.0&gt;&gt; -&gt; L&lt;&lt;635.0,690.0&gt;--&lt;656.0,746.0&gt;&gt;

* uni095C_uni0930_uni094D.vatu: L&lt;&lt;1886.0,837.0&gt;--&lt;1870.0,794.0&gt;&gt; -&gt; L&lt;&lt;1870.0,794.0&gt;--&lt;1642.0,164.0&gt;&gt;

* uni095D_uni0930_uni094D.vatu: L&lt;&lt;210.0,305.0&gt;--&lt;254.0,425.0&gt;&gt; -&gt; L&lt;&lt;254.0,425.0&gt;--&lt;281.0,501.0&gt;&gt;

* uni095E_uni094D.haln: L&lt;&lt;724.0,824.0&gt;--&lt;799.0,927.0&gt;&gt; -&gt; L&lt;&lt;799.0,927.0&gt;--&lt;1106.0,1349.0&gt;&gt;

* uni0961 (U+0961): L&lt;&lt;257.0,590.0&gt;--&lt;301.0,713.0&gt;&gt; -&gt; L&lt;&lt;301.0,713.0&gt;--&lt;325.0,777.0&gt;&gt;

* uni096A (U+096A): L&lt;&lt;193.0,95.0&gt;--&lt;201.0,118.0&gt;&gt; -&gt; L&lt;&lt;201.0,118.0&gt;--&lt;242.0,230.0&gt;&gt;

* uni096A (U+096A): L&lt;&lt;2056.0,317.0&gt;--&lt;1984.0,118.0&gt;&gt; -&gt; L&lt;&lt;1984.0,118.0&gt;--&lt;1951.0,28.0&gt;&gt;

* uni1E62 (U+1E62): L&lt;&lt;886.0,1028.0&gt;--&lt;1185.0,1439.0&gt;&gt; -&gt; L&lt;&lt;1185.0,1439.0&gt;--&lt;1257.0,1537.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* uni01C4 (U+01C4): L&lt;&lt;935.0,875.0&gt;--&lt;824.0,1350.0&gt;&gt;/L&lt;&lt;824.0,1350.0&gt;--&lt;824.0,1349.0&gt;&gt; = 13.153086583164342

* uni01C5 (U+01C5): L&lt;&lt;1008.0,767.0&gt;--&lt;1007.0,772.0&gt;&gt;/L&lt;&lt;1007.0,772.0&gt;--&lt;1007.0,769.0&gt;&gt; = 11.309932474020227

* uni0915_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1213.0,289.0&gt;&gt; = 13.978169517093123

* uni0916_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1722.0,370.0&gt;&gt; = 12.49247557736108

* uni0916_uni0930_uni094D.vatu: L&lt;&lt;52.0,0.0&gt;--&lt;1722.0,370.0&gt;&gt;/L&lt;&lt;1722.0,370.0&gt;--&lt;452.0,370.0&gt;&gt; = 12.49247557736108

* uni0917_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1863.0,401.0&gt;&gt; = 12.485252069704043

* uni0918_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1873.0,403.0&gt;&gt; = 12.478825942667704

* uni091A_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1803.0,388.0&gt;&gt; = 12.494156501091224

* uni091B_uni0930_uni094D.vatu: L&lt;&lt;960.0,0.0&gt;--&lt;536.0,0.0&gt;&gt;/L&lt;&lt;536.0,0.0&gt;--&lt;1399.0,215.0&gt;&gt; = 13.989369374610066

* uni091C_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1865.0,402.0&gt;&gt; = 12.50203554615018

* uni091E_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1905.0,411.0&gt;&gt; = 12.50588808887614

* uni0923_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1888.0,407.0&gt;&gt; = 12.499065987539916

* uni0924_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1521.0,325.0&gt;&gt; = 12.475109712208948

* uni0925_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1550.0,332.0&gt;&gt; = 12.496405179302853

* uni0925_uni0930_uni094D.vatu: L&lt;&lt;52.0,0.0&gt;--&lt;1550.0,332.0&gt;&gt;/L&lt;&lt;1550.0,332.0&gt;--&lt;142.0,332.0&gt;&gt; = 12.496405179302853

* uni0926_uni094D.half: L&lt;&lt;1617.0,178.0&gt;--&lt;1616.0,177.0&gt;&gt;/L&lt;&lt;1616.0,177.0&gt;--&lt;1619.0,179.0&gt;&gt; = 11.309932474020227

* uni0927_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1523.0,326.0&gt;&gt; = 12.495810359397797

* uni0927_uni0930_uni094D.vatu: L&lt;&lt;52.0,0.0&gt;--&lt;1523.0,326.0&gt;&gt;/L&lt;&lt;1523.0,326.0&gt;--&lt;209.0,326.0&gt;&gt; = 12.495810359397797

* uni0928_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1877.0,404.0&gt;&gt; = 12.482260924684706

* uni0929_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1874.0,404.0&gt;&gt; = 12.502167804288424

* uni092A_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1870.0,403.0&gt;&gt; = 12.498771480797592

* uni092C_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1827.0,393.0&gt;&gt; = 12.484368535813914

* uni092D_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1901.0,410.0&gt;&gt; = 12.502556852726771

* uni092E_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1921.0,414.0&gt;&gt; = 12.489850870338772

* uni092F_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1310.0,279.0&gt;&gt; = 12.504693325258396

* uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1929.0,416.0&gt;&gt; = 12.496482872235207

* uni0932_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1875.0,404.0&gt;&gt; = 12.495525238591755

* uni0935_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1827.0,393.0&gt;&gt; = 12.484368535813914

* uni0936_uni0930_uni094D.vatu: L&lt;&lt;2036.0,658.0&gt;--&lt;1363.0,922.0&gt;&gt;/L&lt;&lt;1363.0,922.0&gt;--&lt;1510.0,861.0&gt;&gt; = 1.1180310216747913

* uni0937_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1862.0,401.0&gt;&gt; = 12.491933528971943

* uni0948 (U+0948): L&lt;&lt;541.0,1548.0&gt;--&lt;631.0,1548.0&gt;&gt;/L&lt;&lt;631.0,1548.0&gt;--&lt;-175.0,1750.0&gt;&gt; = 14.069691087894096

* uni0959_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1722.0,370.0&gt;&gt; = 12.49247557736108

* uni0959_uni0930_uni094D.vatu: L&lt;&lt;52.0,0.0&gt;--&lt;1722.0,370.0&gt;&gt;/L&lt;&lt;1722.0,370.0&gt;--&lt;452.0,370.0&gt;&gt; = 12.49247557736108

* uni095A_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1863.0,401.0&gt;&gt; = 12.485252069704043

* uni095B_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1865.0,402.0&gt;&gt; = 12.50203554615018

* uni095F_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;52.0,0.0&gt;&gt;/L&lt;&lt;52.0,0.0&gt;--&lt;1310.0,279.0&gt;&gt; = 12.504693325258396
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* questiondown (U+00BF): L&lt;&lt;1631.0,1273.0&gt;--&lt;1381.0,1272.0&gt;&gt;

* uni093D (U+093D): L&lt;&lt;1451.0,1079.0&gt;--&lt;1449.0,269.0&gt;&gt;

* uni0943 (U+0943): L&lt;&lt;-5.0,9.0&gt;--&lt;-4.0,-178.0&gt;&gt;

* uni0943 (U+0943): L&lt;&lt;-637.0,-286.0&gt;--&lt;-636.0,-418.0&gt;&gt;

* uni0943 (U+0943): L&lt;&lt;-834.0,-611.0&gt;--&lt;-835.0,-495.0&gt;&gt;

* uni0943 (U+0943): L&lt;&lt;-836.0,-455.0&gt;--&lt;-837.0,-270.0&gt;&gt;

* uni0943 (U+0943): L&lt;&lt;-837.0,-270.0&gt;--&lt;-838.0,-133.0&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



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

<details><summary>[20] Samaano-Wide-Thin-Slanted.ttf</summary>
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
<td align="left">U+0189: LATIN CAPITAL LETTER AFRICAN D</td>
<td align="left">U+0256: LATIN SMALL LETTER D WITH TAIL</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



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
    <summary>🔥 <b>FAIL</b> Check family name for GF Guide compliance. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>&quot;Samaano Wide-Thin-Slanted&quot; contains the following characters which are not allowed: &quot;-&quot;.</p>
 [code: forbidden-characters]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking file is named canonically. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Expected &quot;SamaanoWide-Thin-Slanted-Regular.ttf. Got Samaano-Wide-Thin-Slanted.ttf.</p>
 [code: bad-filename]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 434 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



* ⚠️ **WARN** <p>Font is monospaced but 2 glyphs (0.28%) have a different width. You should check the widths of: ['Eng', 'eng']</p>
 [code: mono-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check glyphs in mark glyph class are non-spacing. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following spacing glyphs may be in the GDEF mark glyph class by mistake:
glyph094D (unencoded), uni0331 (U+0331), uni0930_uni094D.blwf (unencoded), uni0930_uni094D.rphf (unencoded), uni093A (U+093A), uni093C (U+093C), uni0945 (U+0945), uni0946 (U+0946), uni0947 (U+0947), uni0948 (U+0948), uni0951 (U+0951), uni0952 (U+0952), uni0953 (U+0953), uni0954 (U+0954), uni0955 (U+0955), uni0956 (U+0956), uni0957 (U+0957), uni0962 (U+0962) and uni0963 (U+0963)</p>
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
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gpos.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning information.</p>
 [code: lacks-kern-info]



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
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: A	Contours detected: 1	Expected: 2

- Glyph name: g	Contours detected: 1	Expected: 2 or 3

- Glyph name: braceleft	Contours detected: 3	Expected: 1

- Glyph name: Agrave	Contours detected: 2	Expected: 3

- Glyph name: Aacute	Contours detected: 2	Expected: 3

- Glyph name: Acircumflex	Contours detected: 2	Expected: 3

- Glyph name: Atilde	Contours detected: 2	Expected: 3

- Glyph name: Adieresis	Contours detected: 3	Expected: 4

- Glyph name: Icircumflex	Contours detected: 1	Expected: 2

- Glyph name: Amacron	Contours detected: 2	Expected: 3

- Glyph name: Abreve	Contours detected: 2	Expected: 3

- Glyph name: Aogonek	Contours detected: 1	Expected: 2 or 3

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: gcircumflex	Contours detected: 2	Expected: 3 or 4

- Glyph name: gbreve	Contours detected: 2	Expected: 3 or 4

- Glyph name: gdotaccent	Contours detected: 2	Expected: 3 or 4

- Glyph name: uni0123	Contours detected: 2	Expected: 3 or 4

- Glyph name: Jcircumflex	Contours detected: 1	Expected: 2

- Glyph name: uni091B	Contours detected: 1	Expected: 2

- Glyph name: uni092D	Contours detected: 2	Expected: 1

- Glyph name: uni092E	Contours detected: 3	Expected: 2

- Glyph name: uni093D	Contours detected: 2	Expected: 1

- Glyph name: uni0945	Contours detected: 2	Expected: 1

- Glyph name: uni0955	Contours detected: 3	Expected: 2

- Glyph name: uni0956	Contours detected: 2	Expected: 1

- Glyph name: uni0957	Contours detected: 3	Expected: 2

- Glyph name: uni0962	Contours detected: 2	Expected: 1

- Glyph name: uni0963	Contours detected: 2	Expected: 1

- Glyph name: uni0967	Contours detected: 2	Expected: 1

- Glyph name: uni0970	Contours detected: 1	Expected: 2

- Glyph name: uni097F	Contours detected: 2	Expected: 3

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

- Glyph name: A	Contours detected: 1	Expected: 2

- Glyph name: Aacute	Contours detected: 2	Expected: 3

- Glyph name: Abreve	Contours detected: 2	Expected: 3

- Glyph name: Acircumflex	Contours detected: 2	Expected: 3

- Glyph name: Adieresis	Contours detected: 3	Expected: 4

- Glyph name: Agrave	Contours detected: 2	Expected: 3

- Glyph name: Amacron	Contours detected: 2	Expected: 3

- Glyph name: Aogonek	Contours detected: 1	Expected: 2 or 3

- Glyph name: Atilde	Contours detected: 2	Expected: 3

- Glyph name: Icircumflex	Contours detected: 1	Expected: 2

- Glyph name: Jcircumflex	Contours detected: 1	Expected: 2

- Glyph name: braceleft	Contours detected: 3	Expected: 1

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: g	Contours detected: 1	Expected: 2 or 3

- Glyph name: gbreve	Contours detected: 2	Expected: 3 or 4

- Glyph name: gcircumflex	Contours detected: 2	Expected: 3 or 4

- Glyph name: gdotaccent	Contours detected: 2	Expected: 3 or 4

- Glyph name: uni0123	Contours detected: 2	Expected: 3 or 4

- Glyph name: uni091B	Contours detected: 1	Expected: 2

- Glyph name: uni092D	Contours detected: 2	Expected: 1

- Glyph name: uni092E	Contours detected: 3	Expected: 2

- Glyph name: uni093D	Contours detected: 2	Expected: 1

- Glyph name: uni0945	Contours detected: 2	Expected: 1

- Glyph name: uni0955	Contours detected: 3	Expected: 2

- Glyph name: uni0956	Contours detected: 2	Expected: 1

- Glyph name: uni0957	Contours detected: 3	Expected: 2

- Glyph name: uni0962	Contours detected: 2	Expected: 1

- Glyph name: uni0963	Contours detected: 2	Expected: 1

- Glyph name: uni0967	Contours detected: 2	Expected: 1

- Glyph name: uni0970	Contours detected: 1	Expected: 2

- Glyph name: uni097F	Contours detected: 2	Expected: 3

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12
</code></pre>
 [code: contour-count]



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







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, tifinagh, coptic, cherokee</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: coptic, glagolitic, gothic, elbasan, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: duployan, malayalam, hebrew, old-permic, todhri, tai-le, coptic, tifinagh, math, syriac, canadian-aboriginal</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: gothic, thai, tifinagh, caucasian-albanian, syriac, sunuwar, cherokee</li>
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
    <summary>⚠️ <b>WARN</b> Combined length of family and style must not exceed 32 characters. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Name ID 6 'SamaanoWide-Thin-Slanted-Regular' exceeds 27 characters. This has been found to cause problems with PostScript printers, especially on Mac platforms.</p>
 [code: nameid6-too-long]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: i̊ i̋ j̀ j́ j̃ j̄ j̈ į̀ į́ į̂ į̃ į̄ į̌</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̅ i̇ ỉ ǐ ị̅ ị̇ ị̉ ị̊ ị̋ ị̌ i̦̅ i̦̇ ỉ̦ i̦̊ i̦̋ ǐ̦ i̧̅ i̧̇ ỉ̧ i̧̊</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Nzakara (Latn, 50,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Makaa (Latn, 221,000 speakers), Ejagham (Latn, 120,000 speakers), Igbo (Latn, 27,823,640 speakers), Zapotec (Latn, 490,000 speakers), Aghem (Latn, 38,843 speakers), Yala (Latn, 200,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Sar (Latn, 500,000 speakers), Koonzime (Latn, 40,000 speakers), Mundani (Latn, 34,000 speakers), Dutch (Latn, 31,709,104 speakers), Ngbaka (Latn, 1,020,000 speakers), Ekpeye (Latn, 226,000 speakers), Avokaya (Latn, 100,000 speakers), Mango (Latn, 77,000 speakers), Southern Kisi (Latn, 360,000 speakers), Gulay (Latn, 250,478 speakers), Cicipu (Latn, 44,000 speakers), Basaa (Latn, 332,940 speakers), Dii (Latn, 71,000 speakers), South Central Banda (Latn, 244,000 speakers), Lugbara (Latn, 2,200,000 speakers), Navajo (Latn, 166,319 speakers), Nateni (Latn, 100,000 speakers), Kom (Latn, 360,685 speakers), Belarusian (Cyrl, 10,064,517 speakers), Ma’di (Latn, 584,000 speakers), Ebira (Latn, 2,200,000 speakers), Mfumte (Latn, 79,000 speakers), Bafut (Latn, 158,146 speakers), Vute (Latn, 21,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Fur (Latn, 1,230,163 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Dan (Latn, 1,099,244 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* B (U+0042): L&lt;&lt;1413.0,907.0&gt;--&lt;1407.0,890.0&gt;&gt;/L&lt;&lt;1407.0,890.0&gt;--&lt;1413.0,908.0&gt;&gt; = 1.0050860052537793

* Dcroat (U+0110): L&lt;&lt;2362.0,1020.0&gt;--&lt;2364.0,1023.0&gt;&gt;/L&lt;&lt;2364.0,1023.0&gt;--&lt;2325.0,915.0&gt;&gt; = 13.834853156658712

* uni01C5 (U+01C5): L&lt;&lt;966.0,1020.0&gt;--&lt;967.0,1023.0&gt;&gt;/L&lt;&lt;967.0,1023.0&gt;--&lt;956.0,960.0&gt;&gt; = 8.530765609948096

* uni0913 (U+0913): L&lt;&lt;2546.0,1550.0&gt;--&lt;2542.0,1549.0&gt;&gt;/L&lt;&lt;2542.0,1549.0&gt;--&lt;2612.0,1549.0&gt;&gt; = 14.036243467926484

* uni0916_uni0930_uni094D.vatu: L&lt;&lt;190.0,0.0&gt;--&lt;1814.0,370.0&gt;&gt;/L&lt;&lt;1814.0,370.0&gt;--&lt;592.0,370.0&gt;&gt; = 12.834760383293624

* uni0916_uni0930_uni094D.vatu: L&lt;&lt;447.0,0.0&gt;--&lt;190.0,0.0&gt;&gt;/L&lt;&lt;190.0,0.0&gt;--&lt;1814.0,370.0&gt;&gt; = 12.834760383293624

* uni0917_uni0930_uni094D.vatu: L&lt;&lt;453.0,0.0&gt;--&lt;196.0,0.0&gt;&gt;/L&lt;&lt;196.0,0.0&gt;--&lt;1995.0,410.0&gt;&gt; = 12.838675460780657

* uni0918_uni0930_uni094D.vatu: L&lt;&lt;201.0,-49.0&gt;--&lt;1847.0,326.0&gt;&gt;/L&lt;&lt;1847.0,326.0&gt;--&lt;299.0,326.0&gt;&gt; = 12.83435285303413

* uni0918_uni0930_uni094D.vatu: L&lt;&lt;458.0,-49.0&gt;--&lt;201.0,-49.0&gt;&gt;/L&lt;&lt;201.0,-49.0&gt;--&lt;1847.0,326.0&gt;&gt; = 12.83435285303413

* uni091A_uni0930_uni094D.vatu: L&lt;&lt;383.0,0.0&gt;--&lt;126.0,0.0&gt;&gt;/L&lt;&lt;126.0,0.0&gt;--&lt;1951.0,416.0&gt;&gt; = 12.840898455437413

* uni091B_uni0930_uni094D.vatu: L&lt;&lt;383.0,0.0&gt;--&lt;126.0,0.0&gt;&gt;/L&lt;&lt;126.0,0.0&gt;--&lt;1603.0,333.0&gt;&gt; = 12.705303928524263

* uni091C_uni0930_uni094D.vatu: L&lt;&lt;448.0,0.0&gt;--&lt;191.0,0.0&gt;&gt;/L&lt;&lt;191.0,0.0&gt;--&lt;2008.0,414.0&gt;&gt; = 12.835609486401424

* uni091E_uni0930_uni094D.vatu: L&lt;&lt;505.0,0.0&gt;--&lt;248.0,0.0&gt;&gt;/L&lt;&lt;248.0,0.0&gt;--&lt;2048.0,410.0&gt;&gt; = 12.831779042530089

* uni0923_uni0930_uni094D.vatu: L&lt;&lt;481.0,0.0&gt;--&lt;224.0,0.0&gt;&gt;/L&lt;&lt;224.0,0.0&gt;--&lt;2033.0,412.0&gt;&gt; = 12.830273512751555

* uni0925_uni0930_uni094D.vatu: L&lt;&lt;523.0,0.0&gt;--&lt;266.0,0.0&gt;&gt;/L&lt;&lt;266.0,0.0&gt;--&lt;2073.0,412.0&gt;&gt; = 12.844003410182452

* uni0926_uni0930_uni094D.vatu: L&lt;&lt;383.0,0.0&gt;--&lt;126.0,0.0&gt;&gt;/L&lt;&lt;126.0,0.0&gt;--&lt;1358.0,264.0&gt;&gt; = 12.094757077012089

* uni0927_uni0930_uni094D.vatu: L&lt;&lt;476.0,0.0&gt;--&lt;219.0,0.0&gt;&gt;/L&lt;&lt;219.0,0.0&gt;--&lt;2030.0,413.0&gt;&gt; = 12.84664964895844

* uni0928_uni0930_uni094D.vatu: L&lt;&lt;470.0,0.0&gt;--&lt;213.0,0.0&gt;&gt;/L&lt;&lt;213.0,0.0&gt;--&lt;2018.0,411.0&gt;&gt; = 12.827587702972119

* uni0929_uni0930_uni094D.vatu: L&lt;&lt;456.0,0.0&gt;--&lt;199.0,0.0&gt;&gt;/L&lt;&lt;199.0,0.0&gt;--&lt;2016.0,414.0&gt;&gt; = 12.835609486401424

* uni092A_uni0930_uni094D.vatu: L&lt;&lt;446.0,0.0&gt;--&lt;189.0,0.0&gt;&gt;/L&lt;&lt;189.0,0.0&gt;--&lt;2001.0,413.0&gt;&gt; = 12.839794937341944

* uni092B_uni0930_uni094D.vatu: L&lt;&lt;383.0,0.0&gt;--&lt;126.0,0.0&gt;&gt;/L&lt;&lt;126.0,0.0&gt;--&lt;1573.0,334.0&gt;&gt; = 12.997508619477422

* uni092C_uni0930_uni094D.vatu: L&lt;&lt;406.0,0.0&gt;--&lt;149.0,0.0&gt;&gt;/L&lt;&lt;149.0,0.0&gt;--&lt;1974.0,416.0&gt;&gt; = 12.840898455437413

* uni092D_uni0930_uni094D.vatu: L&lt;&lt;495.0,0.0&gt;--&lt;238.0,0.0&gt;&gt;/L&lt;&lt;238.0,0.0&gt;--&lt;2042.0,411.0&gt;&gt; = 12.834462913442819

* uni092E_uni0930_uni094D.vatu: L&lt;&lt;507.0,0.0&gt;--&lt;250.0,0.0&gt;&gt;/L&lt;&lt;250.0,0.0&gt;--&lt;2060.0,413.0&gt;&gt; = 12.85351156020271

* uni092F_uni0930_uni094D.vatu: L&lt;&lt;383.0,0.0&gt;--&lt;126.0,0.0&gt;&gt;/L&lt;&lt;126.0,0.0&gt;--&lt;1980.0,323.0&gt;&gt; = 9.882760671675692

* uni0930_uni0930_uni094D.vatu: L&lt;&lt;1172.0,186.0&gt;--&lt;1172.0,186.0&gt;&gt;/L&lt;&lt;1172.0,186.0&gt;--&lt;383.0,0.0&gt;&gt; = 13.264802931115398

* uni0930_uni0930_uni094D.vatu: L&lt;&lt;383.0,0.0&gt;--&lt;126.0,0.0&gt;&gt;/L&lt;&lt;126.0,0.0&gt;--&lt;1128.0,230.0&gt;&gt; = 12.927780100724538

* uni0930_uni094D.vatu: L&lt;&lt;383.0,0.0&gt;--&lt;126.0,0.0&gt;&gt;/L&lt;&lt;126.0,0.0&gt;--&lt;1951.0,416.0&gt;&gt; = 12.840898455437413

* uni0931_uni0930_uni094D.vatu: L&lt;&lt;383.0,0.0&gt;--&lt;126.0,0.0&gt;&gt;/L&lt;&lt;126.0,0.0&gt;--&lt;1158.0,202.0&gt;&gt; = 11.07485226585879

* uni0932_uni0930_uni094D.vatu: L&lt;&lt;493.0,0.0&gt;--&lt;236.0,0.0&gt;&gt;/L&lt;&lt;236.0,0.0&gt;--&lt;2015.0,404.0&gt;&gt; = 12.794521411690255

* uni0935_uni0930_uni094D.vatu: L&lt;&lt;426.0,0.0&gt;--&lt;169.0,0.0&gt;&gt;/L&lt;&lt;169.0,0.0&gt;--&lt;1974.0,411.0&gt;&gt; = 12.827587702972119

* uni0937_uni0930_uni094D.vatu: L&lt;&lt;460.0,6.0&gt;--&lt;203.0,6.0&gt;&gt;/L&lt;&lt;203.0,6.0&gt;--&lt;2002.0,416.0&gt;&gt; = 12.838675460780657

* uni0939_uni0930_uni094D.vatu: L&lt;&lt;958.0,370.0&gt;--&lt;701.0,370.0&gt;&gt;/L&lt;&lt;701.0,370.0&gt;--&lt;1766.0,615.0&gt;&gt; = 12.955319281265771

* uni0944 (U+0944): L&lt;&lt;-1109.0,-947.0&gt;--&lt;-1109.0,-947.0&gt;&gt;/L&lt;&lt;-1109.0,-947.0&gt;--&lt;-1153.0,-958.0&gt;&gt; = 14.036243467926484

* uni0944 (U+0944): L&lt;&lt;-292.0,-841.0&gt;--&lt;-1109.0,-947.0&gt;&gt;/L&lt;&lt;-1109.0,-947.0&gt;--&lt;-1109.0,-947.0&gt;&gt; = 7.392429216723766

* uni0958_uni0930_uni094D.vatu: L&lt;&lt;383.0,0.0&gt;--&lt;126.0,0.0&gt;&gt;/L&lt;&lt;126.0,0.0&gt;--&lt;1206.0,263.0&gt;&gt; = 13.686197239230474

* uni0959_uni0930_uni094D.vatu: L&lt;&lt;190.0,0.0&gt;--&lt;1814.0,370.0&gt;&gt;/L&lt;&lt;1814.0,370.0&gt;--&lt;592.0,370.0&gt;&gt; = 12.834760383293624

* uni0959_uni0930_uni094D.vatu: L&lt;&lt;447.0,0.0&gt;--&lt;190.0,0.0&gt;&gt;/L&lt;&lt;190.0,0.0&gt;--&lt;1814.0,370.0&gt;&gt; = 12.834760383293624

* uni095A_uni0930_uni094D.vatu: L&lt;&lt;453.0,0.0&gt;--&lt;196.0,0.0&gt;&gt;/L&lt;&lt;196.0,0.0&gt;--&lt;1995.0,410.0&gt;&gt; = 12.838675460780657

* uni095B_uni0930_uni094D.vatu: L&lt;&lt;448.0,0.0&gt;--&lt;191.0,0.0&gt;&gt;/L&lt;&lt;191.0,0.0&gt;--&lt;2008.0,414.0&gt;&gt; = 12.835609486401424

* uni095E_uni0930_uni094D.vatu: L&lt;&lt;383.0,0.0&gt;--&lt;126.0,0.0&gt;&gt;/L&lt;&lt;126.0,0.0&gt;--&lt;1573.0,334.0&gt;&gt; = 12.997508619477422

* uni095F_uni0930_uni094D.vatu: L&lt;&lt;383.0,0.0&gt;--&lt;126.0,0.0&gt;&gt;/L&lt;&lt;126.0,0.0&gt;--&lt;1980.0,323.0&gt;&gt; = 9.882760671675692

* uni0968 (U+0968): L&lt;&lt;398.0,486.0&gt;--&lt;417.0,488.0&gt;&gt;/L&lt;&lt;417.0,488.0&gt;--&lt;402.0,488.0&gt;&gt; = 6.009005957494474
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* backslash (U+005C): L&lt;&lt;1263.0,0.0&gt;--&lt;1271.0,1550.0&gt;&gt;

* backslash (U+005C): L&lt;&lt;1354.0,1550.0&gt;--&lt;1341.0,0.0&gt;&gt;

* eight (U+0038): L&lt;&lt;1992.0,-3.0&gt;--&lt;56.0,0.0&gt;&gt;

* grave (U+0060): L&lt;&lt;1407.0,1057.0&gt;--&lt;1406.0,1286.0&gt;&gt;

* uni0938_uni094D.haln: L&lt;&lt;701.0,659.0&gt;--&lt;697.0,0.0&gt;&gt;

* uni0943 (U+0943): L&lt;&lt;-1061.0,-178.0&gt;--&lt;-1058.0,-577.0&gt;&gt;

* uni0943 (U+0943): L&lt;&lt;-1131.0,-591.0&gt;--&lt;-1134.0,-132.0&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



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
| 0 | 0 | 40 | 117 | 928 | 49 | 748 | 0 | 
| 0% | 0% | 2% | 6% | 49% | 3% | 40% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
