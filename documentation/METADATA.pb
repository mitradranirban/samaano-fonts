name: "Samaano"
designer: "Anirban Mitra"
license: "OFL"
category: "SLAB_SERIF"
date_added: "2024-11-08"
fonts {
  name: "Samaano"
  style: "bold"
  weight: 700
  filename: "Samaano[slnt,wdth,wght].ttf"
  post_script_name: "Samaano-Bold"
  full_name: "Samaano Bold"
  copyright: "Copyright 2024 The Samaano Project Authors (https://github.com/mitradranirban/samaano-fonts)"
}
source {
  repository_url: "https://github.com/mitradranirban/samaano-fonts"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Samaano[slnt,wdth,wght].ttf"
    dest_file: "Samaano[slnt,wdth,wght].ttf"
  }
  files {
    source_file: "documentation/ARTICLE.en_us.html"
    dest_file: "ARTICLE.en_us.html"
  }
  
    branch: "main"
}
subsets: "devanagari"
subsets: "latin"
subsets: "latin-ext"
subsets: "menu"
subsets: "vietnamese"
axes {
  tag: "slnt"
  min_value: -20.0
  max_value: 0.0
}
axes {
  tag: "wdth"
  min_value: 100.0
  max_value: 200.0
}
axes {
  tag: "wght"
  min_value: 100.0
  max_value: 700.0
}
primary_script: "Deva"
