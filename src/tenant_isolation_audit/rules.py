from __future__ import annotations

from tenant_isolation_audit.models import Rule

PROJECT_NAME = 'tenant-isolation-audit'
SUMMARY = 'Review multi-tenant design notes for isolation and access-control gaps.'
SAMPLE_RISK = 'query all accounts tenant_filter missing shared bucket access_test none'
SAMPLE_CLEAN = (
                   'query accounts tenant_filter required bucket per-tenant access_test cros'
                   's-tenant denied'
               )
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "endpoint", "service", "job", "route", "event")

RULES = (
    Rule(
        code='missing-tenant-filter',
        severity='high',
        pattern='\\btenant_filter\\s*(missing|none|null)\\b',
        message='tenant filter is missing',
        recommendation='Require tenant predicate on all scoped data access.',
    ),
    Rule(
        code='shared-resource',
        severity='medium',
        pattern='\\bshared bucket|shared database|shared index\\b',
        message='shared resource detected',
        recommendation='Document isolation controls and access policies.',
    ),
    Rule(
        code='missing-access-test',
        severity='low',
        pattern='\\baccess_test\\s*(none|missing|null)\\b',
        message='cross-tenant access test is missing',
        recommendation='Add tests for denied cross-tenant access.',
    ),
)
