// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import { unified } from '@astrojs/markdown-remark';
import remarkMath from 'remark-math';
import rehypeMathRaw from './src/plugins/rehype-math-raw.mjs';

// https://astro.build/config
export default defineConfig({
  site: 'https://vishwadarpan.com',
  integrations: [mdx()],
  markdown: {
    processor: unified({
      remarkPlugins: [remarkMath],
      rehypePlugins: [rehypeMathRaw],
    }),
  },
});
