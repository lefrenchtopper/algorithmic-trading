from django.contrib import admin
from portfolio_app.models import Portfolio, Position, Trade, PerformanceMetric


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "initial_cash",
        "current_cash",
        "total_value",
        "is_active",
        "created_at",
    )
    list_filter = ("is_active", "created_at")
    search_fields = ("name", "description")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = (
        "portfolio",
        "stock",
        "quantity",
        "average_cost",
        "current_price",
        "current_value",
        "unrealized_pnl",
        "last_updated",
    )
    list_filter = ("portfolio", "stock")
    search_fields = ("portfolio__name", "stock__ticker")
    readonly_fields = ("created_at", "last_updated")


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = (
        "portfolio",
        "stock",
        "trade_type",
        "quantity",
        "price",
        "filled_quantity",
        "status",
        "created_at",
    )
    list_filter = ("trade_type", "status", "created_at")
    search_fields = (
        "portfolio__name",
        "stock__ticker",
        "external_order_id",
        "external_trade_id",
    )
    readonly_fields = ("created_at", "submitted_at", "filled_at")


@admin.register(PerformanceMetric)
class PerformanceMetricAdmin(admin.ModelAdmin):
    list_display = (
        "portfolio",
        "date",
        "total_value",
        "cash_value",
        "positions_value",
        "daily_return",
        "cumulative_return",
    )
    list_filter = ("date", "portfolio")
    search_fields = ("portfolio__name",)
    readonly_fields = ("created_at",)
    date_hierarchy = "date"
