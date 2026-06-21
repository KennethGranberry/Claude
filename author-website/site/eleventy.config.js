// Eleventy configuration — KennethGranberry.com
// Content-first static site. No manuscript content is fetched or sent anywhere;
// the build operates only on the files in this repo.

export default function (eleventyConfig) {
  // Pass CSS and static assets straight through.
  eleventyConfig.addPassthroughCopy({ "src/css": "css" });
  eleventyConfig.addPassthroughCopy({ "src/assets": "assets" });

  // Current year, for the footer.
  eleventyConfig.addShortcode("year", () => `${new Date().getFullYear()}`);

  return {
    dir: {
      input: "src",
      output: "_site",
      includes: "_includes",
      data: "_data",
    },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
    templateFormats: ["njk", "md", "html"],
  };
}
