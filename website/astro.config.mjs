// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
	integrations: [
		starlight({
			title: 'Materiały z Informatyki',
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/JaBabiar/TEB.TOR.25-26.S2' }],
			sidebar: [
				{
					label: 'TEB Toruń - Semestr Letni',
					// ZMIANA JEST TUTAJ: autogenerate ląduje wewnątrz tablicy items
					items: [
						{ autogenerate: { directory: 'TEB.TOR.25-26.S2' } }
					]
				},
			],
		}),
	],
});