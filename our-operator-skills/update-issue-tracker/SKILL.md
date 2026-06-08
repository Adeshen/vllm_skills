---
name: update-issue-tracker
description: Update the issue tracker JSON state and generate HTML report for a completed issue reproduction step. Use when finishing an issue reproduction step or completing a full report.
---

# Update Issue Tracker

When completing issue reproduction work, update the tracker state and generate reports directly.

## When to Use

- After completing a reproduction step (1-7)
- After writing or updating a markdown report in `discussion_reports/bug/`
- When asked to generate an HTML report
- When asked to update issue progress

## Workflow

### 1. Update JSON State

Always update `issue_tracker/data/issues.json` when completing work:

```json
{
  "issues": [
    {
      "id": "7985",
      "url": "https://github.com/vllm-project/vllm-ascend/issues/7985",
      "title": "Issue title here",
      "status": "in_progress",  // or: not_started, completed, blocked
      "priority": "high",  // or: medium, low
      "reproduction_result": "blocked",  // or: reproduced, approximately_reproduced, not_reproduced
      "created_at": "2026-04-20T10:00:00Z",
      "updated_at": "2026-04-27T21:30:00Z",
      "steps": [
        {
          "step_id": 1,
          "name": "GitHub Issue 获取与解析",
          "status": "completed",  // or: pending, in_progress, skipped, blocked
          "completed_at": "2026-04-23T10:00:00Z",
          "agent": "claude",  // or: codex
          "notes": "Brief note about what was done",
          "artifacts": ["path/to/file.md", "path/to/file.json"]
        }
        // ... repeat for all 7 steps
      ],
      "metadata": {
        "created_at": "2026-04-23T09:00:00Z",
        "last_modified": "2026-04-23T19:00:00Z",
        "total_steps": 7,
        "completed_steps": 6,
        "skipped_steps": 1,
        "progress_percentage": 85.7
      },
      "report_path": "discussion_reports/bug/issue_7985_*.md",
      "html_report_path": "discussion_reports/bug/issue_7985_*.html",
      "tags": ["pd-disaggregation", "mooncake", "keyerror"],
      "environment": {
        "host": "npu4",
        "container": "vllm_qwen3",
        "model": "Qwen3.5-9B"
      }
    }
  ],
  "summary": {
    "total_issues": 1,
    "by_status": {
      "not_started": 0,
      "in_progress": 0,
      "completed": 0,
      "blocked": 1
    },
    "by_priority": {
      "high": 1,
      "medium": 0,
      "low": 0
    },
    "by_reproduction_result": {
      "reproduced": 0,
      "approximately_reproduced": 0,
      "not_reproduced": 0,
      "blocked": 1
    }
  },
  "version": "1.0",
  "last_updated": "2026-04-27T21:30:00Z"
}
```

### 2. Generate HTML Report

When generating an HTML report:

1. **Read the template**: `issue_tracker/templates/issue_report_template.html`

2. **Replace placeholders**:
   - `{{issue_id}}` → Issue number
   - `{{issue_title}}` → Issue title
   - `{{host}}` → Environment host
   - `{{container}}` → Environment container
   - `{{generated_date}}` → Current date (YYYY-MM-DD)
   - `{{status}}` → Status (blocked, completed, etc.)
   - `{{status_class}}` → CSS class (blocked, completed, in_progress)
   - `{{completed_steps}}` → Number of completed steps
   - `{{total_steps}}` → Total steps (7)
   - `{{progress_percentage}}` → Progress percentage
   - `{{sections}}` → HTML content from markdown sections

3. **Convert markdown sections to HTML**:
   - Read the markdown report sections
   - Convert each section to HTML using this format:
   ```html
   <section class="panel">
     <h2>Section Title</h2>
     <div class="content">
       [Content with proper HTML formatting]
     </div>
   </section>
   ```

4. **Save the HTML file** to `discussion_reports/bug/issue_{{id}}_{{slug}}.html`

## Section Conversion Guide

| Markdown | HTML |
|----------|------|
| `# Heading` | `<h2>Heading</h2>` |
| `## Subheading` | `<h3>Subheading</h3>` |
| `- Item` | `<li>Item</li>` inside `<ul>` |
| `` `code` `` | `<code>code</code>` |
| ` ```language\ncode\n``` ` | `<pre><code>code</code></pre>` |
| `**bold**` | `<strong>bold</strong>` |
| `[text](url)` | `<a href="url">text</a>` |
| `- Item: \`value\`` | `<li>Item: <code>value</code></li>` |

## Standard Sections

Include these sections in the HTML (in order):

1. **Target** - Issue link and purpose
2. **Original Conditions** - Original environment and failure signature
3. **Local Environment** - Local test environment
4. **Experiment Matrix** - Test cases table
5. **Key Findings** - Detailed findings (can have subsections)
6. **Representative Logs** - Important log snippets
7. **Conclusion** - Final status and summary
8. **Next Steps** - Follow-up actions

## Quality Checklist

Before finishing:
- [ ] JSON is valid (use `cat issues.json | python3 -m json.tool` to verify)
- [ ] HTML has valid structure
- [ ] All placeholders replaced
- [ ] Sections match the markdown report
- [ ] Status and progress are accurate
- [ ] Artifact paths are correct
- [ ] Date format is ISO 8601 for JSON, YYYY-MM-DD for HTML display
