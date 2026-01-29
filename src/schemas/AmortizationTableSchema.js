import { z } from "zod"

export const AmortizationPeriodSchema = z.object({
    actual_period: z.number().int().nonnegative(),
    period_payment_amount: z.number().nonnegative(),
    interest_monthly_rate: z.number().nonnegative(),
    period_interest_amount: z.number().nonnegative(),
    capital_period_amortization_amount: z.number().nonnegative(),
    remain_balance_amount: z.number(),
  });
export const AmortizationResponseSchema = z.object({
    amortization_periods: z.array(AmortizationPeriodSchema).nonempty(),
  });