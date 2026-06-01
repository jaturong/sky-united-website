const SkyI18n = {
  defaultLanguage: "th",
  supportedLanguages: ["en", "th"],
  currentLanguage: "th",
  translations: {},
};

SkyI18n.getPathPrefix = () => {
  const path = window.location.pathname;
  return path.includes("/products/") || path.includes("/news/") ? "../" : "";
};

SkyI18n.getNestedValue = (source, path) => {
  return path.split(".").reduce((value, key) => {
    if (Array.isArray(value) && Number.isInteger(Number(key))) {
      return value[Number(key)];
    }

    if (value && Object.prototype.hasOwnProperty.call(value, key)) {
      return value[key];
    }

    return undefined;
  }, source);
};

SkyI18n.loadLanguage = async (language) => {
  const safeLanguage = SkyI18n.supportedLanguages.includes(language)
    ? language
    : SkyI18n.defaultLanguage;

  if (SkyI18n.translations[safeLanguage]) {
    return SkyI18n.translations[safeLanguage];
  }

  const response = await fetch(`${SkyI18n.getPathPrefix()}lang/${safeLanguage}.json`);

  if (!response.ok) {
    throw new Error(`Unable to load language: ${safeLanguage}`);
  }

  const translations = await response.json();
  SkyI18n.translations[safeLanguage] = translations;
  return translations;
};

SkyI18n.applyLanguage = async (language) => {
  const translations = await SkyI18n.loadLanguage(language);

  document.querySelectorAll("[data-i18n]").forEach((element) => {
    const key = element.dataset.i18n;
    const value = SkyI18n.getNestedValue(translations, key);

    if (typeof value === "string") {
      element.textContent = value;
    }
  });

  document.querySelectorAll("[data-i18n-attr]").forEach((element) => {
    const mappings = element.dataset.i18nAttr.split(",");

    mappings.forEach((mapping) => {
      const [attribute, key] = mapping.split(":").map((part) => part.trim());
      const value = SkyI18n.getNestedValue(translations, key);

      if (attribute && typeof value === "string") {
        element.setAttribute(attribute, value);
      }
    });
  });

  SkyI18n.currentLanguage = language;
  document.documentElement.lang = language;
  document.documentElement.dataset.lang = language;
  localStorage.setItem("skyUnitedLanguage", language);

  const toggle = document.querySelector("[data-language-toggle]");

  if (toggle) {
    toggle.textContent = language === "th" ? "EN" : "TH";
    toggle.setAttribute(
      "aria-label",
      language === "th" ? "Switch language to English" : "เปลี่ยนภาษาเป็นไทย"
    );
  }
};

SkyI18n.init = async () => {
  // Force Thai as default for now
  localStorage.setItem("skyUnitedLanguage", "th");

  const storedLanguage = localStorage.getItem("skyUnitedLanguage");
  const initialLanguage = SkyI18n.supportedLanguages.includes(storedLanguage)
    ? storedLanguage
    : SkyI18n.defaultLanguage;

  try {
    await SkyI18n.applyLanguage(initialLanguage);
  } catch (error) {
    console.warn(error);
  }

  const toggle = document.querySelector("[data-language-toggle]");
  console.log("Language toggle button found:", toggle);

  if (toggle) {
    toggle.addEventListener("click", async () => {
      const nextLanguage = SkyI18n.currentLanguage === "th" ? "en" : "th";
      console.log("Switching language to:", nextLanguage);
      await SkyI18n.applyLanguage(nextLanguage);
    });
  }
};

document.addEventListener("DOMContentLoaded", SkyI18n.init);
