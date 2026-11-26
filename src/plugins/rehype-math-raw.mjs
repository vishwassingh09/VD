import { visit } from 'unist-util-visit';

/**
 * Preserves remark-math inline and display math blocks as plain LaTeX text
 * inside semantic elements so client-side MathJax 3 (including [tex]/physics)
 * renders them cleanly without Markdown or MDX mangling underscores or braces.
 */
export default function rehypeMathRaw() {
  return (tree) => {
    visit(tree, 'element', (node, index, parent) => {
      if (!parent || typeof index !== 'number') return;

      // Display math: <pre><code class="language-math math-display">...</code></pre>
      if (node.tagName === 'pre' && Array.isArray(node.children) && node.children.length === 1) {
        const codeNode = node.children[0];
        const classes = codeNode?.properties?.className;
        if (
          codeNode?.type === 'element' &&
          codeNode.tagName === 'code' &&
          Array.isArray(classes) &&
          classes.includes('math-display')
        ) {
          const tex = extractText(codeNode).trim();
          parent.children[index] = {
            type: 'element',
            tagName: 'div',
            properties: {
              className: ['math-display'],
              style: 'text-align: center; font-size: 1.2em; margin: 1em 0; overflow-x: auto;',
            },
            children: [{ type: 'text', value: `$$${tex}$$` }],
          };
          return;
        }
      }

      // Inline math: <code class="language-math math-inline">...</code>
      const classes = node.properties?.className;
      if (
        node.tagName === 'code' &&
        Array.isArray(classes) &&
        classes.includes('math-inline')
      ) {
        const tex = extractText(node).trim();
        parent.children[index] = {
          type: 'element',
          tagName: 'span',
          properties: { className: ['math-inline'] },
          children: [{ type: 'text', value: `$${tex}$` }],
        };
      }
    });
  };
}

function extractText(node) {
  if (!node) return '';
  if (node.type === 'text') return node.value || '';
  if (Array.isArray(node.children)) {
    return node.children.map(extractText).join('');
  }
  return '';
}
