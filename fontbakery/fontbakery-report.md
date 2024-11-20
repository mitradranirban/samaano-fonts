## FontBakery report

fontbakery version: 0.12.10



## Experimental checks

These won't break the CI job for now, but will become effective after some time if nobody raises any concern.


<details><summary>[6] Samaano[slnt,wdth,wght].ttf</summary>
<div>
<details>
    <summary>✅ <b>PASS</b> Check tabular widths don't have kerning. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking that the typoAscender exceeds the yMax of the /Agrave. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.metrics.html#"></a></summary>
    <div>







* ✅ **PASS** <p>OS/2.sTypoAscender value is greater than the yMax of /Agrave.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure the font's instances are in the correct order. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Does the font's CFF table top dict strings fit into the ASCII range? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.cff.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_cff</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Ensure 'smcp' (small caps) lookups are defined before ligature lookups in the 'GSUB' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Font lacks 'smcp' or 'liga' features.</p>
 



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Validate 'date_added' field on METADATA.pb. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>
</div>
</details>




## All other checks



<details><summary>[18] Family checks</summary>
<div>
<details>
    <summary>ℹ️ <b>INFO</b> Check axis ordering on the STAT table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.stat.html#"></a></summary>
    <div>







* ℹ️ **INFO** <p>None of the fonts lack a STAT table.</p>
<pre><code>And these are the most common STAT axis orderings:
('wdth-wght-slnt', 1)
</code></pre>
 [code: summary]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Fonts have consistent underline thickness? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.post.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Fonts have consistent underline thickness.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Fonts have consistent PANOSE family type? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.os2.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Make sure all font files have the same version value. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.head.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check that OS/2.fsSelection bold & italic settings are unique for each NameID1 <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.os2.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Verify that each group of fonts with the same nameID 1 has maximum of 4 fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Verify that family names in the name table are consistent across all fonts in the family. Checks Typographic Family name (nameID 16) if present, otherwise uses Font Family name (nameID 1) <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check that family axis ranges are indentical <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.fvar.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure VFs have 'ital' STAT axis. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.stat.html#"></a></summary>
    <div>







* ✅ **PASS** <p>OK</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking all files are in the same directory. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All files are in the same directory.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Each font in a family must have the same set of vertical metrics values. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.metrics.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Vertical metrics are the same across the family.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does font file include unacceptable control character glyphs? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure Italic styles have Roman counterparts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.family.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> All tabular figures must have the same width across the RIBBI-family. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.family.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> OS/2.fsSelection bit 7 (USE_TYPO_METRICS) is set in all fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.os2.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure that all variable font files have the same set of axes and axis ranges. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Fonts have equal codepoint coverage <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.family.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: stylenames_are_canonical</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Directory name in GFonts repo structure must match NameID 1 of the regular. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.repo.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: gfonts_repo_structure</p>
 [code: unfulfilled-conditions]



</div>
</details>
</div>
</details>

<details><summary>[227] Samaano[slnt,wdth,wght].ttf</summary>
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







* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 864 instead.
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
    <summary>⚠️ <b>WARN</b> Detect any interpolation issues in the font. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Interpolation issues were found in the font:</p>
<pre><code>- Contour 3 in glyph 'Dcroat': becomes underweight between wght=100,wdth=100,slnt=0 and wght=700,wdth=200,slnt=-20.

- Contour 3 in glyph 'Eth': becomes underweight between wght=100,wdth=100,slnt=0 and wght=700,wdth=200,slnt=-20.

- Contour 7 in glyph 'uni20BF': becomes underweight between wght=100,wdth=100,slnt=0 and wght=700,wdth=200,slnt=-20.
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
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, math, tifinagh, cherokee</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: elbasan, gothic, coptic, math, glagolitic</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: tai-le, old-permic, todhri, tifinagh, duployan, coptic, math, malayalam, canadian-aboriginal, syriac, hebrew</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+030F COMBINING DOUBLE GRAVE ACCENT: not included in any glyphset definition</li>
<li>U+0310 COMBINING CANDRABINDU: try adding one of: math, sunuwar</li>
<li>U+0311 COMBINING INVERTED BREVE: try adding one of: coptic, todhri</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, cherokee, duployan</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: thai, cherokee, caucasian-albanian, tifinagh, gothic, sunuwar, syriac</li>
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







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: i̐</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̅ i̇ ǐ i̒ i̛̅ i̛̇ i̛̊ i̛̋ ǐ̛ i̛̐ i̛̒ i̤̅ i̤̇ i̤̊ i̤̋ ǐ̤ i̤̐ i̤̒ i̦̅ i̦̇</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Lithuanian (Latn, 2,357,094 speakers), Dutch (Latn, 31,709,104 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Kpelle, Guinea (Latn, 622,000 speakers), Cicipu (Latn, 44,000 speakers), Ekpeye (Latn, 226,000 speakers), Igbo (Latn, 27,823,640 speakers), Lugbara (Latn, 2,200,000 speakers), Gulay (Latn, 250,478 speakers), Zapotec (Latn, 490,000 speakers), Nateni (Latn, 100,000 speakers), Ngbaka (Latn, 1,020,000 speakers), Makaa (Latn, 221,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Ejagham (Latn, 120,000 speakers), Dii (Latn, 71,000 speakers), Ebira (Latn, 2,200,000 speakers), Mango (Latn, 77,000 speakers), Nzakara (Latn, 50,000 speakers), Belarusian (Cyrl, 10,064,517 speakers), Mundani (Latn, 34,000 speakers), Fur (Latn, 1,230,163 speakers), Yala (Latn, 200,000 speakers), Aghem (Latn, 38,843 speakers), Avokaya (Latn, 100,000 speakers), Southern Kisi (Latn, 360,000 speakers), South Central Banda (Latn, 244,000 speakers), Sar (Latn, 500,000 speakers), Navajo (Latn, 166,319 speakers), Basaa (Latn, 332,940 speakers), Dan (Latn, 1,099,244 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Vute (Latn, 21,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Kom (Latn, 360,685 speakers), Mfumte (Latn, 79,000 speakers), Bafut (Latn, 158,146 speakers), Koonzime (Latn, 40,000 speakers), Ma’di (Latn, 584,000 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have on-curve points which have potentially incorrect y coordinates:</p>
<pre><code>* Eogonek (U+0118): X=334.0,Y=-1.0 (should be at baseline 0?)

* Eogonek (U+0118): X=452.0,Y=-1.0 (should be at baseline 0?)

* Eogonek (U+0118): X=334.0,Y=-1.0 (should be at baseline 0?)

* Eogonek (U+0118): X=876.0,Y=-1.0 (should be at baseline 0?)

* ccedilla (U+00E7): X=568.0,Y=2.0 (should be at baseline 0?)

* ccedilla (U+00E7): X=724.0,Y=2.0 (should be at baseline 0?)

* iogonek (U+012F): X=339.0,Y=2.0 (should be at baseline 0?)

* iogonek (U+012F): X=457.0,Y=2.0 (should be at baseline 0?)

* iogonek (U+012F): X=339.0,Y=2.0 (should be at baseline 0?)

* iogonek (U+012F): X=881.0,Y=2.0 (should be at baseline 0?)

* uni0162 (U+0162): X=447.0,Y=1.0 (should be at baseline 0?)

* uni0162 (U+0162): X=603.0,Y=1.0 (should be at baseline 0?)

* uni01EA (U+01EA): X=341.0,Y=2.0 (should be at baseline 0?)

* uni01EA (U+01EA): X=459.0,Y=2.0 (should be at baseline 0?)

* uni01EA (U+01EA): X=341.0,Y=2.0 (should be at baseline 0?)

* uni01EA (U+01EA): X=883.0,Y=2.0 (should be at baseline 0?)

* uni01EB (U+01EB): X=334.0,Y=1.0 (should be at baseline 0?)

* uni01EB (U+01EB): X=452.0,Y=1.0 (should be at baseline 0?)

* uni01EB (U+01EB): X=334.0,Y=1.0 (should be at baseline 0?)

* uni01EB (U+01EB): X=876.0,Y=1.0 (should be at baseline 0?)

* uni2116 (U+2116): X=501.0,Y=1549.0 (should be at cap-height 1548?)

* uni2116 (U+2116): X=601.0,Y=1549.0 (should be at cap-height 1548?)

* uni2116 (U+2116): X=810.0,Y=1549.0 (should be at cap-height 1548?)

* uni2116 (U+2116): X=910.0,Y=1549.0 (should be at cap-height 1548?)

* uni2116 (U+2116): X=532.0,Y=1549.0 (should be at cap-height 1548?)

* uni2116 (U+2116): X=882.0,Y=1549.0 (should be at cap-height 1548?)

* uniFB02 (U+FB02): X=240.0,Y=1547.0 (should be at cap-height 1548?)

* uniFB02 (U+FB02): X=440.0,Y=1547.0 (should be at cap-height 1548?)

* uniFB02 (U+FB02): X=241.0,Y=1547.0 (should be at cap-height 1548?)

* uniFB02 (U+FB02): X=668.0,Y=1547.0 (should be at cap-height 1548?)
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
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.os2.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>OS/2 VendorID value 'anir' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> List all superfamily filepaths <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.superfamily.html#"></a></summary>
    <div>







* ℹ️ **INFO** <p>fonts/variable</p>
 [code: family-path]



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> Font contains all required tables? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.tables.html#"></a></summary>
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
    <summary>ℹ️ <b>INFO</b> Check for presence of an ARTICLE.en_us.html file <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.description.html#"></a></summary>
    <div>







* ℹ️ **INFO** <p>This font doesn't have an ARTICLE.en_us.html file.</p>
 [code: missing-article]



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> EPAR table present in font? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.license.html#"></a></summary>
    <div>







* ℹ️ **INFO** <p>EPAR table not present in font. To learn more see <a href="https://github.com/fonttools/fontbakery/issues/818">https://github.com/fonttools/fontbakery/issues/818</a></p>
 [code: lacks-EPAR]



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.hinting.html#"></a></summary>
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
    <summary>ℹ️ <b>INFO</b> Show hinting filesize impact. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.hinting.html#"></a></summary>
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
<td align="right">272.0kb</td>
</tr>
<tr>
<td align="left">Hinted Size</td>
<td align="right">272.1kb</td>
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
    <summary>ℹ️ <b>INFO</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ℹ️ **INFO** <p>Latn</p>
 [code: dlng-tag]



* ℹ️ **INFO** <p>Latn,Deva</p>
 [code: slng-tag]



</div>
</details>

<details>
    <summary>ℹ️ <b>INFO</b> Font has old ttfautohint applied? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.hinting.html#"></a></summary>
    <div>







* ℹ️ **INFO** <p>Could not detect which version of ttfautohint was used in this font. It is typically specified as a comment in the font version entries of the 'name' table. Such font version strings are currently: ['Version 2.000']</p>
 [code: version-not-detected]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Name table ID 6 (PostScript name) must be consistent across platforms. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check name table for empty records. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Description strings in the name table must not contain copyright info. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does full font name begin with the font family name? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> The variable font 'wght' (Weight) axis coordinate must be 400 on the 'Regular' instance. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.fvar.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Regular:wght is 400.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> The variable font 'wdth' (Width) axis coordinate must be 100 on the 'Regular' instance. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.fvar.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Regular:wdth is 100.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> The variable font 'slnt' (Slant) axis coordinate must be zero on the 'Regular' instance. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.fvar.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Regular:slnt is zero.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> The variable font 'slnt' (Slant) axis coordinate specifies positive values in its range? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.fvar.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> The variable font 'wght' (Weight) axis coordinate must be within spec range of 1 to 1000 on all instances. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.fvar.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> The variable font 'wdth' (Width) axis coordinate must strictly greater than zero. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.fvar.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> All fvar axes have a correspondent Axis Record on STAT table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.stat.html#"></a></summary>
    <div>







* ✅ **PASS** <p>STAT table has all necessary Axis Records.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does the number of glyphs in the loca table match the maxp table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.loca.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking font version fields (head and name table). <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.head.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Font has correct post table version? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.post.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Font has an acceptable post format 2.0 table version.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check if OS/2 xAvgCharWidth is correct. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.os2.html#"></a></summary>
    <div>







* ✅ **PASS** <p>OS/2 xAvgCharWidth value is correct.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check if OS/2 fsSelection matches head macStyle bold and italic bits. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.os2.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking unitsPerEm value is reasonable. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.head.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does the font have a DSIG table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.dsig.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check glyphs in mark glyph class are non-spacing. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check GDEF mark glyph class doesn't have characters that are not marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gpos.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Is there a usable "kern" table declared in the font? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.kern.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Font does not declare an optional &quot;kern&quot; table.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Is there any unused data at the end of the glyf table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.glyf.html#"></a></summary>
    <div>







* ✅ **PASS** <p>There is no unused data at the end of the glyf table.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Font follows the family naming recommendations? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> MaxAdvanceWidth is consistent with values in the Hmtx and Hhea tables? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.hhea.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> PostScript name follows OpenType specification requirements? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check for points out of bounds. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.glyf.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check glyphs do not have duplicate components which have the same x,y coordinates. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.glyf.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check code page character ranges <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.os2.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does the font have any invalid feature tags? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.layout.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does the font have any invalid script tags? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.layout.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does the font have any invalid language tags? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.layout.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking post.italicAngle value. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.post.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Value of post.italicAngle is 0.0 with style=&quot;Bold&quot;.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking head.macStyle value. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.head.html#"></a></summary>
    <div>







* ✅ **PASS** <p>head macStyle ITALIC bit is properly set.</p>
 



* ✅ **PASS** <p>head macStyle BOLD bit is properly set.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking OS/2 fsSelection value. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.os2.html#"></a></summary>
    <div>







* ✅ **PASS** <p>OS/2 fsSelection REGULAR bit is properly set.</p>
 



* ✅ **PASS** <p>OS/2 fsSelection ITALIC bit is properly set.</p>
 



* ✅ **PASS** <p>OS/2 fsSelection BOLD bit is properly set.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Validates that the value of axisNameID used by each VariationAxisRecord is greater than 255 and less than 32768. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.fvar.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Validates that the value of subfamilyNameID used by each InstanceRecord is 2, 17, or greater than 255 and less than 32768. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.fvar.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Validates that the value of postScriptNameID used by each InstanceRecord is 6, 0xFFFF, or greater than 255 and less than 32768. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.fvar.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Validates that when an instance record is included for the default instance, its subfamilyNameID value is set to a name ID whose string is equal to the string of either name ID 2 or 17, and its postScriptNameID value is set to a name ID whose string is equal to the string of name ID 6. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.fvar.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Validates that all of the instance records in a given font have the same size. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.fvar.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Validates that all of the instance records in a given font have distinct data. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.fvar.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Validate foundry-defined design-variation axis tag names. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.fvar.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> STAT table has Axis Value tables? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.stat.html#"></a></summary>
    <div>







* ✅ **PASS** <p>STAT table has Axis Value tables.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check hhea.caretSlopeRise and hhea.caretSlopeRun <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.hhea.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check that Arabic spacing symbols U+FBB2–FBC1 aren't classified as marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.arabic.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Looks good!</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Looks good!</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.metrics.html#"></a></summary>
    <div>







* ✅ **PASS** <p>OS/2 usWinAscent &amp; usWinDescent values look good!</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Do we have the latest version of FontBakery installed? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.fontbakery.html#"></a></summary>
    <div>







* ✅ **PASS** <p>FontBakery is up-to-date.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure that the font can be rasterized by FreeType. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Font can be rasterized by FreeType.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure no GPOS7 lookups are present. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Font has no GPOS7 lookups</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check that legacy accents aren't used in composite glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Looks good!</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking Vertical Metric Linegaps. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.metrics.html#"></a></summary>
    <div>







* ✅ **PASS** <p>OS/2 sTypoLineGap and hhea lineGap are both 0.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Font contains '.notdef' as its first glyph? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ✅ **PASS** <p>OK</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Looks good.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Name table records must not have trailing spaces. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ✅ **PASS** <p>No trailing spaces on name table entries.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking OS/2 Metrics match hhea Metrics. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.metrics.html#"></a></summary>
    <div>







* ✅ **PASS** <p>OS/2.sTypoAscender/Descender values match hhea.ascent/descent.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking with ots-sanitize. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.sanitize.html#"></a></summary>
    <div>







* ✅ **PASS** <p>ots-sanitize passed this file</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure indic fonts have the Indian Rupee Sign glyph. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Looks good!</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Font has the proper sfntVersion value? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Font has the correct sfntVersion value.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Looks good!</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check correctness of STAT table strings <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.stat.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Looks good!</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure component transforms do not perform scaling or rotation. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ✅ **PASS** <p>No glyphs had components with scaling or rotation</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking with fontTools.ttx <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.sanitize.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Font contains unique glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Glyph names are all unique.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Font did not contain any unreachable glyphs</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Are there unwanted tables? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.tables.html#"></a></summary>
    <div>







* ✅ **PASS** <p>There are no unwanted tables.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Glyph names are all valid.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Font has **proper** whitespace glyph names? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Font has <strong>AGL recommended</strong> names for whitespace glyphs.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Font contains glyphs for whitespace characters? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Font contains glyphs for whitespace characters.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Whitespace glyphs have ink? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ✅ **PASS** <p>There is no whitespace glyph with ink.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Space and non-breaking space have the same width? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Space and non-breaking space have the same width.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check name ID 25 to end with "Italic" for Italic VFs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Combined length of family and style must not exceed 32 characters. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check family name for GF Guide compliance. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check copyright namerecords match license file. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.license.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> License URL matches License text on name table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.license.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Font has a valid license URL in NAME table.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Name table entries should not contain line-breaks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Name table strings must not contain the string 'Reserved Font Name'. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.license.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Substitute copyright, registered and trademark symbols in name table entries. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check OFL body text is correct. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.license.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check license file has good copyright string. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.license.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> A font repository should not include FontBakery report files <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.repo.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> A font repository should not include ZIP files <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.repo.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All marks were anchored to dotted circle</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Are there unwanted Apple tables? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.tables.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking file is named canonically. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Font filename is correct, &quot;Samaano[slnt,wdth,wght].ttf&quot;.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Color layers should have a minimum brightness <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.color.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check font has the expected color font tables. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.color.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Put an empty glyph on GID 1 right after the .notdef glyph for COLRv0 fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.color.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure files are not too large. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Font had a reasonable file size</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Copyright notices match canonical pattern in fonts <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.copyright.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Font familyname seems to be unique.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check font names are correct <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking OS/2 fsType does not impose restrictions. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.os2.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check variable font instances <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> All name entries referenced by fvar instances exist on the name table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Validate defaults on fvar table match registered fallback names in GFAxisRegistry. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.axisregistry.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check glyphs do not have components which are themselves components. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyf.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check Google Fonts glyph coverage. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check small caps glyphs are available. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Are there non-ASCII characters in ASCII-only NAME table entries? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Description strings in the name table must not exceed 200 characters. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Make sure family name does not begin with a digit. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Font has all mandatory 'name' table entries? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Version format is correct in 'name' table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure fonts do not contain any pre-production tables. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.tables.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check font can render its own name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Checking direction of slnt axis angles <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Font enables smart dropout control in "prep" table instructions? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.hinting.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure Stylistic Sets have description. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.gsub.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Stricter unitsPerEm criteria for Google Fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.head.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check the OS/2 usWeightClass is appropriate for the font's best SubFamily name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.os2.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> The variable font 'wght' (Weight) axis coordinate must be 700 on the 'Bold' instance. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* ✅ **PASS** <p>Bold:wght is 700.</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check variable font instances don't have duplicate names <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check a static ttf can be generated from a variable font. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* ✅ **PASS** <p>fontTools.varLib.mutator generated a static font instance</p>
 



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check that variable fonts have an HVAR table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Ensure VFs do not contain the ital axis. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> Check font follows the Google Fonts vertical metric schema <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.vmetrics.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>✅ <b>PASS</b> There must not be VTT Talk sources in the font. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.hinting.html#"></a></summary>
    <div>







* ✅ **PASS** <p>All looks good!</p>
 [code: ok]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> CFF table FontName must match name table ID 6 (PostScript name). <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_cff</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> The variable font 'ital' (Italic) axis coordinate must be zero on the 'Regular' instance. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.fvar.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: has_ital_axis</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> The variable font 'opsz' (Optical Size) axis coordinate should be between 10 and 16 on the 'Regular' instance. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.fvar.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: has_opsz_axis</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> The variable font 'ital' (Italic) axis coordinates is in a valid range? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.fvar.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: has_ital_axis</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Is the CFF subr/gsubr call depth > 10? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.cff.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_cff</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Does the font use deprecated CFF operators or operations? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.cff.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_cff</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Is the CFF2 subr/gsubr call depth > 10? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.cff.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_cff2</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check name table IDs 1, 2, 16, 17 to conform to Italic style. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.name.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Font is not Italic.</p>
 



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Checking OS/2 achVendID against configuration. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.os2.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Add the <code>vendor_id</code> key to a <code>fontbakery.yaml</code> file on your font project directory to enable this check.
You'll also need to use the <code>--configuration</code> flag when invoking fontbakery.</p>
 



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Ensure 'ital' STAT axis is boolean value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.stat.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Font doesn't have an ital axis</p>
 



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Ensure 'ital' STAT axis is last. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.stat.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>No 'ital' axis in STAT.</p>
 



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Each font in set of sibling families must have the same set of vertical metrics values. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.superfamily.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Sibling families were not detected.</p>
 



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check that glyph for U+0675 ARABIC LETTER HIGH HAMZA is not a mark. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.arabic.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>This check will only run on fonts that have both glyphs U+0621 and U+0675</p>
 [code: glyphs-missing]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Does the font contain chws and vchw features? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_cjk_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: not is_variable_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Checking STAT table entries in static fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.stat.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: not is_variable_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Does METADATA.pb copyright field contain broken links? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Font styles are named canonically? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Check that font weight has a canonical value. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check samples can be rendered. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Ensure METADATA.pb category field is valid. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check if category on METADATA.pb matches what can be inferred from the family name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Validate VF axes match the ones declared on METADATA.pb. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Check URL on copyright string is the same as in repository_url field. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Copyright notice is the same in all fonts? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Designers are listed correctly on the Google Fonts catalog? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Multiple values in font designer field in METADATA.pb must be separated by commas. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> At least one designer is declared in METADATA.pb <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>No applicable arguments</p>
 [code: no-arguments]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Ensure METADATA.pb does not use escaped strings. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: metadata_file</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check font family directory name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check that METADATA.pb family values are all the same. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Font filenames match font.filename entries? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Validate METADATA.pb axes values are within gf_axisregistry bounds. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.axisregistry.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Validate METADATA.pb axes tags are defined in gf_axisregistry. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.axisregistry.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Ensure there is a regular style defined in METADATA.pb. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check METADATA.pb includes production subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata, listed_on_gfonts_api</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check METADATA.pb file only contains a single CJK subset. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb license is "APACHE2", "UFL" or "OFL"? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.license.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb font.filename and font.post_script_name fields have equivalent values? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata, not is_variable_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb font.full_name and font.post_script_name fields have equivalent values ? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Check font name is the same as family name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata, font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb weight matches postScriptName for static fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata, not is_variable_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb should contain at least "menu" and "latin" subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Validate family.minisite_url field. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb font.name and font.full_name fields match the values declared on the name table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb font.name value should be same as the family name declared on the name table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Checks METADATA.pb font.post_script_name matches postscript name declared on the name table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check METADATA.pb font weights are correct. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check METADATA.pb parse correctly. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Font family at 'fonts/variable' lacks a METADATA.pb file.</p>
 [code: file-not-found]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Check for primary_script <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: Regular should be 400. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata, has_regular_style</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Copyright notice on METADATA.pb should not contain 'Reserved Font Name'. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb subsets should be alphabetically ordered. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Ensure METADATA.pb lists all font binaries. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: check if fonts field only has unique "full_name" values. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb: check if fonts field only contains unique style:weight pairs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check for METADATA subsets with zero support. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb font.filename field contains font name in right format? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: family_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb font.full_name field contains font name in right format? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> METADATA.pb font.post_script_name field contains font name in right format? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.metadata.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: font_metadata</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Does DESCRIPTION file contain broken links? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.description.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: description_and_article_html</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> DESCRIPTION.en_us.html should end in a linebreak. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.description.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: description</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> On a family update, the DESCRIPTION.en_us.html file should ideally also be updated. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.description.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: description</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Does DESCRIPTION file contain a upstream Git repo URL? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.description.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: description_html</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check the description doesn't contain unsupported html elements <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.description.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: description_and_article</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> DESCRIPTION.en_us.html must have more than 200 bytes. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.description.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: description</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> URLs on DESCRIPTION file must not display http(s) prefix. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.description.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: description_and_article_html</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Is this a proper HTML snippet? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.description.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: description_and_article</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check font has a license. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.license.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: gfonts_repo_structure</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check upstream.yaml file contains all required fields <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.repo.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: upstream_yaml</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> A static fonts directory, if present, must contain manually hinted fonts <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.repo.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: gfonts_repo_structure</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check that texts shape as per expectation <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Shaping test directory not defined in configuration file</p>
 



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check that no forbidden glyphs are found while shaping <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Shaping test directory not defined in configuration file</p>
 



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check that no collisions are found while shaping <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Shaping test directory not defined in configuration file</p>
 



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Are any segments inordinately short? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: not is_variable_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: not is_variable_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: not is_variable_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: not is_variable_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Does the font contain less than 150 CJK characters? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_claiming_to_be_cjk_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check font follows the Google Fonts CJK vertical metric schema <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.vmetrics.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_cjk_font</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check if the vertical metrics of a CJK family are similar to the same family hosted on Google Fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.vmetrics.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_cjk_font, regular_remote_style</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Font has ttfautohint params? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.hinting.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Font appears to our heuristic as not hinted using ttfautohint.</p>
 [code: not-hinted]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> PPEM must be an integer on hinted fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.hinting.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: is_hinted</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Is there kerning info for non-ligated sequences? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.gpos.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: has_kerning_info</p>
 [code: unfulfilled-conditions]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Ensure VFs with duplexed axes do not vary horizontal advance. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.varfont.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>This font has no duplexed axes</p>
 [code: no-relevant-axes]



</div>
</details>

<details>
    <summary>⏩ <b>SKIP</b> Check if the vertical metrics of a family are similar to the same family hosted on Google Fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.vmetrics.html#"></a></summary>
    <div>







* ⏩ **SKIP** <p>Unfulfilled Conditions: regular_remote_style</p>
 [code: unfulfilled-conditions]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 11 | 91 | 9 | 139 | 0 | 
| 0% | 0% | 0% | 4% | 36% | 4% | 55% | 0% | 



**Note:** The following loglevels were omitted in this report:


* DEBUG
