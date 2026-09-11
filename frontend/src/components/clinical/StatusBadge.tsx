/**
 * MedPredict AI — StatusBadge Component
 * Restrained medical status pill badge with subtle borders and typography
 */

import React from 'react';

export type StatusType = 'healthy' | 'warning' | 'critical' | 'info' | 'neutral';

interface StatusBadgeProps {
  status: StatusType | string;
  label?: string;
  pulse?: boolean;
}

export const StatusBadge: React.FC<StatusBadgeProps> = ({
  status,
  label,
  pulse = false,
}) => {
  const norm = status.toLowerCase();

  let styles = 'bg-ivory text-slateText border-borderLine';
  let dotColor = 'bg-slateText';
  let defaultLabel = 'Unknown';

  if (norm === 'healthy' || norm === 'normal' || norm === 'low') {
    styles = 'bg-status-healthyBg text-status-healthy border-status-healthyBorder';
    dotColor = 'bg-status-healthy';
    defaultLabel = 'Normal / Low Risk';
  } else if (norm === 'warning' || norm === 'moderate' || norm === 'borderline') {
    styles = 'bg-status-warningBg text-status-warning border-status-warningBorder';
    dotColor = 'bg-status-warning';
    defaultLabel = 'Moderate / Warning';
  } else if (norm === 'critical' || norm === 'high' || norm === 'urgent') {
    styles = 'bg-status-criticalBg text-status-critical border-status-criticalBorder';
    dotColor = 'bg-status-critical';
    defaultLabel = 'High / Critical';
  } else if (norm === 'info' || norm === 'active') {
    styles = 'bg-status-infoBg text-status-info border-status-infoBorder';
    dotColor = 'bg-status-info';
    defaultLabel = 'Informational';
  }

  return (
    <span
      className={`inline-flex items-center space-x-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-semibold border ${styles}`}
    >
      <span
        className={`w-1.5 h-1.5 rounded-full ${dotColor} ${
          pulse ? 'animate-pulse' : ''
        }`}
      />
      <span>{label || defaultLabel}</span>
    </span>
  );
};
