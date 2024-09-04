## FontBakery report

fontbakery version: 0.12.10





## Check results



<details><summary>[23] Samaano[wdth,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> The variable font 'wdth' (Width) axis coordinate must be 100 on the 'Regular' instance. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.fvar.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The &quot;wdth&quot; axis coordinate of the &quot;Regular&quot; instance must be 100. Got 50.0 as a default value instead.</p>
 [code: wdth-not-100]



</div>
</details>

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







* 🔥 **FAIL** <p>The PANOSE numbers are incorrect for a monospaced font.</p>
 [code: mono-bad-panose]



* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 94 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



* ⚠️ **WARN** <p>Font is monospaced but 1 glyphs (0.79%) have a different width. You should check the widths of: ['underscore']</p>
 [code: mono-outliers]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Validates that when an instance record is included for the default instance, its subfamilyNameID value is set to a name ID whose string is equal to the string of either name ID 2 or 17, and its postScriptNameID value is set to a name ID whose string is equal to the string of name ID 6. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.fvar.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>'Black' instance has the same coordinates as the default instance; its subfamily name should be 'UltraCondensed Black'.</p>
<p>Note: It is alternatively possible that Name ID 17 is incorrect, and should be set to the default instance subfamily name, 'Black', rather than ''UltraCondensed Black''. If the default instance is 'Black', NameID 17 is probably the problem.</p>
 [code: invalid-default-instance-subfamily-name]



* 🔥 **FAIL** <p>'Black' instance has the same coordinates as the default instance; its postscript name should be 'Samaano-UltraCondensedBlack', instead of 'Samaano-Black'.</p>
 [code: invalid-default-instance-postscript-name]



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
    <summary>🔥 <b>FAIL</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphnames.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyph names do not comply with naming conventions: ja-deva</p>
<p>A glyph name must be entirely comprised of characters from the following set: A-Z a-z 0-9 .(period) <em>(underscore). A glyph name must not start with a digit or period. There are a few exceptions such as the special glyph &quot;.notdef&quot;. The glyph names &quot;twocents&quot;, &quot;a1&quot;, and &quot;</em>&quot; are all valid, while &quot;2cents&quot; and &quot;.twocents&quot; are not.</p>
 [code: found-invalid-names]



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
    <summary>🔥 <b>FAIL</b> Combined length of family and style must not exceed 32 characters. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.name.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>Variable font instance name 'Samaano UltraCondensed Black Thin' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 258 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Samaano UltraCondensed Black Thin' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 258 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Samaano UltraCondensed Black ExtraLight' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 260 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Samaano UltraCondensed Black ExtraLight' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 260 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Samaano UltraCondensed Black Light' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 262 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Samaano UltraCondensed Black Light' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 262 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Samaano UltraCondensed Black Regular' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 264 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Samaano UltraCondensed Black Regular' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 264 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Samaano UltraCondensed Black Medium' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 266 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Samaano UltraCondensed Black Medium' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 266 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Samaano UltraCondensed Black SemiBold' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 268 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Samaano UltraCondensed Black SemiBold' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 268 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Samaano UltraCondensed Black Bold' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 270 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Samaano UltraCondensed Black Bold' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 270 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Samaano UltraCondensed Black ExtraBold' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 272 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Samaano UltraCondensed Black ExtraBold' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 272 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Samaano UltraCondensed Black Black' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 274 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



* 🔥 **FAIL** <p>Variable font instance name 'Samaano UltraCondensed Black Black' formed by space-separated concatenation of font family name (nameID 1) and instance subfamily nameID 274 exceeds 32 characters.</p>
<p>This has been found to cause shaping issues for some accented letters in Microsoft Word on Windows 10 and 11.</p>
 [code: instance-too-long]



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


- 0x00C0 (LATIN CAPITAL LETTER A WITH GRAVE)


- 0x00C1 (LATIN CAPITAL LETTER A WITH ACUTE)


- 0x00C2 (LATIN CAPITAL LETTER A WITH CIRCUMFLEX)


- 0x00C3 (LATIN CAPITAL LETTER A WITH TILDE)


- 0x00C4 (LATIN CAPITAL LETTER A WITH DIAERESIS)


- 0x00C5 (LATIN CAPITAL LETTER A WITH RING ABOVE)


- 0x00C6 (LATIN CAPITAL LETTER AE)


- 0x00C7 (LATIN CAPITAL LETTER C WITH CEDILLA)


- 0x00C8 (LATIN CAPITAL LETTER E WITH GRAVE)


- 0x00C9 (LATIN CAPITAL LETTER E WITH ACUTE)


- 0x00CA (LATIN CAPITAL LETTER E WITH CIRCUMFLEX)


- 0x00CB (LATIN CAPITAL LETTER E WITH DIAERESIS)


- 0x00CC (LATIN CAPITAL LETTER I WITH GRAVE)


- 0x00CD (LATIN CAPITAL LETTER I WITH ACUTE)


- 0x00CE (LATIN CAPITAL LETTER I WITH CIRCUMFLEX)


- 0x00CF (LATIN CAPITAL LETTER I WITH DIAERESIS)


- 0x00D0 (LATIN CAPITAL LETTER ETH)


- 0x00D1 (LATIN CAPITAL LETTER N WITH TILDE)


- 0x00D2 (LATIN CAPITAL LETTER O WITH GRAVE)


- 0x00D3 (LATIN CAPITAL LETTER O WITH ACUTE)


- 0x00D4 (LATIN CAPITAL LETTER O WITH CIRCUMFLEX)


- 0x00D5 (LATIN CAPITAL LETTER O WITH TILDE)


- 0x00D6 (LATIN CAPITAL LETTER O WITH DIAERESIS)


- 0x00D7 (MULTIPLICATION SIGN)


- 0x00D8 (LATIN CAPITAL LETTER O WITH STROKE)


- 0x00D9 (LATIN CAPITAL LETTER U WITH GRAVE)


- 0x00DA (LATIN CAPITAL LETTER U WITH ACUTE)


- 0x00DB (LATIN CAPITAL LETTER U WITH CIRCUMFLEX)


- 0x00DC (LATIN CAPITAL LETTER U WITH DIAERESIS)


- 0x00DD (LATIN CAPITAL LETTER Y WITH ACUTE)


- 0x00DE (LATIN CAPITAL LETTER THORN)


- 0x00DF (LATIN SMALL LETTER SHARP S)


- 0x00E0 (LATIN SMALL LETTER A WITH GRAVE)


- 0x00E1 (LATIN SMALL LETTER A WITH ACUTE)


- 0x00E2 (LATIN SMALL LETTER A WITH CIRCUMFLEX)


- 0x00E3 (LATIN SMALL LETTER A WITH TILDE)


- 0x00E4 (LATIN SMALL LETTER A WITH DIAERESIS)


- 0x00E5 (LATIN SMALL LETTER A WITH RING ABOVE)


- 0x00E6 (LATIN SMALL LETTER AE)


- 0x00E7 (LATIN SMALL LETTER C WITH CEDILLA)


- 0x00E8 (LATIN SMALL LETTER E WITH GRAVE)


- 0x00E9 (LATIN SMALL LETTER E WITH ACUTE)


- 0x00EA (LATIN SMALL LETTER E WITH CIRCUMFLEX)


- 0x00EB (LATIN SMALL LETTER E WITH DIAERESIS)


- 0x00EC (LATIN SMALL LETTER I WITH GRAVE)


- 0x00ED (LATIN SMALL LETTER I WITH ACUTE)


- 0x00EE (LATIN SMALL LETTER I WITH CIRCUMFLEX)


- 0x00EF (LATIN SMALL LETTER I WITH DIAERESIS)


- 0x00F0 (LATIN SMALL LETTER ETH)


- 0x00F1 (LATIN SMALL LETTER N WITH TILDE)


- 0x00F2 (LATIN SMALL LETTER O WITH GRAVE)


- 0x00F3 (LATIN SMALL LETTER O WITH ACUTE)


- 0x00F4 (LATIN SMALL LETTER O WITH CIRCUMFLEX)


- 0x00F5 (LATIN SMALL LETTER O WITH TILDE)


- 0x00F6 (LATIN SMALL LETTER O WITH DIAERESIS)


- 0x00F7 (DIVISION SIGN)


- 0x00F8 (LATIN SMALL LETTER O WITH STROKE)


- 0x00F9 (LATIN SMALL LETTER U WITH GRAVE)


- 0x00FA (LATIN SMALL LETTER U WITH ACUTE)


- 0x00FB (LATIN SMALL LETTER U WITH CIRCUMFLEX)


- 0x00FC (LATIN SMALL LETTER U WITH DIAERESIS)


- 0x00FD (LATIN SMALL LETTER Y WITH ACUTE)


- 0x00FE (LATIN SMALL LETTER THORN)


- 0x00FF (LATIN SMALL LETTER Y WITH DIAERESIS)


- 0x0100 (LATIN CAPITAL LETTER A WITH MACRON)


- 0x0101 (LATIN SMALL LETTER A WITH MACRON)


- 0x0102 (LATIN CAPITAL LETTER A WITH BREVE)


- 0x0103 (LATIN SMALL LETTER A WITH BREVE)


- 0x0104 (LATIN CAPITAL LETTER A WITH OGONEK)


- 0x0105 (LATIN SMALL LETTER A WITH OGONEK)


- 0x0106 (LATIN CAPITAL LETTER C WITH ACUTE)


- 0x0107 (LATIN SMALL LETTER C WITH ACUTE)


- 0x010A (LATIN CAPITAL LETTER C WITH DOT ABOVE)


- 0x010B (LATIN SMALL LETTER C WITH DOT ABOVE)


- 0x010C (LATIN CAPITAL LETTER C WITH CARON)


- 0x010D (LATIN SMALL LETTER C WITH CARON)


- 0x010E (LATIN CAPITAL LETTER D WITH CARON)


- 0x010F (LATIN SMALL LETTER D WITH CARON)


- 0x0110 (LATIN CAPITAL LETTER D WITH STROKE)


- 0x0111 (LATIN SMALL LETTER D WITH STROKE)


- 0x0112 (LATIN CAPITAL LETTER E WITH MACRON)


- 0x0113 (LATIN SMALL LETTER E WITH MACRON)


- 0x0116 (LATIN CAPITAL LETTER E WITH DOT ABOVE)


- 0x0117 (LATIN SMALL LETTER E WITH DOT ABOVE)


- 0x0118 (LATIN CAPITAL LETTER E WITH OGONEK)


- 0x0119 (LATIN SMALL LETTER E WITH OGONEK)


- 0x011A (LATIN CAPITAL LETTER E WITH CARON)


- 0x011B (LATIN SMALL LETTER E WITH CARON)


- 0x011E (LATIN CAPITAL LETTER G WITH BREVE)


- 0x011F (LATIN SMALL LETTER G WITH BREVE)


- 0x0120 (LATIN CAPITAL LETTER G WITH DOT ABOVE)


- 0x0121 (LATIN SMALL LETTER G WITH DOT ABOVE)


- 0x0122 (LATIN CAPITAL LETTER G WITH CEDILLA)


- 0x0123 (LATIN SMALL LETTER G WITH CEDILLA)


- 0x0126 (LATIN CAPITAL LETTER H WITH STROKE)


- 0x0127 (LATIN SMALL LETTER H WITH STROKE)


- 0x012A (LATIN CAPITAL LETTER I WITH MACRON)


- 0x012B (LATIN SMALL LETTER I WITH MACRON)


- 0x012E (LATIN CAPITAL LETTER I WITH OGONEK)


- 0x012F (LATIN SMALL LETTER I WITH OGONEK)


- 0x0130 (LATIN CAPITAL LETTER I WITH DOT ABOVE)


- 0x0131 (LATIN SMALL LETTER DOTLESS I)


- 0x0136 (LATIN CAPITAL LETTER K WITH CEDILLA)


- 0x0137 (LATIN SMALL LETTER K WITH CEDILLA)


- 0x0139 (LATIN CAPITAL LETTER L WITH ACUTE)


- 0x013A (LATIN SMALL LETTER L WITH ACUTE)


- 0x013B (LATIN CAPITAL LETTER L WITH CEDILLA)


- 0x013C (LATIN SMALL LETTER L WITH CEDILLA)


- 0x013D (LATIN CAPITAL LETTER L WITH CARON)


- 0x013E (LATIN SMALL LETTER L WITH CARON)


- 0x0141 (LATIN CAPITAL LETTER L WITH STROKE)


- 0x0142 (LATIN SMALL LETTER L WITH STROKE)


- 0x0143 (LATIN CAPITAL LETTER N WITH ACUTE)


- 0x0144 (LATIN SMALL LETTER N WITH ACUTE)


- 0x0145 (LATIN CAPITAL LETTER N WITH CEDILLA)


- 0x0146 (LATIN SMALL LETTER N WITH CEDILLA)


- 0x0147 (LATIN CAPITAL LETTER N WITH CARON)


- 0x0148 (LATIN SMALL LETTER N WITH CARON)


- 0x0150 (LATIN CAPITAL LETTER O WITH DOUBLE ACUTE)


- 0x0151 (LATIN SMALL LETTER O WITH DOUBLE ACUTE)


- 0x0152 (LATIN CAPITAL LIGATURE OE)


- 0x0153 (LATIN SMALL LIGATURE OE)


- 0x0154 (LATIN CAPITAL LETTER R WITH ACUTE)


- 0x0155 (LATIN SMALL LETTER R WITH ACUTE)


- 0x0158 (LATIN CAPITAL LETTER R WITH CARON)


- 0x0159 (LATIN SMALL LETTER R WITH CARON)


- 0x015A (LATIN CAPITAL LETTER S WITH ACUTE)


- 0x015B (LATIN SMALL LETTER S WITH ACUTE)


- 0x015E (LATIN CAPITAL LETTER S WITH CEDILLA)


- 0x015F (LATIN SMALL LETTER S WITH CEDILLA)


- 0x0160 (LATIN CAPITAL LETTER S WITH CARON)


- 0x0161 (LATIN SMALL LETTER S WITH CARON)


- 0x0164 (LATIN CAPITAL LETTER T WITH CARON)


- 0x0165 (LATIN SMALL LETTER T WITH CARON)


- 0x016A (LATIN CAPITAL LETTER U WITH MACRON)


- 0x016B (LATIN SMALL LETTER U WITH MACRON)


- 0x016E (LATIN CAPITAL LETTER U WITH RING ABOVE)


- 0x016F (LATIN SMALL LETTER U WITH RING ABOVE)


- 0x0170 (LATIN CAPITAL LETTER U WITH DOUBLE ACUTE)


- 0x0171 (LATIN SMALL LETTER U WITH DOUBLE ACUTE)


- 0x0172 (LATIN CAPITAL LETTER U WITH OGONEK)


- 0x0173 (LATIN SMALL LETTER U WITH OGONEK)


- 0x0174 (LATIN CAPITAL LETTER W WITH CIRCUMFLEX)


- 0x0175 (LATIN SMALL LETTER W WITH CIRCUMFLEX)


- 0x0176 (LATIN CAPITAL LETTER Y WITH CIRCUMFLEX)


- 0x0177 (LATIN SMALL LETTER Y WITH CIRCUMFLEX)


- 0x0178 (LATIN CAPITAL LETTER Y WITH DIAERESIS)


- 0x0179 (LATIN CAPITAL LETTER Z WITH ACUTE)


- 0x017A (LATIN SMALL LETTER Z WITH ACUTE)


- 0x017B (LATIN CAPITAL LETTER Z WITH DOT ABOVE)


- 0x017C (LATIN SMALL LETTER Z WITH DOT ABOVE)


- 0x017D (LATIN CAPITAL LETTER Z WITH CARON)


- 0x017E (LATIN SMALL LETTER Z WITH CARON)


- 0x0218 (LATIN CAPITAL LETTER S WITH COMMA BELOW)


- 0x0219 (LATIN SMALL LETTER S WITH COMMA BELOW)


- 0x021A (LATIN CAPITAL LETTER T WITH COMMA BELOW)


- 0x021B (LATIN SMALL LETTER T WITH COMMA BELOW)


- 0x0237 (LATIN SMALL LETTER DOTLESS J)


- 0x02C6 (MODIFIER LETTER CIRCUMFLEX ACCENT)


- 0x02C7 (CARON)


- 0x02D8 (BREVE)


- 0x02D9 (DOT ABOVE)


- 0x02DA (RING ABOVE)


- 0x02DB (OGONEK)


- 0x02DC (SMALL TILDE)


- 0x02DD (DOUBLE ACUTE ACCENT)


- 0x0302 (COMBINING CIRCUMFLEX ACCENT)


- 0x0303 (COMBINING TILDE)


- 0x0304 (COMBINING MACRON)


- 0x0306 (COMBINING BREVE)


- 0x0307 (COMBINING DOT ABOVE)


- 0x0308 (COMBINING DIAERESIS)


- 0x030A (COMBINING RING ABOVE)


- 0x030B (COMBINING DOUBLE ACUTE ACCENT)


- 0x030C (COMBINING CARON)


- 0x0326 (COMBINING COMMA BELOW)


- 0x0327 (COMBINING CEDILLA)


- 0x0328 (COMBINING OGONEK)


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
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.gdef.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
acutecomb (U+0301), gravecomb (U+0300), uni0900 (U+0900), uni0901 (U+0901) and uni0902 (U+0902)</p>
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
    <summary>⚠️ <b>WARN</b> Detect any interpolation issues in the font. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Interpolation issues were found in the font:</p>
<pre><code>- Contour order differs in glyph 'uni090E': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] in wght=900,wdth=200, [7, 8, 9, 0, 1, 2, 3, 4, 5, 6] in wght=100,wdth=50.

- Contour order differs in glyph 'uni090D': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] in wght=900,wdth=200, [7, 8, 9, 0, 1, 2, 3, 4, 5, 6] in wght=100,wdth=50.
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
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>latin-ext</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: j̀ j́</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: ì í</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Mfumte (Latn, 79,000 speakers), Mundani (Latn, 34,000 speakers), Yala (Latn, 200,000 speakers), Ngbaka (Latn, 1,020,000 speakers), Navajo (Latn, 166,319 speakers), Ekpeye (Latn, 226,000 speakers), Koonzime (Latn, 40,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Ejagham (Latn, 120,000 speakers), Kom (Latn, 360,685 speakers), Dii (Latn, 71,000 speakers), South Central Banda (Latn, 244,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Ma’di (Latn, 584,000 speakers), Sar (Latn, 500,000 speakers), Igbo (Latn, 27,823,640 speakers), Belarusian (Cyrl, 10,064,517 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Gulay (Latn, 250,478 speakers), Lugbara (Latn, 2,200,000 speakers), Fur (Latn, 1,230,163 speakers), Zapotec (Latn, 490,000 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Southern Kisi (Latn, 360,000 speakers), Avokaya (Latn, 100,000 speakers), Bafut (Latn, 158,146 speakers), Nateni (Latn, 100,000 speakers), Vute (Latn, 21,000 speakers), Dutch (Latn, 31,709,104 speakers), Lithuanian (Latn, 2,357,094 speakers), Makaa (Latn, 221,000 speakers), Mango (Latn, 77,000 speakers), Cicipu (Latn, 44,000 speakers), Dan (Latn, 1,099,244 speakers), Aghem (Latn, 38,843 speakers), Basaa (Latn, 332,940 speakers), Nzakara (Latn, 50,000 speakers), Ebira (Latn, 2,200,000 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* .notdef has a counter-clockwise outer contour

* C (U+0043) has a counter-clockwise outer contour

* C (U+0043) has a counter-clockwise outer contour

* C (U+0043) has a counter-clockwise outer contour

* X (U+0058) has a counter-clockwise outer contour

* braceright (U+007D) has a counter-clockwise outer contour

* braceright (U+007D) has a counter-clockwise outer contour

* braceright (U+007D) has a counter-clockwise outer contour

* braceright (U+007D) has a counter-clockwise outer contour

* braceright (U+007D) has a counter-clockwise outer contour

* braceright (U+007D) has a counter-clockwise outer contour

* eight (U+0038) has a counter-clockwise outer contour

* eight (U+0038) has a counter-clockwise outer contour

* eight (U+0038) has a counter-clockwise outer contour

* eight (U+0038) has a counter-clockwise outer contour

* eight (U+0038) has a counter-clockwise outer contour

* eight (U+0038) has a counter-clockwise outer contour

* eight (U+0038) has a counter-clockwise outer contour

* five (U+0035) has a counter-clockwise outer contour

* five (U+0035) has a counter-clockwise outer contour

* five (U+0035) has a counter-clockwise outer contour

* five (U+0035) has a counter-clockwise outer contour

* five (U+0035) has a counter-clockwise outer contour

* four (U+0034) has a counter-clockwise outer contour

* four (U+0034) has a counter-clockwise outer contour

* four (U+0034) has a counter-clockwise outer contour

* four (U+0034) has a counter-clockwise outer contour

* nine (U+0039) has a counter-clockwise outer contour

* nine (U+0039) has a counter-clockwise outer contour

* nine (U+0039) has a counter-clockwise outer contour

* nine (U+0039) has a counter-clockwise outer contour

* nine (U+0039) has a counter-clockwise outer contour

* nine (U+0039) has a counter-clockwise outer contour

* one (U+0031) has a counter-clockwise outer contour

* one (U+0031) has a counter-clockwise outer contour

* parenright (U+0029) has a counter-clockwise outer contour

* parenright (U+0029) has a counter-clockwise outer contour

* parenright (U+0029) has a counter-clockwise outer contour

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

* uni0917 (U+0917) has a counter-clockwise outer contour

* uni0917 (U+0917) has a counter-clockwise outer contour

* uni0917 (U+0917) has a counter-clockwise outer contour

* uni0917 (U+0917) has a counter-clockwise outer contour

* uni0917 (U+0917) has a counter-clockwise outer contour

* x (U+0078) has a counter-clockwise outer contour

* x (U+0078) has a counter-clockwise outer contour

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
| 0 | 0 | 14 | 10 | 98 | 8 | 121 | 0 | 
| 0% | 0% | 6% | 4% | 39% | 3% | 48% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
