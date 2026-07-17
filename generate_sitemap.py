import os
from datetime import datetime

base_dir = os.path.dirname(os.path.abspath(__file__))
domain = "https://www.firstpartners.pl"

static_pages = {
    "": {"file": "index.html", "priority": "1.0", "changefreq": "weekly"},
    "growth-audit": {"file": "growth-audit.html", "priority": "0.8", "changefreq": "monthly"},
    "growth-system": {"file": "growth-system.html", "priority": "0.8", "changefreq": "monthly"},
    "partnerstwo": {"file": "partnerstwo.html", "priority": "0.8", "changefreq": "monthly"},
    "warszawa": {"file": "warszawa.html", "priority": "0.7", "changefreq": "monthly"},
    "gabinety-stomatologiczne": {"file": "gabinety-stomatologiczne.html", "priority": "0.7", "changefreq": "monthly"},
    "gabinety-medycyny-estetycznej": {"file": "gabinety-medycyny-estetycznej.html", "priority": "0.7", "changefreq": "monthly"},
    "kliniki-fizjoterapii": {"file": "kliniki-fizjoterapii.html", "priority": "0.7", "changefreq": "monthly"},
    "prywatne-przedszkola-szkoly": {"file": "prywatne-przedszkola-szkoly.html", "priority": "0.7", "changefreq": "monthly"},
    "kursy-online-high-ticket": {"file": "kursy-online-high-ticket.html", "priority": "0.7", "changefreq": "monthly"},
    "kancelarie-prawne": {"file": "kancelarie-prawne.html", "priority": "0.7", "changefreq": "monthly"},
    "b2b": {"file": "b2b.html", "priority": "0.7", "changefreq": "monthly"},
    "deweloperzy-boutique": {"file": "deweloperzy-boutique.html", "priority": "0.7", "changefreq": "monthly"},
    "butikowe-biura-nieruchomosci": {"file": "butikowe-biura-nieruchomosci.html", "priority": "0.7", "changefreq": "monthly"},
    "zarzadzanie-najmem-premium": {"file": "zarzadzanie-najmem-premium.html", "priority": "0.7", "changefreq": "monthly"},
    "polityka-prywatnosci": {"file": "polityka-prywatnosci.html", "priority": "0.3", "changefreq": "monthly"},
    "regulamin": {"file": "regulamin.html", "priority": "0.3", "changefreq": "monthly"},
    "blog": {"file": "blog.html", "priority": "0.8", "changefreq": "weekly"}
}

def generate():
    today = datetime.today().strftime('%Y-%m-%d')
    urls = []
    
    # 1. Add static root and subpages
    for route, meta in static_pages.items():
        filepath = os.path.join(base_dir, meta["file"])
        lastmod = today
        if os.path.exists(filepath):
            mtime = os.path.getmtime(filepath)
            lastmod = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
        
        urls.append(f"  <url>\n    <loc>{domain}/{route}</loc>\n    <lastmod>{lastmod}</lastmod>\n    <changefreq>{meta['changefreq']}</changefreq>\n    <priority>{meta['priority']}</priority>\n  </url>")

    # 2. Add blog posts dynamically
    blog_dir = os.path.join(base_dir, "blog")
    if os.path.exists(blog_dir):
        for filename in os.listdir(blog_dir):
            if filename.endswith(".html") and filename != "template.html":
                slug = os.path.splitext(filename)[0]
                filepath = os.path.join(blog_dir, filename)
                mtime = os.path.getmtime(filepath)
                lastmod = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
                urls.append(f"  <url>\n    <loc>{domain}/blog/{slug}</loc>\n    <lastmod>{lastmod}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>")

    # Build XML structure
    urls_joined = "\n".join(urls)
    xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls_joined}
</urlset>
"""
    sitemap_path = os.path.join(base_dir, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(xml_content)
    print(f"Successfully generated sitemap.xml with {len(urls)} URLs.")

if __name__ == "__main__":
    generate()
