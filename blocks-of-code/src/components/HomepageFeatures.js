import React from 'react';
import clsx from 'clsx';
import styles from './HomepageFeatures.module.css';

const FeatureList = [
  {
    title: 'Especificações',
    Svg: require('../../static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <>
        <a href="https://www.blender.org/support/tutorials/">Blender Tutorials</a><br />
        <a href="https://docs.blender.org/api/current/">Blender APIs</a><br />
        <a href="https://wiki.blender.org/wiki/Main_Page">Blender for Developers</a><br />
        <a href="https://docs.python.org/3/">Python Especification</a><br />
      </>
    ),
  },
  {
    title: 'Instrução',
    Svg: require('../../static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
        Alura ...
      </>
    ),
  },
  {
    title: 'Comunidade',
    Svg: require('../../static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        <a href="https://br.pinterest.com/">Pinterest</a><br />
        <a href="https://www.artstation.com/">ArtStation</a><br />
        <a href="https://www.instagram.com/">Instagram</a>
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} alt={title} />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
