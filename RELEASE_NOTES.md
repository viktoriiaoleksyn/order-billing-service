# Release Notes – order-billing-service v1.1.0

## [v1.1.0] – 2026-11-20

### Added
- Додано спеціальний базовий тариф 80.0 UAH для міста Kyiv.
- Додано явний параметр ставки податку `tax_rate` (зі значенням за замовчуванням 0.20) до функції `process_standard_invoice`.

### Changed
- Коефіцієнт доставки за вагу збільшено з 12.0 до 15.0 UAH/кг.
- Здійснено повний архітектурний рефакторинг модуля: виконано перехід від Common, Control та Stamp Coupling до еталонного **Data Coupling**.

### Breaking Changes
- Змінено сигнатури функцій розрахунку.
- Видалено глобальну змінну `GLOBAL_TAX_RATE`.
- Видалено керуючий прапорець `mode_flag` та замінено його на дві окремі функції (`process_standard_invoice` та `process_tax_exempt_invoice`).
