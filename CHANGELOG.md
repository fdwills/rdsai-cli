# Changelog

All notable changes to RDSAI CLI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Agent effectiveness optimization
- Interactive experience improvements
- Security enhancements
- Diagnostic report export

## [v0.1.1] - 2025-12-17

### Added
- Initial public release
- **AI-powered MySQL assistant** with natural language support (English/中文)
- **14+ diagnostic tools**:
  - TableStructure, TableIndex, TableStatus
  - MySQLExplain, SlowLog, ShowProcess
  - InnodbStatus, Transaction
  - InformationSchema, PerformanceSchema, PerfStatistics
  - KernelParameter, ReplicaStatus
  - DDLExecutor
- **Multi-LLM support**: Qwen, OpenAI, DeepSeek, Anthropic, Gemini, OpenAI-compatible
- **Model management**: Switch models via `/model` command
- **Memory system**: Schema learning and context persistence
- **Interactive TUI shell** with Rich formatting
- **Smart SQL detection**: Auto-detect SQL vs natural language
- **SQL completer**: Intelligent SQL autocomplete with schema awareness
- **Query history**: Track and review SQL execution history via `/history`
- **Database Schema Analysis** (`/research`): Comprehensive schema analysis reports with AI-powered review, index optimization suggestions, compliance checking against Alibaba Database Development Standards
- **Performance Benchmarking** (`/benchmark`): AI-powered sysbench performance testing with automated workflow (prepare → run → cleanup) and comprehensive analysis reports
- **MCP Integration**: Extend capabilities by connecting to external MCP servers, including Alibaba Cloud RDS OpenAPI for cloud RDS instance management
- **Instant SQL Result Explanation**: Press `Ctrl+E` after any SQL query to get AI-powered explanations of results or errors
  - Dedicated explain agent for SQL result analysis
  - Automatic hint display after query execution (`💡 Ctrl+E: Explain result` or `💡 Ctrl+E: Explain error`)
  - Supports both successful queries and error messages
  - Concise, actionable explanations in user's configured language (English/中文)
  - Works seamlessly with query history and context injection
- **Safety features**: Read-only default, DDL/DML confirmation
- **YOLO mode**: Auto-approve for trusted environments
- **SSL/TLS support**: Full SSL configuration options (CA, client cert, key, mode)
- **Transaction safety**: Warnings for uncommitted transactions on exit
- `/setup` wizard for LLM configuration
- `/init` and `/memory` for knowledge management
- `/connect` and `/disconnect` for database connection management
- Vertical format support (`\G`) for SQL results
- Keyboard shortcuts:
  - `Ctrl+E`: Explain SQL result
  - `Ctrl+J`: Insert newline
  - `Ctrl+C`: Exit/interrupt
  - `Tab`: Toggle thinking mode (when buffer is empty)

### Security
- Read-only mode by default
- Explicit confirmation for all write operations
- Transaction safety warnings on exit
- Credential storage in `~/.rdsai-cli/config.json` with proper OS permissions

---

[Unreleased]: https://github.com/aliyun/rdsai-cli/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/aliyun/rdsai-cli/releases/tag/v0.1.1
