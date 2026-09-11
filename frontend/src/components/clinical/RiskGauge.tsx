/**
 * MedPredict AI — Clinical Risk Gauge Component
 * Elegant circular SVG risk meter calibrated to clinical probability thresholds
 */

import React from 'react';
import { ShieldAlert, CheckCircle2, AlertTriangle, AlertCircle } from 'lucide-react';

interface RiskGaugeProps {
  probability: number; // 0.0 to 1.0 or 0 to 100
  riskTier?: 'LOW' | 'MODERATE' | 'HIGH' | 'CRITICAL';
  diseaseName?: string;
  confidenceInterval?: [number, number];
  size?: number;
}

export const RiskGauge: React.FC<RiskGaugeProps> = ({
  probability,
  riskTier,
  diseaseName = 'Cardiovascular Risk Assessment',
  confidenceInterval,
  size = 220,
}) => {
  // Normalize probability to percentage 0 - 100
  const pct = probability > 1.0 ? probability : probability * 100;
  const clampedPct = Math.max(0, Math.min(100, pct));

  // Determine tier if not explicitly passed
  let tier = riskTier;
  if (!tier) {
    if (clampedPct < 35) tier = 'LOW';
    else if (clampedPct < 65) tier = 'MODERATE';
    else if (clampedPct < 85) tier = 'HIGH';
    else tier = 'CRITICAL';
  }

  // Tier configuration
  const tierConfig = {
    LOW: {
      label: 'Low Risk Tier',
      textColor: 'text-status-healthy',
      bgColor: 'bg-status-healthyBg',
      borderColor: 'border-status-healthyBorder',
      strokeColor: '#16A34A',
      icon: CheckCircle2,
      description: 'Standard surveillance interval. Maintain non-pharmacological lifestyle counseling.',
    },
    MODERATE: {
      label: 'Moderate Risk Tier',
      textColor: 'text-status-warning',
      bgColor: 'bg-status-warningBg',
      borderColor: 'border-status-warningBorder',
      strokeColor: '#D97706',
      icon: AlertTriangle,
      description: 'Consider initiating primary prevention GDMT. Reassess biomarkers within 60–90 days.',
    },
    HIGH: {
      label: 'High Risk Tier',
      textColor: 'text-status-critical',
      bgColor: 'bg-status-criticalBg',
      borderColor: 'border-status-criticalBorder',
      strokeColor: '#DC2626',
      icon: ShieldAlert,
      description: 'Immediate clinical review indicated. Recommend combination guideline pharmacotherapy.',
    },
    CRITICAL: {
      label: 'Critical / Emergency Tier',
      textColor: 'text-status-critical',
      bgColor: 'bg-status-criticalBg',
      borderColor: 'border-status-criticalBorder',
      strokeColor: '#991B1B',
      icon: AlertCircle,
      description: 'Urgent diagnostic escalation required. Evaluate for acute decompensation.',
    },
  }[tier];

  // SVG Geometry for semi-circle / 240-degree gauge
  const radius = (size - 30) / 2;
  const strokeWidth = 14;
  const circumference = 2 * Math.PI * radius;
  const arcLength = (240 / 360) * circumference;
  const strokeDashoffset = arcLength - (clampedPct / 100) * arcLength;

  const IconComponent = tierConfig.icon;

  return (
    <div className="bg-surface rounded-card p-5 border border-borderLine shadow-medical flex flex-col items-center justify-between relative overflow-hidden">
      <div className="relative z-10 w-full flex flex-col items-center">
        {/* Header Title */}
        <span className="text-[11px] font-bold uppercase tracking-wider text-slateText font-mono mb-2">
          {diseaseName}
        </span>

        {/* Circular SVG Gauge */}
        <div className="relative my-2" style={{ width: size, height: size - 30 }}>
          <svg
            width={size}
            height={size}
            viewBox={`0 0 ${size} ${size}`}
            className="transform -rotate-120 overflow-visible"
          >
            {/* Background Track */}
            <circle
              cx={size / 2}
              cy={size / 2}
              r={radius}
              fill="none"
              stroke="#E2E8F0"
              strokeWidth={strokeWidth}
              strokeDasharray={`${arcLength} ${circumference}`}
              strokeLinecap="round"
            />
            {/* Active Calibrated Arc */}
            <circle
              cx={size / 2}
              cy={size / 2}
              r={radius}
              fill="none"
              stroke={tierConfig.strokeColor}
              strokeWidth={strokeWidth}
              strokeDasharray={`${arcLength} ${circumference}`}
              strokeDashoffset={strokeDashoffset}
              strokeLinecap="round"
              className="transition-all duration-1000 ease-out"
            />
          </svg>

          {/* Centered Readout */}
          <div className="absolute inset-0 flex flex-col items-center justify-center pt-2">
            <span className="text-4xl font-extrabold text-navy-800 tracking-tight font-sans">
              {clampedPct.toFixed(1)}%
            </span>
            <span className="text-[11px] font-semibold text-slateText tracking-wide uppercase mt-0.5">
              Calibrated Probability
            </span>
          </div>
        </div>

        {/* Risk Classification Badge */}
        <div
          className={`mt-3 inline-flex items-center space-x-1.5 px-3 py-1 rounded-full text-xs font-bold border ${tierConfig.bgColor} ${tierConfig.textColor} ${tierConfig.borderColor}`}
        >
          <IconComponent className="w-3.5 h-3.5" />
          <span>{tierConfig.label}</span>
        </div>

        {/* Confidence Interval Readout */}
        {confidenceInterval && (
          <p className="text-[11px] text-slateText mt-2 font-mono">
            95% Confidence Interval: [{confidenceInterval[0].toFixed(1)}% — {confidenceInterval[1].toFixed(1)}%]
          </p>
        )}

        {/* Clinical Narrative Explanation */}
        <div className="mt-4 p-3 bg-ivory/80 rounded-btn border border-borderLine text-xs text-charcoal leading-relaxed text-left w-full">
          <p className="font-semibold text-navy-800 mb-1">Clinical Decision Advisory:</p>
          <p className="text-slateText">{tierConfig.description}</p>
        </div>
      </div>
    </div>
  );
};
