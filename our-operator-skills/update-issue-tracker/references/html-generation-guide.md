# HTML Report Generation Guide

This guide shows how to generate an HTML report from a markdown issue reproduction report.

## Step-by-Step Process

### 1. Read the Template

```bash
Read issue_tracker/templates/issue_report_template.html
```

### 2. Read the Markdown Report

```bash
Read discussion_reports/bug/issue_XXXX_*.md
```

### 3. Extract Key Information

From the markdown, extract:
- Issue ID (from file name or content)
- Issue title (from Target section or Purpose line)
- GitHub URL
- Environment (host, container, model)
- Status (from Conclusion section)
- Progress (count completed steps)

### 4. Convert Each Section

For each markdown section, create HTML:

```html
<section class="panel">
  <h2>Section Title</h2>
  <div class="content">
    <!-- Convert markdown content to HTML -->
  </div>
</section>
```

### 5. Replace Template Placeholders

In the template HTML, replace:
- `{{issue_id}}` → actual issue ID
- `{{issue_title}}` → actual title
- `{{host}}` → actual host
- `{{container}}` → actual container
- `{{generated_date}}` → today's date
- `{{status}}` → actual status text
- `{{status_class}}` → CSS class name
- `{{completed_steps}}` → actual count
- `{{total_steps}}` → 7
- `{{progress_percentage}}` → calculated percentage
- `{{sections}}` → all section HTML

### 6. Write the HTML File

```bash
Write discussion_reports/bug/issue_XXXX_{{slug}}.html
```

## Conversion Examples

### Bullet Lists

**Markdown:**
```markdown
- Version: `vLLM 0.18.0rc1`
- Topology: PD disaggregation with Mooncake
```

**HTML:**
```html
<ul>
  <li>Version: <code>vLLM 0.18.0rc1</code></li>
  <li>Topology: PD disaggregation with Mooncake</li>
</ul>
```

### Code Blocks

**Markdown:**
````markdown
```bash
curl http://127.0.0.1:13800/v1/models
```
````

**HTML:**
```html
<pre><code>curl http://127.0.0.1:13800/v1/models</code></pre>
```

### Links

**Markdown:**
```markdown
See [GitHub issue](https://github.com/vllm-project/vllm-ascend/issues/7985)
```

**HTML:**
```html
See <a href="https://github.com/vllm-project/vllm-ascend/issues/7985">GitHub issue</a>
```

### Tables

**Markdown:**
```markdown
| Case | Model | Result |
|------|-------|--------|
| 1    | Qwen  | Passed |
```

**HTML:**
```html
<table>
  <thead>
    <tr>
      <th>Case</th>
      <th>Model</th>
      <th>Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Qwen</td>
      <td>Passed</td>
    </tr>
  </tbody>
</table>
```

## Complete Example

### Input Markdown (excerpt)

```markdown
# Target

- Issue: [#7985](https://github.com/vllm-project/vllm-ascend/issues/7985)
- Purpose: Reproduce the PD-disaggregation failure

# Local Environment

- Host: `npu4`
- Container: `vllm_qwen3`
- Date: `2026-04-23`

# Conclusion

The issue was **blocked** by a Mooncake transfer failure.
```

### Output HTML (excerpt)

```html
<section class="panel">
  <h2>Target</h2>
  <div class="content">
    <ul>
      <li>Issue: <a href="https://github.com/vllm-project/vllm-ascend/issues/7985">#7985</a></li>
      <li>Purpose: Reproduce the PD-disaggregation failure</li>
    </ul>
  </div>
</section>

<section class="panel">
  <h2>Local Environment</h2>
  <div class="content">
    <ul>
      <li>Host: <code>npu4</code></li>
      <li>Container: <code>vllm_qwen3</code></li>
      <li>Date: <code>2026-04-23</code></li>
    </ul>
  </div>
</section>

<section class="panel">
  <h2>Conclusion</h2>
  <div class="content">
    <p>The issue was <strong>blocked</strong> by a Mooncake transfer failure.</p>
  </div>
</section>
```

## Status Class Mapping

| JSON Status | CSS Class    | Display Text |
|-------------|---------------|--------------|
| completed   | completed     | completed    |
| blocked     | blocked       | blocked      |
| in_progress | in_progress   | in progress  |
| not_started | (default)     | not started  |

## Tips

1. **Preserve exact paths**: Keep file paths exactly as they appear in markdown
2. **Use code tags**: Wrap file paths, commands, and values in `<code>` tags
3. **Maintain structure**: Keep the section order from the markdown
4. **Check links**: Verify all links work correctly
5. **Validate dates**: Use YYYY-MM-DD format for display dates
