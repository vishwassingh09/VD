import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const physics = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/physics' }),
  schema: z.object({
    title: z.string(),
    tab: z.enum(['introduction', 'school', 'college', 'research', 'exercises', 'notes']),
    sectionId: z.string(),
    group: z.string().optional(),
    order: z.number().default(100),
    sidebarLabel: z.string().optional(),
    isIntro: z.boolean().default(false),
    highlight: z.boolean().default(false),
  }),
});

export const collections = { physics };
