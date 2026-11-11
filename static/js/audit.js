document.addEventListener('DOMContentLoaded', () => {
  const radios = document.querySelectorAll('.option-radio');
  if (!radios.length) return;

  const progressBar  = document.getElementById('progressBar');
  const progressLbl  = document.getElementById('progressLabel');
  const submitBtn    = document.getElementById('submitBtn');
  const submitHint   = document.getElementById('submitHint');
  const hintText     = document.getElementById('hintText');

  // Track answered questions per category
  const answered    = {};  // qid -> value
  const catAnswered = {};  // catId -> Set of qids answered

  function getScore(catId) {
    const qs = document.querySelectorAll(`.option-radio[data-cat="${catId}"]`);
    let total = 0, max = 0;
    const seen = new Set();
    qs.forEach(r => {
      if (!seen.has(r.name)) {
        seen.add(r.name);
        const opts = document.querySelectorAll(`input[name="${r.name}"]`);
        const maxVal = Math.max(...[...opts].map(o => parseInt(o.value)));
        max += maxVal;
      }
      if (r.checked) total += parseInt(r.value);
    });
    return max > 0 ? Math.round(total / max * 100) : 0;
  }

  function updateProgress() {
    const allQids = new Set([...radios].map(r => r.name));
    const answeredQids = new Set([...radios].filter(r => r.checked).map(r => r.name));
    const count = answeredQids.size;
    const total = allQids.size;

    const pct = total > 0 ? (count / total * 100) : 0;
    progressBar.style.width = pct + '%';
    progressLbl.textContent = `${count} / ${total} questions répondues`;

    const remaining = total - count;
    if (remaining === 0) {
      submitBtn.disabled = false;
      submitHint.classList.add('ready');
      hintText.textContent = '✅ Toutes les questions sont complétées. Vous pouvez voir vos résultats !';
    } else {
      submitBtn.disabled = true;
      submitHint.classList.remove('ready');
      hintText.textContent = `${remaining} question(s) restante(s) avant de voir vos résultats.`;
    }
  }

  function updateCatBadge(catId) {
    const badge = document.getElementById(`badge-${catId}`);
    if (!badge) return;
    const score = getScore(catId);
    badge.textContent = score + '%';
    badge.style.background =
      score >= 75 ? '#27AE60' :
      score >= 50 ? '#E67E22' : '#E74C3C';
  }

  radios.forEach(radio => {
    radio.addEventListener('change', () => {
      const qid   = radio.dataset.qid;
      const catId = radio.dataset.cat;

      // Mark question card as answered
      const card = document.getElementById(`qcard-${qid}`);
      if (card) card.classList.add('answered');

      updateCatBadge(catId);
      updateProgress();
    });
  });

  updateProgress();
});
