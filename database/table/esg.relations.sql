USE [ESG]
GO

/****** Object:  Table [esg].[relations]    Script Date: 3/22/2025 7:30:41 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [esg].[relations](
	[relation_id] [int] IDENTITY(1,1) NOT NULL,
	[related_item1_id] [int] NOT NULL,
	[related_item2_id] [int] NOT NULL,
	[relation_between] [varchar](100) NULL,
	[creation_date] [date] NULL,
	[is_relation_active] [bit] NULL,
PRIMARY KEY CLUSTERED 
(
	[relation_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

