USE [ESG]
GO

/****** Object:  Table [esg].[indicator_attributes]    Script Date: 3/22/2025 7:29:21 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [esg].[indicator_attributes](
	[attribute_id] [int] IDENTITY(0,1) NOT NULL,
	[linked_indicator_name] [varchar](500) NOT NULL,
	[attribute_name] [varchar](900) NOT NULL,
	[measuring_unit] [varchar](50) NULL,
	[GWP_Factor] [float] NULL,
	[scope] [varchar](50) NULL,
	[category] [varchar](500) NULL,
	[user_id] [int] NOT NULL,
	[user_defined] [bit] NULL,
PRIMARY KEY CLUSTERED 
(
	[attribute_id] ASC,
	[linked_indicator_name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [esg].[indicator_attributes] ADD  DEFAULT ((1)) FOR [user_id]
GO

ALTER TABLE [esg].[indicator_attributes] ADD  DEFAULT ((0)) FOR [user_defined]
GO

ALTER TABLE [esg].[indicator_attributes]  WITH CHECK ADD FOREIGN KEY([category])
REFERENCES [esg].[sustainability_metrics] ([name])
GO

