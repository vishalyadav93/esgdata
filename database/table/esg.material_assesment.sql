USE [ESG]
GO

/****** Object:  Table [esg].[material_assesment]    Script Date: 3/22/2025 7:30:30 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [esg].[material_assesment](
	[user_id] [int] NOT NULL,
	[material_name] [varchar](800) NOT NULL,
	[effective_date] [date] NULL,
	[linked_indicator_name] [varchar](900) NULL,
PRIMARY KEY CLUSTERED 
(
	[user_id] ASC,
	[material_name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

