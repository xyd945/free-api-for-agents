'use client';

import { useState } from 'react';
import styles from './page.module.css';

export default function Home() {
  const [copied, setCopied] = useState(false);

  const promptText = `Hey! We are working in a repository that contains a massive directory of free, public, no-auth APIs. To understand how to find and use these APIs to fetch live data, please read the \`free_public_apis/SKILL.md\` file first. It acts as your primary instruction manual and contains a table of contents to all the available API categories.`;

  const handleCopy = () => {
    navigator.clipboard.writeText(promptText);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <main className={styles.container}>
      <section className={styles.hero}>
        <h1 className={styles.title}>Free APIs for AI Agents 🤖⚙️</h1>
        <p className={styles.subtitle}>
          A massive, zero-dependency directory of 100% Free, No-Auth, HTTPS public APIs. Built to give your AI Agents and LLMs reliable real-time web capabilities.
        </p>

        <div className={styles.promptContainer}>
          <div className={styles.promptHeader}>
            <span>🚀 Quick Start for Agents</span>
            <button className={styles.copyButton} onClick={handleCopy}>
              {copied ? 'Copied!' : 'Copy Prompt'}
            </button>
          </div>
          <div className={styles.promptText}>
            "{promptText}"
          </div>
        </div>
      </section>

      <section className={styles.stats}>
        <div className={styles.statCard}>
          <div className={styles.statNumber}>1000+</div>
          <div className={styles.statLabel}>Free Public APIs</div>
        </div>
        <div className={styles.statCard}>
          <div className={styles.statNumber}>47</div>
          <div className={styles.statLabel}>Data Categories</div>
        </div>
        <div className={styles.creditText}>
          Based on the legendary <a href="https://github.com/public-apis/public-apis" target="_blank" rel="noopener noreferrer">public-apis</a> repository (400k+ GitHub Stars ⭐). Restructured and optimized for AI context limits.
        </div>
      </section>

      <section className={styles.examplesSection}>
        <h2 className={styles.sectionTitle}>Agent Build Examples</h2>
        <div className={styles.grid}>
          
          <div className={styles.card}>
            <div className={styles.cardHeader}>
              <h3 className={styles.cardTitle}>🎭 Daily Wisdom & Fun Dashboard</h3>
              <p className={styles.cardDescription}>
                A Python script built by an agent pulling from 5 different entertainment APIs concurrently.
              </p>
            </div>
            <div className={styles.terminal}>
              <div className={styles.terminalHeader}>
                <div className={`${styles.dot} ${styles.dotRed}`}></div>
                <div className={`${styles.dot} ${styles.dotYellow}`}></div>
                <div className={`${styles.dot} ${styles.dotGreen}`}></div>
              </div>
              {`Fetching your Daily Wisdom & Fun Dashboard...
--------------------------------------------------

==================================================
🌟 TODAY'S WISDOM & FUN DASHBOARD 🌟
==================================================

🤔 DID YOU KNOW?
"Honey is the only food which does not spoil."

💡 ADVICE OF THE DAY:
"Share positive energy."

🎤 KANYE WEST SAYS:
"Trust me ... I won't stop"
`}
            </div>
          </div>

          <div className={styles.card}>
            <div className={styles.cardHeader}>
              <h3 className={styles.cardTitle}>📊 Executive Market Dashboard</h3>
              <p className={styles.cardDescription}>
                A serious script querying the European Central Bank, CoinGecko, and the U.S. Treasury.
              </p>
            </div>
            <div className={styles.terminal}>
              <div className={styles.terminalHeader}>
                <div className={`${styles.dot} ${styles.dotRed}`}></div>
                <div className={`${styles.dot} ${styles.dotYellow}`}></div>
                <div className={`${styles.dot} ${styles.dotGreen}`}></div>
              </div>
              {`Fetching Global Economic Dashboard...
--------------------------------------------------

==================================================
📊 EXECUTIVE MARKET DASHBOARD 
==================================================

💱 FOREIGN EXCHANGE (1 USD)
- EUR: 0.86603
- JPY: 158.86

🪙 CRYPTOCURRENCY MARKETS
- Bitcoin (BTC) : $71,674
- Ethereum (ETH): $2,103.28

🇺🇸 U.S. NATIONAL DEBT
- Total Outstanding: $38.88 Trillion
`}
            </div>
          </div>

        </div>
      </section>
    </main>
  );
}
