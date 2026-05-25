const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1280, height: 800 });

  const sections = [
    { name: 'accueil_hero', url: 'http://localhost:8000/index.html', selector: '.hero' },
    { name: 'accueil_features', url: 'http://localhost:8000/index.html', selector: '.features' },
    { name: 'accueil_specialties', url: 'http://localhost:8000/index.html', selector: '.specialties' },
    { name: 'accueil_gallery', url: 'http://localhost:8000/index.html', selector: '.gallery' },
    { name: 'accueil_reviews', url: 'http://localhost:8000/index.html', selector: '.reviews' },
    { name: 'accueil_map', url: 'http://localhost:8000/index.html', selector: '.map-section' },

    { name: 'menu_hero', url: 'http://localhost:8000/menu.html', selector: '.page-hero' },
    { name: 'menu_infinite', url: 'http://localhost:8000/menu.html', selector: '.menu-infinite' },
    { name: 'menu_full', url: 'http://localhost:8000/menu.html', selector: '.menu-full' },

    { name: 'apropos_hero', url: 'http://localhost:8000/apropos.html', selector: '.page-hero' },
    { name: 'apropos_history', url: 'http://localhost:8000/apropos.html', selector: '.about-hero' },
    { name: 'apropos_values', url: 'http://localhost:8000/apropos.html', selector: '.values-grid' },
    { name: 'apropos_story', url: 'http://localhost:8000/apropos.html', selector: '.story' },

    { name: 'evenement_hero', url: 'http://localhost:8000/evenement.html', selector: '.page-hero' },
    { name: 'evenement_list', url: 'http://localhost:8000/evenement.html', selector: '.events-grid' },
    { name: 'evenement_regular', url: 'http://localhost:8000/evenement.html', selector: '.values-grid' },

    { name: 'contact_hero', url: 'http://localhost:8000/contact.html', selector: '.page-hero' },
    { name: 'contact_form', url: 'http://localhost:8000/contact.html', selector: '.reservation-form' }
  ];

  if (!fs.existsSync('screenshots')) {
    fs.mkdirSync('screenshots');
  }

  for (const section of sections) {
    console.log(`Capturing ${section.name}...`);
    try {
        await page.goto(section.url);
        await page.waitForTimeout(2000);

        await page.evaluate(() => {
            const header = document.querySelector('.header');
            if (header) header.style.display = 'none';
        });

        const element = await page.$(section.selector);
        if (element) {
          await element.screenshot({ path: `screenshots/${section.name}.png` });
        } else {
          console.error(`Selector ${section.selector} not found on ${section.url}`);
        }
    } catch (e) {
        console.error(`Error capturing ${section.name}: ${e.message}`);
    }
  }

  await browser.close();
})();
