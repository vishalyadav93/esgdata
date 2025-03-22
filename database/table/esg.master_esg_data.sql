USE [ESG]
GO

/****** Object:  Table [esg].[master_esg_data]    Script Date: 3/22/2025 7:30:14 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [esg].[master_esg_data](
	[user_id] [int] NOT NULL,
	[indicator] [int] NOT NULL,
	[data_date] [date] NOT NULL,
	[effective_date] [date] NULL,
	[expiry_date] [date] NULL,
	[value] [float] NULL,
	[data_frequency_in_days] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[user_id] ASC,
	[indicator] ASC,
	[data_date] ASC,
	[data_frequency_in_days] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

