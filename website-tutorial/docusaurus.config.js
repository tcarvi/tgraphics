const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** @type {import('@docusaurus/types').DocusaurusConfig} */
module.exports = {
  title: 'Instruções Blender',
  tagline: 'blender',
  url: 'http://tcarvi.com.br',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'tcarvi', // Usually your GitHub org/user name.
  projectName: 'blocks-of-blender', // Usually your repo name.
  customFields: {
    mainButtonText: 'Comece a desenvolver arte',
  },
  themeConfig: {
    navbar: {
      title: 'Modelagem e Animação com Blender',
      logo: {
        alt: 'My Site Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'doc',
          docId: 'comandos/visualizar',
          position: 'left',
          label: 'Tutorial',
        },
        {
          href: 'https://github.com/tcarvi/tgraphics',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      copyright: `TCARVI: Blocks of Code. Licensa GNU. ${new Date().getFullYear()}`,
    },
    prism: {
      theme: lightCodeTheme,
      darkTheme: darkCodeTheme,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl:
            'https://github.com/tcarvi/tgraphics/blob/master/blocks-of-code/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
