for dir in ~/Desktop/share/zeitraum/Presentation_HTML/*; do (echo "processing $dir" && cd "$dir" && pandoc -s content_de.md -o content_de.html && pandoc -s content_en.md -o content_en.html && pandoc -s content_nl.md -o content_nl.html); done


